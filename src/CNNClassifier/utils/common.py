# We Use utils for the functions which are frequently used in other components of the project

import os
from box.exceptions import BoxValueError
import yaml  
# (yaml)  Certainly! YAML (YAML Ain't Markup Language) is a way to store and share data in a very readable and user-friendly format. It's often used for:

# 1. **Configuration Files**: Think of it like a settings file for software. Instead of having a complicated file full of code, you can use YAML to specify how a program should work. It's easier for humans to understand.

# 2. **Data Storage**: You can save lists, dictionaries, and other structured data in YAML files. It's like a more organized way to save information for your programs to use.

# 3. **Communication Between Programs**: When different programs need to talk to each other, they can use YAML to exchange data. It's like speaking the same language, making it easy to understand each other's information.

# 4. **Automation**: People use YAML in tools like Ansible and Docker to define how to set up and run applications. It's a way to tell computers what to do, and it's easier for people to write and understand.

# In simple terms, YAML is like a friendly middle-ground language for humans and computers to share information, settings, and instructions. It makes data more readable and accessible.

from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
# The ensure module can be used to validate any type of condition, such as the type of a variable, the length of a string, or the value of a dictionary key. It is a useful tool for writing more robust and reliable Python code.
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml (path_to_yaml : Path) -> ConfigBox:
    """ Reads the yaml file and return 
    
    Args:
        Path_to_yaml(str) : path like input

    Raises:
        valueError: if the yaml file is empty
        e: empty file

    Returns:

        ConfigBox : ConfigBox type
    
    """

    try:

        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list , verbose=True):
    """
    create list of directories

    Args:
        path_to_directories (list) : list of path of directories
        ignore_log (bool , optional) : ignore if multiple dirs is to be created. Default to False.
    
    
    """

    
    for path in path_to_directories:

        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

        
@ensure_annotations
def save_json(path: Path , data :dict):

    """
    save json data

    Args:
        path(Path) : path to json file
        data(dict) : data to be saved in json file

    """

    with open(path , "w") as f:
        json.dump(data , f , indent=4)

    logger.info(f"json saved file at : {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data : Any , path:Path):
    """ save binary file
    
    Args:
        data(Any) : data to be saved as binary
        path(Path) : path to save binary file
        
    """

    joblib.dump(value=data , filename=path)
    logger.info(f"save binary file at: {path}")



@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())





# **import os**

# The `os` module provides a number of functions for interacting with the operating system, such as getting the current working directory, creating new files and directories, and listing the contents of a directory.

# This module is often used to perform tasks such as reading and writing files, creating and deleting directories, and executing system commands.

# **from box.exceptions import BoxValueError**

# The `BoxValueError` exception is raised by the `box` module when a configuration value is invalid.

# This exception can be used to validate configuration values and ensure that they meet certain requirements.

# **import yaml**

# The `yaml` module provides a Python library for parsing and generating YAML files.

# YAML is a human-readable data serialization language that is often used to store configuration files.

# This module is used to load and save configuration files in the `ConfigBox` class.

# **import cnnClassifier**

# The `cnnClassifier` module is a custom Python module that implements a convolutional neural network (CNN) classifier.

# This module is used to train and deploy a CNN model to classify images.

# **import json**

# The `json` module provides a Python library for parsing and generating JSON files.

# JSON is a lightweight data-interchange format that is often used to store and transmit data between different systems.

# This module is used to serialize and deserialize configuration values in the `ConfigBox` class.

# **import joblib**

# The `joblib` module provides a Python library for persisting and loading Python objects.

# This module is used to save and load the trained CNN model in the `cnnClassifier` module.

# **from ensure import ensure_annotations**

# The `ensure_annotations()` function is a custom Python function that uses the `ensure` library to validate that the function signature annotations are met.

# This function is used to ensure that the function signatures are consistent and that the correct types of data are passed to the functions.

# **from box import ConfigBox**

# The `ConfigBox` class is a Python class that provides a convenient way to load and manage configuration files.

# This class is used to load and manage the configuration files in the application.

# **from pathlib import Path**

# The `Path` class from the `pathlib` module provides a robust and efficient way to work with file paths.

# This class is used to normalize and manipulate file paths in the application.

# **import typing**

# The `typing` module provides a Python library for providing type hints.

# Type hints are used to specify the expected types of data for variables, function arguments, and return values.

# This module is used to make the code more readable and maintainable.

# **import base64**

# The `base64` module provides a Python library for encoding and decoding binary data to and from ASCII strings.

# This module is often used to encode and decode images and other types of binary data.


