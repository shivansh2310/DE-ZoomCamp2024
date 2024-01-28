Docker & SQL

--1)

docker build --help

--2)

winpty docker run -it python:3.9 bash
pip list

wheel      0.42.0


--3)

SELECT COUNT(*) 
FROM GREEN_TAXI_DATA
WHERE DATE(LPEP_PICKUP_DATETIME) = '2019-09-18' AND DATE(LPEP_DROPOFF_DATETIME) = '2019-09-18';

Ans :- 15612

--4)

SELECT DISTINCT DATE(LPEP_PICKUP_DATETIME) 
FROM GREEN_TAXI_DATA
WHERE TRIP_DISTANCE = (SELECT MAX(TRIP_DISTANCE) FROM GREEN_TAXI_DATA);

Ans :- 2019-09-26

--5)

SELECT tz.Borough, SUM(gt.total_amount) AS total_amount_sum
FROM taxi_zone tz
JOIN green_taxi_data gt ON tz.index = gt.index
WHERE gt.lpep_pickup_datetime >= '2019-09-18'
GROUP BY tz.Borough
HAVING SUM(gt.total_amount) > 50000
ORDER BY total_amount_sum DESC
LIMIT 3

--6)

WITH LOC AS 
(
  SELECT DISTINCT "LocationID" FROM TAXI_ZONE
  WHERE "Zone" = 'Astoria'
), TIP AS
(
  SELECT MAX(TIP_AMOUNT) FROM GREEN_TAXI_DATA
  WHERE "PULocationID" = (SELECT * FROM LOC)
), LOC_ID AS
(
	SELECT DISTINCT "DOLocationID" 
	FROM GREEN_TAXI_DATA 
	WHERE "PULocationID" = (SELECT * FROM LOC) AND TIP_AMOUNT = (SELECT * FROM TIP)
)

SELECT DISTINCT "Zone" FROM TAXI_ZONE
WHERE "LocationID" = (SELECT * FROM LOC_ID);

Ans :- JFK airport


Terraform

terraform apply

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + labels                     = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "data-axiom-412014"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + dataset {
              + target_types = (known after apply)

              + dataset {
                  + dataset_id = (known after apply)
                  + project_id = (known after apply)
                }
            }

          + routine {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + routine_id = (known after apply)
            }

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_data-axiom-412014"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }

      + website {
          + main_page_suffix = (known after apply)
          + not_found_page   = (known after apply)
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_storage_bucket.data-lake-bucket: Refreshing state... [id=dtc_data_lake_data-axiom-412014]
google_bigquery_dataset.dataset: Refreshing state... [id=projects/data-axiom-412014/datasets/trips_data_all]


Apply complete! Resources: 2 added, 0 changed, 0 destroyed.