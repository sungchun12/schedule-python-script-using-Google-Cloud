#this script appends live Chicago traffic data into BigQuery, there will be duplicates
#but that's accounted for with a saved view removing duplicates using SQL

from __future__ import print_function, absolute_import #package to smooth over python 2 and 3 differences
import pandas as pd #package for dataframes
from sodapy import Socrata #package for open source api
from google.datalab import Context #package for datalab
import time
from datetime import datetime, timedelta
import logging #package for error logging

#tracks error messaging
logging.basicConfig(level=logging.INFO)

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("data.cityofchicago.org", None)

#indent the run function by 1 tab
def run():
# Example authenticated client (needed for non-public datasets):
	client = Socrata("data.cityofchicago.org", None)
	                 
	# First 2000 results, returned as JSON from API / converted to Python list of
	# dictionaries by sodapy.
	results = client.get("8v9j-bter", limit=2000)
	
	# Convert to pandas DataFrame
	results_df = pd.DataFrame.from_records(results)
	
	
	#have this go directly into bigquery syntax-https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_gbq.html
	results_df.to_gbq('chicago_traffic.demo_data', "demos-sung", chunksize=2000, verbose=True, if_exists='append')
