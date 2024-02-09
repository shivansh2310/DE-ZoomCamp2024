# Week 3 Homeowork

**SETUP:**
Create an external table using the Green Taxi Trip Records Data for 2022.
Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).

```sql
CREATE OR REPLACE EXTERNAL TABLE `de_bq.external_green_taxi_2022`
OPTIONS (
  format = 'parquet',
  uris = ['gs://de-zoomcamp_bq/Green_taxi_data/green_tripdata_2022-*.parquet']
);

```

**Question 1:** What is count of records for the 2022 Green Taxi Data?? 

- 65,623,481
- 840,402
- 1,936,423
- 253,647

```sql
SELECT COUNT(*) FROM `data-axiom-412014.de_bq.green_taxi_2022`;
```
```
840,402
```

**Question 2:** Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- 0 MB for the External Table and 6.41MB for the Materialized Table
- 18.82 MB for the External Table and 47.60 MB for the Materialized Table
- 0 MB for the External Table and 0MB for the Materialized Table
- 2.14 MB for the External Table and 0MB for the Materialized Table

```sql
SELECT DISTINCT(PULocationID) FROM `data-axiom-412014.de_bq.green_taxi_2022`;

SELECT DISTINCT(PULocationID) FROM `data-axiom-412014.de_bq.external_green_taxi_2022`;

```
```
0 MB for the External Table and 6.41MB for the Materialized Table
```

**Question 3:** How many records have a fare_amount of 0?

- 12,488
- 128,219
- 112
- 1,622

```sql
SELECT COUNT(*) FROM `data-axiom-412014.de_bq.green_taxi_2022` WHERE fare_amount = 0;
```
```
1,622
```

**Question 4:** What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

- Cluster on lpep_pickup_datetime Partition by PUlocationID
- Partition by lpep_pickup_datetime Cluster on PUlocationID
- Partition by lpep_pickup_datetime and Partition by PUlocationID
- Cluster on by lpep_pickup_datetime and Cluster on PUlocationID

```sql
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
```
```
Partition by lpep_pickup_datetime Cluster on PUlocationID
```


**Question 5:** Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

- 22.82 MB for non-partitioned table and 647.87 MB for the partitioned table
- 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table
- 5.63 MB for non-partitioned table and 0 MB for the partitioned table
- 10.31 MB for non-partitioned table and 10.31 MB for the partitioned table

```sql
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
```

```
12.82 MB for non-partitioned table and 1.12 MB for the partitioned table
```

**Question 6:** Where is the data stored in the External Table you created?

- Big Query
- GCP Bucket
- Big Table
- Container Registry

```
GCP Bucket
```

**Question 7:** It is best practice in Big Query to always cluster your data:

- True
- False

```
False
```

**Question 8:Bonus** Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

```sql
SELECT COUNT(*) FROM data-axiom-412014.de_bq.green_taxi_2022_2;
```

- Materialized table is faster and use fewer resources because the data is pre computed in materialized views, it uses pre-computed results from materialized views and and red-only changes from base tables to compute up-to-date results.