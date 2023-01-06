import random
from loguru import logger
from labelu_ml.model import LabelUMLBase


class MyModel(LabelUMLBase):
    def __init__(
        self,
        **kwargs
    ):
        super(MyModel, self).__init__(**kwargs)

    def predict(self, sample: dict, **kwargs) -> dict:
        logger.debug("get predict resut on: {sample}")
        return {
                'result': "prediction result",
                'score': random.uniform(0, 1)
            }
