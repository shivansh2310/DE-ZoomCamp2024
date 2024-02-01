import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/data-axiom-412014-096d0aaa0530.json"

bucket_name = 'de-zoomcamp_mage'
project_id = 'data-axiom-412014'

table_name = "green_taxi_data"

root_path = f'{bucket_name}/{table_name}'




@data_exporter
def export_data(df_new, *args, **kwargs):

    table = pa.Table.from_pandas(df_new)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )

    