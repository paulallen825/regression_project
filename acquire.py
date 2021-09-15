import pandas as pd
import numpy as np
import os

#acquire
from env import host, user, password
from pydataset import data


# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")


# get helper function to get the necessary connction to url.

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to create a connection urs to access database info.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

# Use the above helper function and a sql query in a single function.
def new_zillow_data():
    '''
    This function reads data from the Codeup db into a df.
    '''
    zillow_sql = '''SELECT parcelid, bathroomcnt, bedroomcnt,
                 calculatedfinishedsquarefeet, fips, yearbuilt, taxvaluedollarcnt,
                 taxamount, propertylandusetypeid 
                 FROM predictions_2017 
                 JOIN properties_2017 using (parcelid) 
                 WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08 
                 AND propertylandusetypeid BETWEEN 260 and 264'''
    
    
    return pd.read_sql(zillow_sql, get_connection('zillow'))



def get_zillow_data():
    '''
    This function reads in zillow data from Codeup database and writes data to
    a csv file if, returns df.
    '''
    if os.path.isfile('zillow_df.csv'):
        # If csv file exists, read in data from csv.
        df = pd.read_csv('zillow_df.csv', index_col=0)
        
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_zillow_data()
        # Write DataFrame to a csv file.
        df.to_csv('zillow_df.csv')
    return df
