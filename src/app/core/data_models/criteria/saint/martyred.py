from app.core.enums.prediction_type import PredictionType
from app.core.data_models.criteria.base import BaseCriteriaModel

class MartyredCriteriaModel(BaseCriteriaModel):
    def __init__(self,
    year_of_death: int = None,
    age_at_death: int = None,
    region: str = None) -> None:
        super().__init__( 
            prediction_type = PredictionType.MARTYRED, 
        )
        self.year_of_death: int = year_of_death,
        self.age_at_death: int = age_at_death,
        self.region: str = region
        