import logging

import uvicorn
from fastapi import FastAPI
from fastapi.logger import logger
from routes import router as api_router

# from starlette.middleware import Middleware
# from starlette.middleware.sessions import SessionMiddleware

# middleware = [Middleware(SessionMiddleware, secret_key="secret_key")]
# app = FastAPI(middleware=middleware)
app = FastAPI()
app.include_router(api_router)


logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', log_level="info", port=8001, reload=True)
