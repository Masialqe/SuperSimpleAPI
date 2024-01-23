from fastapi import APIRouter

testRouter = APIRouter()

""" Test API connectivity """
@testRouter.get("/isalive", status_code= 200)
def IsAlive():
    return {
        "isAlive": True
    }
