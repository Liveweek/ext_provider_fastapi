from typing import Literal, Union
from pydantic import BaseModel, Field


from ext_provider.base import ExternalObjectBase, ExternalObjectType


class ExternalCSV(ExternalObjectBase):
    object_type:   Literal[ExternalObjectType.CSV] = ExternalObjectType.CSV
    fs_connect_id: str
    file_path:     str
    separator:     str = Field(min_length=1, max_length=1)
    

class ExternalExcel(ExternalObjectBase):
    object_type:   Literal[ExternalObjectType.EXCEL] = ExternalObjectType.EXCEL
    fs_connect_id: str
    file_path:     str
    
    
class ExternalDBTable(ExternalObjectBase):
    object_type:     Literal[ExternalObjectType.DB_TABLE] = ExternalObjectType.DB_TABLE
    dbms_connect_id: str
    table_name:      str
    table_schema:    str
    

class RequestMethod(BaseModel):
    path: str
    request_method: Literal['GET', 'POST', 'PUT', 'DELETE']
    requets_params: dict[str, str] | None
    
    
class ExternalWebService(ExternalObjectBase):
    object_type:              Literal[ExternalObjectType.WEB_SERVICE] = ExternalObjectType.WEB_SERVICE
    ws_connect_id:            str
    external_data_object:     Union[ExternalDBTable, ExternalCSV, ExternalExcel] = Field(discriminator="object_type")
    get_status_request:       RequestMethod | None 
    learn_trigger_request:    RequestMethod | None
    get_data_request:         RequestMethod | None
    
    
class State(BaseModel):
    state_id : str
    state_value: str
    
class ExternalResource(BaseModel):
    resource_cd:          str
    resource_description: str
    tags:                 list[str]
    external_obj:         Union[ExternalDBTable, ExternalCSV, ExternalExcel, ExternalWebService] = Field(discriminator="object_type")
    state:                dict[str, State]