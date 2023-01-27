from config import settings
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory
from botocore import client
from app.data_access.data_stores.sql.connection_manager import ConnectionManager
from app.data_access.data_stores.sql.repositories.write import WriteRepository
from app.data_access.data_stores.sql.query_handlers.logging import LoggingQueryHandler
from app.data_access.data_stores.blob.s3 import S3Client
from app.logging_management.logger import Logger
from app.application.ml_model_operations.model_reader import ModelReader
from app.application.column_transformation_operations.column_transformer_reader import ColumnTransformerReader
from app.application.predictors.saint.martyred import MartyredPredictor
from app.application.prediction_handlers.saint.martyred import MartyredPredictionHandler

class Container(DeclarativeContainer):

    def __init__(self) -> None:
        pass

    __config = Configuration()

    __config.from_dict(settings)
    
    environment = __config.environment()

    # data access
    __logging_connection_manager = Factory(ConnectionManager, 
    host = __config.sql.logging_db.host(),
    database = __config.sql.logging_db.ldatabase(),
    username = __config.sql.logging_db.username(),
    password = __config.sql.logging_db.password())

    __logging_write_repository = Factory(WriteRepository,
    connection_manager = __logging_connection_manager)

    __logging_query_handler = Factory(LoggingQueryHandler,
    write_repository = __logging_write_repository)
    # data access

    #blob
    __blob_client = Factory(S3Client,
    s3_client = client(service_name = 's3',
    region_name = __config.aws.region(),
    aws_access_key_id = __config.aws.access_key_id(),
    aws_secret_access_key = __config.aws.access_key_secret(),
    endpoint_url = __config.blob.s3.endpoint()))
    #blob

    # logging
    __logger = Factory(Logger, 
    query_handler = __logging_query_handler)
    # logging

    # application

    # ml model ops
    __model_reader = Factory(ModelReader,
    blob_client = __blob_client)
    # ml model ops

    # column transformer ops
    __column_transformer_reader = Factory(ColumnTransformerReader,
    blob_client = __blob_client)
    # column transformer ops

    # predictors
    __martyred_predictor = Factory(MartyredPredictor,
    column_transformer_reader = __column_transformer_reader)
    # predictors

    # prediction handlers
    __martyred_prediction_handler = Factory(MartyredPredictionHandler,
    model_reader = __model_reader,
    predictor = __martyred_predictor,
    logger = __logger)
    # prediction handlers
    