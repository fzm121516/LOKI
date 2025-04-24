import datetime
import os
import json
import yaml
import argparse
import sys

from loguru import logger as eval_logger

from lm_evaluate.models import *
from lm_evaluate.tasks import *
from lm_evaluate.api.registry import MODEL_REGISTRY, TASK_REGISTRY


"""
    TODO: Set verbosity -- DONE
    TODO: Allow multi-gpu inference -- DONE
    TODO: More intricate evaluation results, i.e., we should print a pretty table at the end. -- DONE
    TODO: Add more metrics for synthbench. We need to calculate which generate model the LMM can predict correctly the most. -- DONE
    TODO: Add LLaVA-NeXT-Video -- DONE
    TODO: Add XComposer-2.5 -- DONE
    TODO: Add VILA -- DONE
    TODO: Add internvl2 -- DONE
    TODO: Add MPlug-Owl3 -- DONE
    TODO: Add mistral api -- DONE
    TODO: Add datetime to log file -- DONE
    TODO: Add generation config for each model
    TODO: Rewrite config logic -- DONE
    TODO: Aggregate batch_generate and generate
    TODO: Split LOKI into subtasks
"""
import numpy as np
import torch
import random
seed = 42
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


def main(args):
    
    eval_logger.remove()
    eval_logger.add(sys.stdout, colorize=True, level=args.verbosity)
    eval_logger.info(f"Verbosity set to {args.verbosity}")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
        
    if not os.path.exists(args.model_config_path):
        eval_logger.error(f"Model config path: {args.model_config_path} does not exist.")
    
    if not os.path.exists(args.task_config_path):
        eval_logger.error(f"Task config path: {args.task_config_path} does not exist.")
    
    model_config = yaml.load(open(args.model_config_path), Loader=yaml.SafeLoader)
    task_config = yaml.load(open(args.task_config_path), Loader=yaml.SafeLoader)
    
    model_type = model_config["model_type"]
    task_type = task_config["task_type"]
    
    if task_type not in TASK_REGISTRY:
        eval_logger.error(f"No task named {task_type} is found. Supported tasks: {TASK_REGISTRY.keys()}")
        sys.exit(-1)
        
    model_init_kwargs = model_config["init_kwargs"]
    task_init_kwargs = task_config["init_kwargs"]
    task = TASK_REGISTRY[task_type](**task_init_kwargs)
    
    if args.evaluate_random:
        model_name = "random"
        results, accuracies = task.evaluate_random()
        
        accuracies['model_config'] = model_config
        accuracies['task_config'] = task_config
        
        now = datetime.datetime.now()
        datetime_str = now.strftime("%m%d_%H%M")
        
        task_name = task.task_name
        file_dir = os.path.join(args.log_dir, f"{model_type}_{task_type}", datetime_str)
        
        os.makedirs(file_dir, exist_ok=True)
        accuracy_file = os.path.join(file_dir, f"{model_name}_{task_name}_accuracy.json")
        result_file = os.path.join(file_dir, f"{model_name}_{task_name}_result.json")
        
        task.log_accuracies(accuracies, accuracy_file)
        task.log_results(results, result_file)
        
        return
    
    else:
        
        if model_type not in MODEL_REGISTRY:
            eval_logger.error(f"No model named {model_type} is found. Supported models: {MODEL_REGISTRY.keys()}")
            sys.exit(-1)
        
        if not args.evaluate_from_predictions:
            model = MODEL_REGISTRY[model_type](**model_init_kwargs)
            model_name = model.model_version.split("/")[-1]
            model_generate_kwargs = model_config["generate_kwargs"]
            
            model.accelerator.wait_for_everyone()
            
            if task.task_modality not in model.supported_modalities:
                eval_logger.error(f"Task: {task.task_name} is in {task.task_modality}. But Model: {model.model_version} only supports: {model.supported_modalities}.")
                sys.exit(-1)
            
            # FIXME: This is a temporary hack for batching
            if args.batch_size > 1:
                results, accuracies = task.batch_evaluate(model, predict_only=args.predict_only, batch_size=args.batch_size, **model_generate_kwargs)
            else:
                results, accuracies = task.evaluate(model, predict_only=args.predict_only, batch_size=args.batch_size, **model_generate_kwargs)
        
        else:
            model = None
            prediction_json = json.load(open(args.prediction_file, 'r'))
            responses = prediction_json["responses"]
            model_name = prediction_json["model"]
            results, accuracies = task.evaluate_from_predictions(responses)
    
    accuracies['model_config'] = model_config
    accuracies['task_config'] = task_config
    
    # start logging
    
    
    
    if model is None or model.rank == 0:
    # get log dir name
        now = datetime.datetime.now()
        datetime_str = now.strftime("%m%d_%H%M")
        
        task_name = task.task_name
        file_dir = os.path.join(args.log_dir, f"{model_type}_{task_type}", datetime_str)
        
        os.makedirs(file_dir, exist_ok=True)
        accuracy_file = os.path.join(file_dir, f"{model_name}_{task_name}_accuracy.json")
        result_file = os.path.join(file_dir, f"{model_name}_{task_name}_result.json")
        
        task.log_accuracies(accuracies, accuracy_file)
        task.log_results(results, result_file)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--model_config_path",
        type=str,
        required=True
    )
    parser.add_argument(
        "--task_config_path",
        type=str,
        required=True
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=1
    )
    parser.add_argument(
        "--log_dir",
        default="./logs",
        type=str
    )
    parser.add_argument(
        "--verbosity",
        type=str,
        default="INFO",
        help="Log error when tasks are not registered.",
    )
    parser.add_argument(
        "--evaluate_from_predictions",
        action="store_true"
    )
    parser.add_argument(
        "--predict_only",
        action="store_true"
    )
    parser.add_argument(
        "--prediction_file",
        type=str,
    )
    parser.add_argument(
        "--evaluate_random",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    main(args)
    
    