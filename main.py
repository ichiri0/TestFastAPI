from colorama import init, Fore
import logging
import sys
from fastapi import FastAPI
import uvicorn

import settings
from api.api_v1.routers.users.controller import router as users_router


init(autoreset=True)

color_info = Fore.GREEN
color_error = Fore.RED

app = FastAPI(title="Заметки")
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_IP,
                port=settings.SERVER_PORT, reload=True)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
