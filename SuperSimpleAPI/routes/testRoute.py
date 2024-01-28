from fastapi import APIRouter

testRouter = APIRouter()

@testRouter.get("/isalive", status_code= 200)
def IsAlive():
    """ Test API connectivity """
    return {
        "isAlive": True
    }
