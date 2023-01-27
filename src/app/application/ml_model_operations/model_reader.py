from typing import Any
from app.core.constants.blob_directory_names import MODELS_DIRECTORY_NAME as directory
from app.core.enums.prediction_type import PredictionType
from app.application.resolvers.blob_file_names.ml_model import MLModelFileNameResolver
from app.data_access.data_stores.blob.base import BaseBlobClient
from tensorflow.keras import Model
from tensorflow.keras.models import model_from_json

class ModelReader(object):

    def __init__(self, 
    blob_client: BaseBlobClient) -> None:
        self.__blob_client: BaseBlobClient = blob_client
        self.__directory: str = directory
        
    def get_model(self, prediction_type: PredictionType) -> Model:
        blob_name: str = MLModelFileNameResolver.resolve_file_name(prediction_type)

        model_blob: Any = self.__blob_client.get_blob(self.__directory, blob_name)

        model_json: str = None

        if isinstance(model_blob, bytes):
            model_json = model_blob.decode('utf8').replace("'", '"')
        else:
            model_json = model_blob

        return model_from_json(model_json)