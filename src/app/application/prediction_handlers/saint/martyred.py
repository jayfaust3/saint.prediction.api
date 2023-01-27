from app.application.ml_model_operations.model_reader import ModelReader
from app.application.prediction_handlers.base import BasePredictionHandler
from app.application.predictors.base import BasePredictor
from app.core.data_models.criteria.saint.martyred import MartyredCriteriaModel
from app.logging_management.logger import Logger

class MartyredPredictionHandler(BasePredictionHandler[MartyredCriteriaModel]):

    def __init__(self,
    model_reader: ModelReader,
    predictor: BasePredictor[MartyredCriteriaModel],
    logger: Logger) -> None:
        super().__init__(model_reader = model_reader,
        predictor = predictor,
        logger = logger)
