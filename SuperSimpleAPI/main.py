from fastapi import FastAPI
from routes.filmRoute import router
from routes.testRoute import testRouter
import uvicorn

#FastAPI Instance
app = FastAPI()

#add endpoints
app.include_router(router, prefix="/api/v1")
app.include_router(testRouter, prefix="/api/v1")

#configure uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


