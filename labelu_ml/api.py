from loguru import logger
from fastapi import FastAPI

from labelu_ml.model import LabelUMLBase

app = FastAPI()


@app.get("/predict")
def read_main():
    logger.debug("request for get preannotation result")
    ml.predict("sample")
    return {"message": "preannotation result"}


def init_app(ml_instance: LabelUMLBase):
    logger.debug("init application")
    global ml
    ml = ml_instance
    return app
