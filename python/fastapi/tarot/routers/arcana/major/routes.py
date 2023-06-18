from fastapi import APIRouter

routes = APIRouter()

@routes.get('/major')
async def major():
    return {'0': 'The Fool', '1': 'The Magician'}