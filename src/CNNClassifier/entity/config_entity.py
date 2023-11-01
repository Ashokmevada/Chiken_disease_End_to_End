from dataclasses import dataclass
from pathlib import Path

"""
The frozen=True argument specifies that instances of this dataclass should be immutable, meaning their attributes cannot be changed after creation. This is a useful feature when you want to ensure that the data within an instance remains constant throughout its lifecycle, which can be helpful for scenarios like configuration settings.

"""
@dataclass(frozen = True) 
class DataIngestionConfig:
    root_dir: Path
    source_dir : str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_dir: Path
    checkpoint_model_filepath: Path