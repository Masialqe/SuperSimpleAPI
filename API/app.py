from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from . import controller
import uvicorn


app = FastAPI()
app.include_router(controller.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000 openapi_prefix="/api")

