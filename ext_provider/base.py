from pydantic import BaseModel, Extra
from enum import Enum


class DatasetType(str, Enum):
    DB_TABLE    = 'DB_TABLE'
    CSV         = 'CSV'
    EXCEL       = 'EXCEL'
    WEB_SERVICE = 'WEB_SERVICE'
    

class DatasetBase(BaseModel):
    dataset_type: DatasetType
    
    class Config:
        extra = Extra.forbid