from libs.api import ApiHandler
from modules.user.controller import UserController
from modules.spending.controller import SpendingController

api = ApiHandler()
api.inject_router(UserController.router)
api.inject_router(SpendingController.router)
api.start()