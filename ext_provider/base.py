from pydantic import BaseModel, Extra
from enum import Enum


class ExternalObjectType(str, Enum):
    DB_TABLE    = 'DB_TABLE'
    CSV         = 'CSV'
    EXCEL       = 'EXCEL'
    WEB_SERVICE = 'WEB_SERVICE'
    

class ExternalObjectBase(BaseModel):
    object_type: ExternalObjectType
    
    class Config:
        extra = Extra.forbid