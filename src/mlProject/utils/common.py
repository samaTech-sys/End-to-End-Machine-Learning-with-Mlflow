#THis file has common mathods that will be used throughout the project. Created thsm and I could just all them when needed
import os 
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any

@typechecked
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Reads Yaml file and returns 

    Args:
        path_to_yaml (Path): path to input 
        
    Raises: 
        ValueError: if yaml file is empty
        e: if yaml file is empty 

    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml.resolve()} loaded successfully")  
            return ConfigBox(content)  
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
        
@typechecked
def create_directories(path_to_directories:list, verbose=True):
    """
    Create list of directories 

    Args:
        path_to_directories (list): List of path to directories 
        verbose (bool, optional): Ignore id multiple directories is to be created. Default is false.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
            
@typechecked
def save_json(path:Path, data:dict):
    """
    Save Json file

    Args:
        path (Path): path to json file 
        data (dict): data to be saved to json file 
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")

@typechecked
def load_json(path:Path)->ConfigBox:
    """
    Loadsjson file

    Args:
        path (Path): Path of jsonfile being loaded

    Returns:
        ConfigBox: data as class attributes loaded in dict
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from at: {path}")
        return ConfigBox(content)
    
@typechecked
def save_bin(data:Any, path:Path):
    """
    Save Binary path

    Args:
        data (Any): data to be saved as binary 
        path (Path): path to binary file
    """
    with open(path, "w") as f:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
        
@typechecked
def load_bin(path:Path)->Any:
    """
    Load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: any object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary data loaded from: {path}")
    return data

@typechecked
def get_size(path:Path)-> str:
    """
    Get Size in KB 

    Args:
        path (Path): path to file 

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"