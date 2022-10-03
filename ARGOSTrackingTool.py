#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Eliza Carter (eliza.carter@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

## Task 2
# Copy and paste a line of data as the lineString variable value
lineString ="20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude

# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#%%

## Task 3
#Create a variable pointing to the data file
file_name = "./data/raw/sara.txt"

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[101]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#%%

## Task 8
#Create a variable pointing to the data file
file_name = "./data/raw/sara.txt"

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

date_dict = {}
location_dict = {}

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

#Pretend we read one line of data from the file
for lineString in line_list:
    
    #Check to see if the lineString is a data line
    if lineString[0] in ('#','u'):
        continue
    
    #Split the string into a list of data items
    lineData = lineString.split()
        
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    if obs_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
        
#Create an empty key list
matching_keys = []
    
# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)

# Report whether no keys were found
if len(matching_keys) == 0:
    print(f"Sara was not located on {user_date}")
else:
    
#Reveal locations for each key in matching_keys
    for matching_key in matching_keys:
        obs_lat, obs_lon = location_dict[matching_key]
        print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")


    
    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    
    
   