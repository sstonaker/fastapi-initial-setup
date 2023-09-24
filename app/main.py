import logging

import models
import utils
import uvicorn
from database import engine
from fastapi import FastAPI, status
from fastapi.logger import logger
from routes import router as api_router
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse

models.SQLModel.metadata.create_all(bind=engine)
# middleware is needed to access request.session object to send flash messages
middleware = [Middleware(SessionMiddleware, secret_key="secret_key")]
app = FastAPI(middleware=middleware)
app.include_router(api_router)


@app.exception_handler(400)
@app.exception_handler(502)
async def http_exception_handler(request, exc):
    utils.flash(request, f"{exc.detail} (Status Code: {exc.status_code})", "alert-danger")
    return RedirectResponse(
        url=request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER
    )

logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', log_level="info", reload=True)
