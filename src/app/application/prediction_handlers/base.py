from abc import ABC
from typing import Any, Generic
from traceback import format_exception
from app.core.constants.generics import TCriteria
from app.core.data_models.error import ErrorModel
from app.logging_management.logger import Logger
from tensorflow.keras import Model
from app.application.ml_model_operations.model_reader import ModelReader
from app.application.prediction_precision_calculators.prediction_precision_calculator import PredictionPrecisionCalculator
from app.core.data_models.prediction import PredictionModel
from app.application.predictors.base import BasePredictor

class BasePredictionHandler(Generic[TCriteria], ABC):

    def __init__(self, 
    model_reader: ModelReader,
    predictor: BasePredictor[TCriteria],
    logger: Logger) -> None:
        self.__model_reader: ModelReader = model_reader
        self.__predictor: BasePredictor[TCriteria] = predictor,
        self.__logger: Logger = logger

    def make_prediction(self, criteria: TCriteria) -> PredictionModel:
        try:
            print('Making prediction of type: `{0}`'.format(self.__prediction_type.name).replace('`', "'"))

            model: Model = self.__model_reader.get_model(criteria.prediction_type)

            prediction: Any = self.__predictor.predict(model, criteria)
            
            precision: float = PredictionPrecisionCalculator.get_prediction_precision(model)

            return PredictionModel(prediction = prediction, precision = precision)
        except Exception as err:
            error_model = ErrorModel(stack_trace = ''.join(format_exception(None, err, err.__traceback__)), 
            error_message = str(err),
            optional_data = 'Unable to make prediction, Prediction Type: `{0}`'.format(self.__prediction_type.name).replace('`', "'"))
            
            self.__logger.log_error(error_model)
