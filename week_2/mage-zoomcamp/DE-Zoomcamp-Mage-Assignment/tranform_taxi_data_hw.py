import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(result_df, *args, **kwargs):
    print("Rows with 0 passanger: ", result_df['passenger_count'].isin([0]).sum() )


    #Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero
    df_new = result_df[(result_df['passenger_count'] != 0) & (result_df['trip_distance'] != 0)]


    #Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    df_new['lpep_pickup_date'] = df_new['lpep_pickup_datetime'].dt.date

    #Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    df_new.rename(columns={'VendorID' : 'vendor_id'}, inplace=True)


    return df_new 




@test
def test_output(output, *args) -> None:

    #Assertions
    
    assert set(output['vendor_id'].unique()) == {1, 2}, "Error: 'vendor_id' contains values other than 1 and 2"
    assert (output['passenger_count'] > 0).all() , 'passenger_count is greater than 0'
    assert (output['trip_distance'] > 0).all() , 'trip_distance is greater than 0'

