from typing import Literal, Union
from pydantic import BaseModel, Field


from ext_provider.base import DatasetBase, DatasetType


class DatasetCSV(DatasetBase):
    dataset_type:  Literal[DatasetType.CSV] = DatasetType.CSV
    fs_connect_id: str
    file_path:     str
    separator:     str = Field(min_length=1, max_length=1)
    

class DatasetExcel(DatasetBase):
    dataset_type:  Literal[DatasetType.EXCEL] = DatasetType.EXCEL
    fs_connect_id: str
    file_path:     str
    
    
class DatasetDBTable(DatasetBase):
    dataset_type:    Literal[DatasetType.DB_TABLE] = DatasetType.DB_TABLE
    dbms_connect_id: str
    table_name:      str
    table_schema:    str
    
    
class State(BaseModel):
    state_id : str
    state_value: str
    
class ExternalResource(BaseModel):
    resource_cd:          str
    resource_description: str
    tags:                 list[str]
    dataset:              DatasetCSV | DatasetDBTable | DatasetExcel = Field(discriminator='dataset_type')
    state:                dict[str, State]