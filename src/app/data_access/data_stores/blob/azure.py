from typing import Any
from azure.storage.blob import BlobServiceClient, BlobClient, StorageStreamDownloader
from azure.storage.blob._shared.authentication import SharedKeyCredentialPolicy
from app.data_access.data_stores.blob.base import BaseBlobClient

class AzureBlobClient(BaseBlobClient):

    def __init__(self,
    blob_service_client: BlobServiceClient,
    container_base_path: str) -> None:
        self.__blob_service_client: BlobServiceClient = blob_service_client
        self.__storage_path: str = container_base_path

    def get_blob(self, blob_directory: str, blob_name: str) -> Any:
        blob: Any = None
        
        blob_client: BlobClient = self.__get_blob_client(blob_directory, blob_name)

        if blob_client.exists():
            blob_stream: StorageStreamDownloader = blob_client.download_blob()

            blob = blob_stream.readall()

        return blob

    def post_blob(self, blob_directory: str, blob_name: str, data: Any) -> None:        
        blob_client: BlobClient = self.__get_blob_client(blob_directory, blob_name)

        if blob_client.exists():
            blob_client.delete_blob()

        blob_client.upload_blob(data = data)

        return

    def __get_blob_client(self, blob_directory: str, blob_name: str) -> BlobClient:
        url: str = self.__construct_url(blob_directory, blob_name)

        credential: SharedKeyCredentialPolicy = self.__blob_service_client.credential

        return BlobClient.from_blob_url(url, credential = credential)

    def __construct_url(self, blob_directory: str, blob_name: str) -> str:
        return '{}{}/{}'.format(self.__storage_path, blob_directory, blob_name)
