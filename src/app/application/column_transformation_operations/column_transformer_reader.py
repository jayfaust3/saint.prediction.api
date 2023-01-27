from typing import Any
from sklearn.compose import ColumnTransformer
from pickle import loads
from app.core.constants.blob_directory_names import COLUMN_TRANSFORMERS_DIRECTORY_NAME as directory
from app.core.enums.prediction_type import PredictionType
from app.application.resolvers.blob_file_names.column_transformer import ColumnTransformerFileNameResolver
from app.data_access.data_stores.blob.base import BaseBlobClient

class ColumnTransformerReader(object):

    def __init__(self, 
    blob_client: BaseBlobClient) -> None:
        self.__blob_client: BaseBlobClient = blob_client
        self.__directory: str = directory

    def get_column_transformer(self, prediction_type: PredictionType) -> ColumnTransformer:
        blob_name: str = ColumnTransformerFileNameResolver.resolve_file_name(prediction_type)

        blob: Any = self.__blob_client.get_blob(self.__directory, blob_name)

        transformer: ColumnTransformer = loads(blob)

        return transformer
