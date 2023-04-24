from house_info import HouseInfo
from datetime import date


class HumidityData(HouseInfo):
    def _convert_data(self, data):
        recs = []

#2 Convert Humidity Data
# On a new line in the _convert_data() method, 
# create a for loop to iterate over data. 
# Use rec as your iterator variable.
#In the body of the for convert the rec string values 
# to float and multiply it by 100, then, append them to recs.
        for rec in data:
            # Convert string of integers into actual integers based 10
            recs.append(float(rec) * 100)
        return recs
#3 Filter Humidity Data Records by Area
# Next, you are going to override the get_data_by_area()
#  method from the parent class.
# Here, you are going to repeat the process you followed
#  for the TemperatureClass. Create a method called 
# get_data_by_area() with two parameters, self and rec_area. 
# The rec_area parameter should have a default value of 0,
#  which translates to all records. 
# The purpose of this method is to filter the humidity 
# data by the "area" field. In this method, 
# rec_area maps to the "area" data column.
# This method should be almost identical to the one 
# you created for the TemperatureData class, 
# with the exception of the field argument. 
# This time, use "humidity" as the filter value.
# The method should look like this:   
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("humidity", rec_area)
        return self._convert_data(recs)


    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("humidity", rec_date)
        return self._convert_data(recs)
