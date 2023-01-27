from abc import ABC, abstractmethod
from typing import Any, Generic
from app.core.constants.generics import TCriteria
from numpy import ndarray
from pandas.core.frame import DataFrame
from app.application.column_transformation_operations.column_transformer_reader import ColumnTransformerReader
from sklearn.compose import ColumnTransformer
from tensorflow.keras import Model

class BasePredictor(Generic[TCriteria], ABC):

    def __init__(self, 
    column_transformer_reader: ColumnTransformerReader) -> None:
        self.__column_transformer_reader: ColumnTransformerReader = column_transformer_reader

    def predict(self, model: Model, criteria: TCriteria, single_result: bool = True) -> Any:
        column_transformer: ColumnTransformer = self.__column_transformer_reader.get_column_transformer(criteria.prediction_type)

        raw_input_data: DataFrame = self._transform_criteria(criteria)

        transformed_input_data: DataFrame = column_transformer.transform(raw_input_data)

        predictions: ndarray = model.predict(transformed_input_data)

        if single_result: return predictions.item(0)

        return predictions

    @abstractmethod
    def _transform_criteria(self, criteria: TCriteria) -> DataFrame:
        pass