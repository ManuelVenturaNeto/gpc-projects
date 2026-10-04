from google.cloud import storage
from .config import settings

def create_bucket():

    storage_client = storage.Client()

    bucket = storage_client.bucket(settings.BUCKET)
    bucket.storage_class = 'STANDARD'

    if storage_client.lookup_bucket(settings.BUCKET) is None:
        storage_client.create_bucket(bucket, location=settings.REGION)

    return bucket