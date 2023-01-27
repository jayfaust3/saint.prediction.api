from pandas import DataFrame
from app.application.column_transformation_operations.column_transformer_reader import ColumnTransformerReader
from app.core.data_models.criteria.saint.martyred import MartyredCriteriaModel
from app.application.predictors.base import BasePredictor
from tensorflow.keras import Model

class MartyredPredictor(BasePredictor[MartyredCriteriaModel]):
    
    def __init__(self,
    column_transformer_reader: ColumnTransformerReader) -> None:
        super().__init__(
            column_transformer_reader)

    def predict(self, model: Model, criteria: MartyredCriteriaModel) -> bool:
        prediction = super().predict(model, criteria)

        return bool(prediction)

    def _transform_criteria(self, criteria: MartyredCriteriaModel) -> DataFrame:
        sanitized_input = DataFrame()

        sanitized_input['year_of_death'] = [criteria.year_of_death]
        sanitized_input['age_at_death'] = [criteria.age_at_death]
        sanitized_input['region'] = [criteria.region]

        return sanitized_input