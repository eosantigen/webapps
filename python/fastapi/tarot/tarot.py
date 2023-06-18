from fastapi import FastAPI
import routers.arcana.major.routes as major_arcana

api = FastAPI()

api.include_router(major_arcana.routes)


@api.get('/')
async def root():
    return {"message": "Hello World"}
