from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello": "World!"}


# @app.get("/component/{component_id}")  #path parameter
# async def get_component(component_id):
#     return {"conponent_id": component_id}

# @app.get("/component/") #query parameter
# async def read_component(number: int, text: str):
#     return {"nymber": number, "text": text}

class PackageIn(BaseModel):
    secret_token: int
    name: str
    number: str
    description: Optional[str] = None

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

# @app.post("/package/")
# async def make_package(priority: int, package: Package, value: bool):
#     return {"priority": priority, **package.dict(), "value": value}


@app.post("/package/", response_model=Package) #post request using response model
async def make_package(package: PackageIn):
    return package