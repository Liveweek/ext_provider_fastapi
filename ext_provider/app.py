from fastapi import FastAPI, APIRouter
import uvicorn


import ext_provider.models as m

ext_provider = APIRouter(
    prefix="/api_v1",
    tags=["External Resource Provider"]
)


@ext_provider.get('/resource/{resource_cd}', response_model=m.ExternalResource)
def get_resource(resource_cd: str):
    return m.ExternalResource(
        resource_cd="some.resource.cd",
        resource_description="resource description",
        tags=[
            "EXTERNAL",
            "CSV",
            "DATASET"
        ],
        dataset=m.DatasetCSV(
            fs_connect_id="fs_localhost",
            file_path=r"/data/models/my_file.csv",
            separator=","
        ),
        state = {
            "created_at": m.State(state_id="resource.cd.created_by", state_value="2023-05-17T11:00:00"),
            "is_readonly": m.State(state_id="resource.cd.is_readonly", state_value="True"),
            "max_dataset_date_to": m.State(state_id="resource.cd.max_dataset_date_to", state_value="2023-05-17T00:00:00"),
        }
    )
    

@ext_provider.post('/resource')
def create_resource(resource: m.ExternalResource):
    print(type(resource.dataset))
    return resource


@ext_provider.get('/resource/{resource_cd}/state')
def get_resource_state(resource_cd: str):
    ...
    


app = FastAPI()

app.include_router(ext_provider)
    
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("ext_provider.app:app", host="0.0.0.0", port=8000, reload=True)