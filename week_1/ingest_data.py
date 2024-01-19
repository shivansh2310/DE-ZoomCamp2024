#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"


# In[5]:


df = pd.read_csv(url, nrows = 100)


# In[6]:


len(df)


# In[7]:


df.head()


# In[8]:


taxi_zone = pd.read_csv("https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv")


# In[9]:


len(taxi_zone)


# In[10]:


taxi_zone.head()


# In[11]:


print(pd.io.sql.get_schema(df, 'green_taxi_data'))


# In[12]:


df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


# In[13]:


print(pd.io.sql.get_schema(df, 'green_taxi_data'))


# In[14]:


get_ipython().system('pip install sqlalchemy')


# In[16]:


get_ipython().system('pip install psycopg2')


# In[17]:


from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

engine.connect()


# In[18]:


print(pd.io.sql.get_schema(df, name="green_taxi_data", con=engine))


# In[19]:


df_iter = pd.read_csv(url, iterator = True, chunksize = 100000)


# In[20]:


df_iter


# In[21]:


df = next(df_iter)


# In[22]:


len(df)


# In[23]:


df.head(n=0)


# In[24]:


df.head(n=0).to_sql(name = 'green_taxi_data', con = engine, if_exists='replace')


# In[25]:


# Loading in the data iteratively using a for loop.

from time import time

for df in df_iter:
    t_start = time()

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    df.to_sql(name = 'green_taxi_data', con = engine, if_exists='append')

    t_end = time()

    print(f'Inserted a new chunk. time taken(ins s) - {round(t_end - t_start, 2)}')


# In[27]:


get_ipython().system('jupyter nbconvert --to script ingest_data.py')


# In[ ]:




