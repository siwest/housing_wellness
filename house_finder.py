import csv
import requests

from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails

"""
Project by: Sarah West

Overview: This is a basic attempt to understand the relationship between median
income and median home sales.

"""

def set_mpl_options():
   mpl.rcParams['legend.fancybox'] = True
   mpl.rcParams['legend.shadow'] = True
   mpl.rcParams['legend.framealpha'] = 0.7

import matplotlib.cbook as cbook
import pandas as pd
import matplotlib.pyplot as plt
from dautil import options
import matplotlib as mpl
from dautil import plotting
import seaborn as sns

data = cbook.get_sample_data('est15ALL.csv', asfileobj=True)
df = pd.read_csv(data, parse_dates=True, index_col=0)

wsid_secret = ""

income_dict = {}
with open('est15ALL.csv', 'r') as csvfile:
    income_reader = csv.DictReader(csvfile)
    for row in income_reader:
        state = row['Postal Code']
        county = row['Name']
        try:
            median_income = float(row['Median Household Income']
                                  .replace(",", ""))
        except ValueError:  # Some period found in original data
            median_income = 0
        income_dict[state] = median_income

home_dict = {}
with open('County_Zhvi_Summary_AllHomes.csv', 'r') as csvfile:
    zhvi_reader = csv.DictReader(csvfile)
    for row in zhvi_reader:
        state = row['State']
        county = row['RegionName']
        region_id = row['RegionID']
        zhvi = float(row['Zhvi'].replace(",", ""))
        #url = 'http://www.zillow.com/webservice/GetRegionChildren.htm'
        #query = {'zws-id': wsid_secret, 'regionId': region_id,
        #         'childtype': 'county'}
        #r = requests.get(url, params=query)
        #print(r.json())

        home_dict[state] = zhvi

match_list = []
for k, v in income_dict.items():
    if k in home_dict:
        my_wellness_index = home_dict[k] / v
        match_list.append((k, my_wellness_index))

# Apply feature scaling
my_sum = 0
my_min = 0
my_max = 0

for elem in match_list:
    my_sum += elem[1]
    my_min = min(my_min, elem)
    my_max = max(max, elem)


for state, i in match_list.items():
  i = (mean - i)**2 / range

print(sorted(match_list, key=lambda x: x[1]))