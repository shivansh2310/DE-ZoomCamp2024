{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5bda95db-7caa-4a9a-93a7-bd2e1cda5598",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9fd4a0e2-8a4c-43c3-ba68-1033c81e3359",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.5.3'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "096c0e7c-c59e-48a0-a4f4-e3a33d8ca06f",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ceff2d68-293e-429d-8190-6b6849d86a68",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(url, nrows = 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4ec8ef68-c729-4585-a5de-13752c3a15e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3575aaf5-feb5-4262-ba43-a65c6ad345ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>VendorID</th>\n",
       "      <th>lpep_pickup_datetime</th>\n",
       "      <th>lpep_dropoff_datetime</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>RatecodeID</th>\n",
       "      <th>PULocationID</th>\n",
       "      <th>DOLocationID</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>trip_distance</th>\n",
       "      <th>fare_amount</th>\n",
       "      <th>extra</th>\n",
       "      <th>mta_tax</th>\n",
       "      <th>tip_amount</th>\n",
       "      <th>tolls_amount</th>\n",
       "      <th>ehail_fee</th>\n",
       "      <th>improvement_surcharge</th>\n",
       "      <th>total_amount</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>trip_type</th>\n",
       "      <th>congestion_surcharge</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>2018-12-21 15:17:29</td>\n",
       "      <td>2018-12-21 15:18:57</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "      <td>264</td>\n",
       "      <td>264</td>\n",
       "      <td>5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.3</td>\n",
       "      <td>4.30</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2019-01-01 00:10:16</td>\n",
       "      <td>2019-01-01 00:16:32</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "      <td>97</td>\n",
       "      <td>49</td>\n",
       "      <td>2</td>\n",
       "      <td>0.86</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.3</td>\n",
       "      <td>7.30</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>2019-01-01 00:27:11</td>\n",
       "      <td>2019-01-01 00:31:38</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>189</td>\n",
       "      <td>2</td>\n",
       "      <td>0.66</td>\n",
       "      <td>4.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.3</td>\n",
       "      <td>5.80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>2019-01-01 00:46:20</td>\n",
       "      <td>2019-01-01 01:04:54</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "      <td>189</td>\n",
       "      <td>17</td>\n",
       "      <td>2</td>\n",
       "      <td>2.68</td>\n",
       "      <td>13.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>2.96</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.3</td>\n",
       "      <td>19.71</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2019-01-01 00:19:06</td>\n",
       "      <td>2019-01-01 00:39:43</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "      <td>82</td>\n",
       "      <td>258</td>\n",
       "      <td>1</td>\n",
       "      <td>4.53</td>\n",
       "      <td>18.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.3</td>\n",
       "      <td>19.30</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   VendorID lpep_pickup_datetime lpep_dropoff_datetime store_and_fwd_flag  \\\n",
       "0         2  2018-12-21 15:17:29   2018-12-21 15:18:57                  N   \n",
       "1         2  2019-01-01 00:10:16   2019-01-01 00:16:32                  N   \n",
       "2         2  2019-01-01 00:27:11   2019-01-01 00:31:38                  N   \n",
       "3         2  2019-01-01 00:46:20   2019-01-01 01:04:54                  N   \n",
       "4         2  2019-01-01 00:19:06   2019-01-01 00:39:43                  N   \n",
       "\n",
       "   RatecodeID  PULocationID  DOLocationID  passenger_count  trip_distance  \\\n",
       "0           1           264           264                5           0.00   \n",
       "1           1            97            49                2           0.86   \n",
       "2           1            49           189                2           0.66   \n",
       "3           1           189            17                2           2.68   \n",
       "4           1            82           258                1           4.53   \n",
       "\n",
       "   fare_amount  extra  mta_tax  tip_amount  tolls_amount  ehail_fee  \\\n",
       "0          3.0    0.5      0.5        0.00           0.0        NaN   \n",
       "1          6.0    0.5      0.5        0.00           0.0        NaN   \n",
       "2          4.5    0.5      0.5        0.00           0.0        NaN   \n",
       "3         13.5    0.5      0.5        2.96           0.0        NaN   \n",
       "4         18.0    0.5      0.5        0.00           0.0        NaN   \n",
       "\n",
       "   improvement_surcharge  total_amount  payment_type  trip_type  \\\n",
       "0                    0.3          4.30             2          1   \n",
       "1                    0.3          7.30             2          1   \n",
       "2                    0.3          5.80             1          1   \n",
       "3                    0.3         19.71             1          1   \n",
       "4                    0.3         19.30             2          1   \n",
       "\n",
       "   congestion_surcharge  \n",
       "0                   NaN  \n",
       "1                   NaN  \n",
       "2                   NaN  \n",
       "3                   NaN  \n",
       "4                   NaN  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3b104c23-af3b-494e-87cb-9a64c46e7680",
   "metadata": {},
   "outputs": [],
   "source": [
    "taxi_zone = pd.read_csv(\"https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f3c7e755-ea71-4f4a-8147-fc3ad7da0c41",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "265"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(taxi_zone)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d7a150ac-7217-44bc-bac2-e3e2ae53c577",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>LocationID</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Zone</th>\n",
       "      <th>service_zone</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>EWR</td>\n",
       "      <td>Newark Airport</td>\n",
       "      <td>EWR</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Jamaica Bay</td>\n",
       "      <td>Boro Zone</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Allerton/Pelham Gardens</td>\n",
       "      <td>Boro Zone</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Alphabet City</td>\n",
       "      <td>Yellow Zone</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Staten Island</td>\n",
       "      <td>Arden Heights</td>\n",
       "      <td>Boro Zone</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   LocationID        Borough                     Zone service_zone\n",
       "0           1            EWR           Newark Airport          EWR\n",
       "1           2         Queens              Jamaica Bay    Boro Zone\n",
       "2           3          Bronx  Allerton/Pelham Gardens    Boro Zone\n",
       "3           4      Manhattan            Alphabet City  Yellow Zone\n",
       "4           5  Staten Island            Arden Heights    Boro Zone"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "taxi_zone.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8f89e63d-c4af-423c-afb7-ab7750d21c54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"green_taxi_data\" (\n",
      "\"VendorID\" INTEGER,\n",
      "  \"lpep_pickup_datetime\" TEXT,\n",
      "  \"lpep_dropoff_datetime\" TEXT,\n",
      "  \"store_and_fwd_flag\" TEXT,\n",
      "  \"RatecodeID\" INTEGER,\n",
      "  \"PULocationID\" INTEGER,\n",
      "  \"DOLocationID\" INTEGER,\n",
      "  \"passenger_count\" INTEGER,\n",
      "  \"trip_distance\" REAL,\n",
      "  \"fare_amount\" REAL,\n",
      "  \"extra\" REAL,\n",
      "  \"mta_tax\" REAL,\n",
      "  \"tip_amount\" REAL,\n",
      "  \"tolls_amount\" REAL,\n",
      "  \"ehail_fee\" REAL,\n",
      "  \"improvement_surcharge\" REAL,\n",
      "  \"total_amount\" REAL,\n",
      "  \"payment_type\" INTEGER,\n",
      "  \"trip_type\" INTEGER,\n",
      "  \"congestion_surcharge\" REAL\n",
      ")\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, 'green_taxi_data'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6469885e-136d-4522-bd2b-327316b33a56",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)\n",
    "df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "13cc1434-5980-437d-88d5-6dc6e04fcfd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"green_taxi_data\" (\n",
      "\"VendorID\" INTEGER,\n",
      "  \"lpep_pickup_datetime\" TIMESTAMP,\n",
      "  \"lpep_dropoff_datetime\" TIMESTAMP,\n",
      "  \"store_and_fwd_flag\" TEXT,\n",
      "  \"RatecodeID\" INTEGER,\n",
      "  \"PULocationID\" INTEGER,\n",
      "  \"DOLocationID\" INTEGER,\n",
      "  \"passenger_count\" INTEGER,\n",
      "  \"trip_distance\" REAL,\n",
      "  \"fare_amount\" REAL,\n",
      "  \"extra\" REAL,\n",
      "  \"mta_tax\" REAL,\n",
      "  \"tip_amount\" REAL,\n",
      "  \"tolls_amount\" REAL,\n",
      "  \"ehail_fee\" REAL,\n",
      "  \"improvement_surcharge\" REAL,\n",
      "  \"total_amount\" REAL,\n",
      "  \"payment_type\" INTEGER,\n",
      "  \"trip_type\" INTEGER,\n",
      "  \"congestion_surcharge\" REAL\n",
      ")\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, 'green_taxi_data'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6b7cf6e8-ce4e-4a0c-bb80-cf694befb311",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: sqlalchemy in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (2.0.15)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from sqlalchemy) (4.5.0)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from sqlalchemy) (2.0.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install sqlalchemy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0b249d3d-6aa1-4374-bbc6-02c9313a7bc5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting psycopg2\n",
      "  Downloading psycopg2-2.9.9-cp311-cp311-win_amd64.whl.metadata (4.5 kB)\n",
      "Downloading psycopg2-2.9.9-cp311-cp311-win_amd64.whl (1.2 MB)\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   -- ------------------------------------- 0.1/1.2 MB 1.7 MB/s eta 0:00:01\n",
      "   ----- ---------------------------------- 0.2/1.2 MB 2.4 MB/s eta 0:00:01\n",
      "   ---------- ----------------------------- 0.3/1.2 MB 2.5 MB/s eta 0:00:01\n",
      "   ------------- -------------------------- 0.4/1.2 MB 2.3 MB/s eta 0:00:01\n",
      "   ------------------- -------------------- 0.6/1.2 MB 2.8 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 0.7/1.2 MB 2.7 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 0.9/1.2 MB 2.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------  1.2/1.2 MB 3.3 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.2/1.2 MB 3.1 MB/s eta 0:00:00\n",
      "Installing collected packages: psycopg2\n",
      "Successfully installed psycopg2-2.9.9\n"
     ]
    }
   ],
   "source": [
    "!pip install psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "ba38165b-55a1-43ea-ade0-f0a789cb338e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlalchemy.engine.base.Connection at 0x1e71932ab50>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sqlalchemy import create_engine\n",
    "\n",
    "engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')\n",
    "\n",
    "engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "00905414-f945-4950-b6be-9cdbabd3a49a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "CREATE TABLE green_taxi_data (\n",
      "\t\"VendorID\" BIGINT, \n",
      "\tlpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\tlpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\tstore_and_fwd_flag TEXT, \n",
      "\t\"RatecodeID\" BIGINT, \n",
      "\t\"PULocationID\" BIGINT, \n",
      "\t\"DOLocationID\" BIGINT, \n",
      "\tpassenger_count BIGINT, \n",
      "\ttrip_distance FLOAT(53), \n",
      "\tfare_amount FLOAT(53), \n",
      "\textra FLOAT(53), \n",
      "\tmta_tax FLOAT(53), \n",
      "\ttip_amount FLOAT(53), \n",
      "\ttolls_amount FLOAT(53), \n",
      "\tehail_fee FLOAT(53), \n",
      "\timprovement_surcharge FLOAT(53), \n",
      "\ttotal_amount FLOAT(53), \n",
      "\tpayment_type BIGINT, \n",
      "\ttrip_type BIGINT, \n",
      "\tcongestion_surcharge FLOAT(53)\n",
      ")\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, name=\"green_taxi_data\", con=engine))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9ef7acca-df8a-40d3-a721-6cb3b8dc24e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_iter = pd.read_csv(url, iterator = True, chunksize = 100000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "44b3063c-2062-4f01-b3e8-36324f561d83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.io.parsers.readers.TextFileReader at 0x1e71911fe50>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_iter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "fdf264bb-46aa-4e0c-899f-e6161e2d5852",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = next(df_iter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "699c2022-45e6-460f-81a1-785e632a4f4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100000"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "291d0802-0759-48ce-876e-2ea84448fffb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>VendorID</th>\n",
       "      <th>lpep_pickup_datetime</th>\n",
       "      <th>lpep_dropoff_datetime</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>RatecodeID</th>\n",
       "      <th>PULocationID</th>\n",
       "      <th>DOLocationID</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>trip_distance</th>\n",
       "      <th>fare_amount</th>\n",
       "      <th>extra</th>\n",
       "      <th>mta_tax</th>\n",
       "      <th>tip_amount</th>\n",
       "      <th>tolls_amount</th>\n",
       "      <th>ehail_fee</th>\n",
       "      <th>improvement_surcharge</th>\n",
       "      <th>total_amount</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>trip_type</th>\n",
       "      <th>congestion_surcharge</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [VendorID, lpep_pickup_datetime, lpep_dropoff_datetime, store_and_fwd_flag, RatecodeID, PULocationID, DOLocationID, passenger_count, trip_distance, fare_amount, extra, mta_tax, tip_amount, tolls_amount, ehail_fee, improvement_surcharge, total_amount, payment_type, trip_type, congestion_surcharge]\n",
       "Index: []"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(n=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b21e8bfe-cad2-40f8-a710-bff89abc2a58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(n=0).to_sql(name = 'green_taxi_data', con = engine, if_exists='replace')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b53057c7-364d-4468-8fef-5a534c21b3a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inserted a new chunk. time taken(ins s) - 24.01\n",
      "Inserted a new chunk. time taken(ins s) - 23.75\n",
      "Inserted a new chunk. time taken(ins s) - 18.4\n",
      "Inserted a new chunk. time taken(ins s) - 19.13\n",
      "Inserted a new chunk. time taken(ins s) - 18.93\n",
      "Inserted a new chunk. time taken(ins s) - 6.24\n"
     ]
    }
   ],
   "source": [
    "# Loading in the data iteratively using a for loop.\n",
    "\n",
    "from time import time\n",
    "\n",
    "for df in df_iter:\n",
    "    t_start = time()\n",
    "\n",
    "    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)\n",
    "    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)\n",
    "\n",
    "    df.to_sql(name = 'green_taxi_data', con = engine, if_exists='append')\n",
    "\n",
    "    t_end = time()\n",
    "\n",
    "    print(f'Inserted a new chunk. time taken(ins s) - {round(t_end - t_start, 2)}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6de6555-7fd3-498f-b0d2-c8e3efb61b7c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
