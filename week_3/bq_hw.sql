SELECT * FROM `data-axiom-412014.de_bq.green_taxi_2022` LIMIT 10;

CREATE OR REPLACE EXTERNAL TABLE `de_bq.external_green_taxi_2022`
OPTIONS (
  format = 'parquet',
  uris = ['gs://de-zoomcamp_bq/Green_taxi_data/green_tripdata_2022-*.parquet']
);

--- 1> 

SELECT COUNT(*) FROM `data-axiom-412014.de_bq.green_taxi_2022`;

--- 2> 

SELECT DISTINCT(PULocationID) FROM `data-axiom-412014.de_bq.green_taxi_2022`;

SELECT DISTINCT(PULocationID) FROM `data-axiom-412014.de_bq.external_green_taxi_2022`;

--- 3> 

SELECT COUNT(*) FROM `data-axiom-412014.de_bq.green_taxi_2022` WHERE fare_amount = 0;

--- 4> 

--- Cluster on `lpep_pickup_datetime` Cluster on `PUlocationID`
--- Error
--- Entries in the CLUSTER BY clause must be column names
CREATE OR REPLACE TABLE data-axiom-412014.de_bq.green_taxi_2022_1
CLUSTER BY DATE(lpep_pickup_datetime), PUlocationID AS
  (SELECT *
   FROM data-axiom-412014.de_bq.green_taxi_2022);

--- Partition by `lpep_pickup_datetime` Cluster on `PUlocationID`
CREATE OR REPLACE TABLE data-axiom-412014.de_bq.green_taxi_2022_2
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
  (SELECT *
   FROM data-axiom-412014.de_bq.green_taxi_2022);

--- Partition by `lpep_pickup_datetime` Partition by `PUlocationID`
--- ERROR
--- Only a single PARTITION BY expression is supported but found 2
CREATE OR REPLACE TABLE data-axiom-412014.de_bq.green_taxi_2022_3
PARTITION BY DATE(lpep_pickup_datetime), PUlocationID AS
  (SELECT *
   FROM data-axiom-412014.de_bq.green_taxi_2022);

--- Partition by `PUlocationID` Cluster on `lpep_pickup_datetime`
--- ERROR
--- PARTITION BY expression must be DATE(<timestamp_column>), DATE(<datetime_column>), DATETIME_TRUNC(<datetime_column>, DAY/HOUR/MONTH/YEAR), a DATE column, TIMESTAMP_TRUNC(<timestamp_column>, DAY/HOUR/MONTH/YEAR), DATE_TRUNC(<date_column>, MONTH/YEAR), or RANGE_BUCKET(<int64_column>, GENERATE_ARRAY(<int64_value>, <int64_value>[, <int64_value>]))
CREATE OR REPLACE TABLE data-axiom-412014.de_bq.green_taxi_2022_4
PARTITION BY PUlocationID
CLUSTER BY DATE(lpep_pickup_datetime) AS
  (SELECT *
   FROM data-axiom-412014.de_bq.green_taxi_2022);

--- This query will process 12.82 MB when run.
SELECT COUNT(*)
FROM data-axiom-412014.de_bq.green_taxi_2022
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-03-01' AND '2022-03-31'
GROUP BY PUlocationID;

--- This query will process 647.87 MB when run.
SELECT COUNT(*)
FROM data-axiom-412014.de_bq.green_taxi_2022_1
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-03-01' AND '2022-03-31'
GROUP BY PUlocationID;

--- This query will process 1.2 MB when run.
--- This is the best strategy.
SELECT COUNT(*)
FROM data-axiom-412014.de_bq.green_taxi_2022_2
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-03-01' AND '2022-03-31'
GROUP BY PUlocationID;


--- 5>
--- Non-partitioned table.
--- This query will process 12.82 MB when run.
SELECT COUNT(DISTINCT PUlocationID)
FROM data-axiom-412014.de_bq.green_taxi_2022
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

--- Partitioned table.
--- This query will process 1.12 MB when run.
SELECT COUNT(DISTINCT PUlocationID)
FROM data-axiom-412014.de_bq.green_taxi_2022_2
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

--- Bonus (8)
--- This query will process 0 B when run.
SELECT COUNT(*) FROM data-axiom-412014.de_bq.green_taxi_2022_2;

