import io
import os
import requests
import pandas as pd
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
# init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "de-zoomcamp-bq")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"green_tripdata_{year}-{month:02}"

        # download it using requests via a pandas df
        request_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}.parquet"
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # read it back into a parquet file
        df = pd.read_parquet(file_name)
        
        # Add .parquet to the end of the file name
        n_file_name = file_name + ".parquet"

        # Rename the file
        os.rename(file_name, n_file_name)

        df.to_parquet(n_file_name, engine='pyarrow')
        print(f"Parquet: {n_file_name}")

        # upload it to gcs 
        upload_to_gcs(BUCKET, f"Green_taxi_data/{n_file_name}", n_file_name)
        print(f"GCS: Green_taxi_data/{n_file_name}")


web_to_gcs('2022')

