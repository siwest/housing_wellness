This is Python script that works with 2015 U.S. Census CSV data and recent Zillow data dump on median home prices. The purpose of this project is to understand the relationship between median income and median home sales in US counties and cities. It's difficult to determine where in this country your family's dollar goes the furthest, and this project attempts answer that.

To that end, we use Zillow's home value index  to derive a Wellness Index for each city and state. 

Wellness Index = Zillow Home Value Index / median income


The output like this:

[('UT_Utah', 4.094598243356999), ('HI_Hawaii', 4.640409319123904), ('NV_Carson City', 5.61948314367755), ('DC_District of Columbia', 7.6441222731313685), ('NY_New York', 20.94564591727654)]


A High Wellness index value indicates the relative expense to live in a region.

Other factors / API calls to add later may include:

* Walk score
