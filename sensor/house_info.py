#Create a class called HouseInfo. 
#Next, create a HouseInfo class constructor with 
#two parameters, self and data.

# 3 Filter Data Records by Area
#On a new line in the get_data_by_area method, 
#create a for loop to iterate over self.data. 
#Use record as your iterator variable.
#Note: The self.data class variable is a list 
#of dictionaries. The dictionary keys are equal 
#to the columns names in the data files. e.g. 
#when the field input parameter is set to "id" then, 
#the record[field] value corresponds to the "id" column 
#values. In this method, the rec_area variable maps to 
#'area' column values.
#In the body of the for loop, 
#select records according to the following structures:
#Create an if statement that is true when rec_area 
#is equal to 0 In the body of the if, append to the 
#record[field] values to the field_data list.
#Create an else if statement that is true when
# rec_area is equal to record['area'] value.
# In order to compare the rec_area integer object
# to the record['area'] string object, 
#the later needs to be converted to an integer 
#using the int() constructor.
#In the body of the elif, append to the record[field] 
#values to the field_data list.
#Finally, your method should return field_data
# (outside of the for loop, and the very end of the method).
 
from datetime import date

class HouseInfo():
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

# 4  Create Method to Select Data by Date
#Still in the HouseInfo class, create another method 
#called get_data_by_date() with three parameters, self, field,
#  and rec_date. The rec_date parameter should 
# have the current date as its default value.
#You can get the current date using the date module. 
# At the top of the file, import date and datetime
#  from the datetime module. See date information 
# and datetime information.
#In the body of the get_data_by_date() method, 
# create a variable called field_data and set it to
#  an empty list.
    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []

        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data
    
    