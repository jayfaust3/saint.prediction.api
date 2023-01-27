from typing import TypeVar
from app.core.data_models.criteria.base import BaseCriteriaModel

TCriteria = TypeVar('TCriteria', bound = BaseCriteriaModel)