import csv

"""
Project by: Sarah West

Overview: This is a basic attempt to understand the relationship between median
income and median home sales. I am simply comparing Census and Zillow public
data sets. These data are available to download here:
http://files.zillowstatic.com/research/public/County/County_Zhvi_Summary_AllHomes.csv
https://www.census.gov/did/www/saipe/downloads/estmod15/index.html

"""

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
        income_dict[state + '_' + county] = median_income

home_dict = {}
with open('County_Zhvi_Summary_AllHomes.csv', 'r') as csvfile:
    zhvi_reader = csv.DictReader(csvfile)
    for row in zhvi_reader:
        state = row['State']
        county = row['RegionName']
        zhvi = float(row['Zhvi'].replace(",", ""))
        home_dict[state + '_' + county] = zhvi

rank_list = []
for k, v in income_dict.items():
    if k in home_dict:
        my_wellness_index = home_dict[k] / v
        print (k + ' has ' + str(my_wellness_index))
