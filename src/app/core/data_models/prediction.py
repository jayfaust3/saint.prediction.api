from typing import Any

class PredictionModel(object):

    def __init__(self,
    prediction: Any = None, 
    precision: float = None) -> None:
        self.prediction: Any = prediction
        self.precision: float = precision
