{{ config(materialized='view') }}

select
    -- identifiers
	dispatching_base_num,
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    cast(pulocationid as integer) as  pickup_locationid,
    cast(dolocationid as integer) as dropoff_locationid,
    SR_Flag, 
    Affiliated_base_number
from {{ source('staging','fhv_2019') }} where pickup_datetime >= '2019-01-01' AND pickup_datetime < '2020-01-01'

