# RisingWave Workshop Homework

**SETUP:**
In this homework we'll put what we learned about Spark in practice.

For this homework we will be using the FHV 2019-10 data found here. FHV Data


**Question 1:** Create a materialized view to compute the average, min and max trip time between each taxi zone.

From this MV, find the pair of taxi zones with the highest average trip time. You may need to use the dynamic filter pattern for this.

Bonus (no marks): Create an MV which can identify anomalies in the data. For example, if the average trip time between two zones is 1 minute, but the max trip time is 10 minutes and 20 minutes respectively.

- Yorkville East, Steinway
- Murray Hill, Midwood
- East Flatbush/Farragut, East Harlem North
- Midtown Center, University Heights/Morris Heights

```sql
CREATE MATERIALIZED VIEW taxi_zone_stats AS
WITH trip_time AS (
SELECT
	tpep_dropoff_datetime - tpep_pickup_datetime AS trip_time,
	pulocationid,
	dolocationid
FROM trip_data
)
SELECT
	AVG(trip_time) AS avg_trip_time,
	MIN(trip_time) AS min_trip_time,
	MAX(trip_time) AS max_trip_time,
	tz_pickup.Zone AS pickup_zone,
	tz_dropoff.Zone AS dropoff_zone
FROM trip_time
JOIN taxi_zone AS tz_pickup ON tz_pickup.location_id=trip_time.pulocationid
JOIN taxi_zone AS tz_dropoff ON tz_dropoff.location_id=trip_time.dolocationid
GROUP BY pickup_zone, dropoff_zone;

```

```sql
SELECT
pickup_zone,
dropoff_zone,
avg_trip_time AS max_avg
FROM taxi_zone_stats
WHERE avg_trip_time=(SELECT MAX(avg_trip_time) FROM taxi_zone_stats);
```
```
Yorkville East, Steinway
```

**Question 2:** Recreate the MV(s) in question 1, to also find the number of trips for the pair of taxi zones with the highest average trip time.

- 1.5
- 2.3
- 3.10
- 4.1


```sql 
CREATE MATERIALIZED VIEW trip_time_sum_2 AS
SELECT
    tz1.zone AS pickup_zone,
    tz2.zone AS dropoff_zone,
    COUNT(*) AS number_trips,
    AVG(td.tpep_dropoff_datetime - td.tpep_pickup_datetime) AS avg_trip_time,
    MIN(td.tpep_dropoff_datetime - td.tpep_pickup_datetime) AS min_trip_time,
    MAX(td.tpep_dropoff_datetime - td.tpep_pickup_datetime) AS max_trip_time 
FROM
    trip_data td 
    JOIN taxi_zone tz1 
        ON td.PULocationID = tz1.location_id 
    JOIN taxi_zone tz2 
        ON td.DOLocationID = tz2.location_id 
GROUP BY
    1, 2;


```

```sql
SELECT
    pickup_zone,
    dropoff_zone,
    number_trips 
FROM
    trip_time_sum_2
ORDER BY
    avg_trip_time DESC
LIMIT 1; 
```

```
4.1
```

**Question 3:** From the latest pickup time to 17 hours before, what are the top 3 busiest zones in terms of number of pickups? For example if the latest pickup time is 2020-01-01 12:00:00, then the query should return the top 3 busiest zones from 2020-01-01 11:00:00 to 2020-01-01 12:00:00.


- Clinton East, Upper East Side North, Penn Station
- LaGuardia Airport, Lincoln Square East, JFK Airport
- Midtown Center, Upper East Side South, Upper East Side North
- LaGuardia Airport, Midtown Center, Upper East Side North

```sql
SELECT 
  tz.zone as pickup_zone,
  count(*) as number_trips
FROM 
  trip_data td
JOIN 
  taxi_zone tz ON td.pulocationid = tz.location_id
WHERE 
  td.tpep_pickup_datetime >= (SELECT MAX(tpep_pickup_datetime)-interval '17 hours' FROM trip_data)
  AND
  td.tpep_pickup_datetime <= (SELECT MAX(tpep_pickup_datetime) FROM trip_data)
GROUP BY
  pickup_zone
ORDER BY
  number_trips DESC
LIMIT 3;
```

```
LaGuardia Airport, Lincoln Square East, JFK Airport
```