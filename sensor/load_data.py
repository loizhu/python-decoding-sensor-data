# At the top of the file, create three import statements
# for os, glob, and csv.
# These libraries will allow us to work with a collection of files.

import os
import glob
import csv

def load_sensor_data():
    sensor_data=[]

    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

#Create one for loop that loops through sensor_files
#  using sensor_file as the iterator variable.

# In the with body, set a variable called data_reader 
# equal to csv.DictReader(). 
# Pass in the current data_file as the first argument, 
# and set the delimiter=',' as the second argument.
#  The data_reader will contain a list of 
# dictionaries with the sensor data.
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file: 
            data_reader = csv.DictReader(data_file, delimiter=',')
        
            #Inside the body of the second for loop, append each 
            # row record to the sensor_data list (you created this list earlier in the Create a Function to Parse the Data task).
            for row in data_reader:
                sensor_data.append(row)

#Finally, your function should return sensor_data
#  (outside of all for loops, and the very end of the function).
    return sensor_data        

