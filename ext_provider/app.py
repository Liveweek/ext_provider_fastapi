from fastapi import FastAPI, APIRouter
import uvicorn


import ext_provider.models as m

ext_provider = APIRouter(
    prefix="/api_v1",
    tags=["External Resource Provider"]
)

@ext_provider.get('/resource')
def get_resources():
    ...


@ext_provider.post('/resource')
def create_resource(resource: m.ExternalResource):
    print(type(resource.dataset))
    return resource


@ext_provider.get('/resource/{resource_cd}', response_model=m.ExternalResource)
def get_resource(resource_cd: str):
    return m.ExternalResource(
        resource_cd="ext.crm.client_activity_model",
        resource_description="Веб-сервис модуля CRM по предсказанию клиентских активностей",
        tags=[
            "external",
            "ML",
            "CRM"
        ],
        external_obj=m.ExternalWebService(
            ws_connect_id='ml_model_ws_conn',
            external_data_object=m.ExternalExcel(
                fs_connect_id='ml_model_fs_conn',
                file_path='/data/reports/result_report.xlsx'
            ),
            get_status_request=m.RequestMethod(
                path="/api_v1/status",
                request_method="GET"
            ),
            learn_trigger_request=m.RequestMethod(
                path='/api_v1/start_learn',
                request_method="POST",
                requets_params={
                    "report_id": "123dasd134"
                }
            )
        ),
        state={
            "is_available": m.State(state_id="ext.crm.client_activity_model.is_available", state_value="True"),
            "last_request_activity": m.State(state_id="ext.crm.client_activity_model.last_request_activity", state_value="2023-05-17T22:00:00")
        }
    )
    

@ext_provider.put('/resource/{resource_cd}', response_model=m.ExternalResource)
def update_resource(resource_cd: str):
    ...


@ext_provider.get('/resource/{resource_cd}/state')
def get_resource_state(resource_cd: str):
    ...
    

@ext_provider.get('/resource_templates')
def get_resource_templates():
    ...



app = FastAPI()

app.include_router(ext_provider)
    
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("ext_provider.app:app", host="0.0.0.0", port=8000, reload=True)