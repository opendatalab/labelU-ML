from abc import ABC, abstractmethod


class LabelUMLBase(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def predict(self, sample: dict, **kwargs) -> dict:
        raise NotImplementedError
