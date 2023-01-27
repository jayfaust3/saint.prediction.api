from abc import ABC
from app.core.enums.prediction_type import PredictionType

class BaseCriteriaModel(ABC):

    def __init__(self, 
    prediction_type: PredictionType) -> None:
        self.prediction_type: PredictionType = prediction_type
