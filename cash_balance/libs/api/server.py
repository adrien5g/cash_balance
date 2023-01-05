import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from conf import get_config

class ApiHandler:
    def __init__(self, router_prefix:str = None) -> None:
        config = get_config()
        self.port = int(config.API_PORT)
        self.app = FastAPI()
        self.router = APIRouter()
        if router_prefix: self.router.prefix = router_prefix

    def inject_router(self, router:APIRouter):
        self.router.include_router(router)

    def start(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
        self.app.include_router(self.router)
        uvicorn.run(self.app, host='0.0.0.0', port=self.port, log_level='info')
