from fastapi import APIRouter
from views.predict import router as predict


main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    predict
]

[main_api_router.include_router(router) for router in routers]