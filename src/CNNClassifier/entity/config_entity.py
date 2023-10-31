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