from typing import Any
import attr
from attr.validators import instance_of

from pathlib import Path
import os

def create_path_checked(path_folder: Path) -> None:
    if not path_folder.exists():
        os.mkdir(path_folder)

@attr.s(frozen=True)
class DBConvGPT:
    """ FIXME: Ahora para safar voy a guardar 1 .json para
    cada persona, esto después tiene que ser una db."""
    path_folder_db: Path = attr.ib(validator=instance_of(Path))
    suffix: str = attr.ib(default=".json", init=False)
    
    create_path_checked(path_folder_db)

    def __getitem__(self, key: str):
        return