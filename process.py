# Data Pre-processing
# process.py
# Created by Mauro J. Pappaterra on 19 of October 2018.
import codecs
import time
import sys

# example executions:
# > python process.py "" F
# > python process.py "" X
# > python process.py "Desktop/samples/" X

# Ask user to enter path to external file
if (len(sys.argv) < 3):
    path = input("\nEnter path to 'LAPD Normalized Dataset.csv':")
    filter = input("\nType F for filtering else N:")
else:
    path = sys.argv[1]
    filter = sys.argv[2]

if (path!= ""):
    print ("\nUsing path: " + path)

counter_in = 0
counter_out = 0

start = time.clock() # start clock
filter = not(filter == "F") # False for filter, True for unfiltered
file_content = ""

def get_time_label(time):
    if (len(time) == 3):
        time = '0' + time
    elif (len(time) == 2):
        time += '00'
    elif (len(time) == 1):
        time = '0' + time + '00'

    return time[:2]

def get_gender_label(gender):
    if (gender == "M"):
        return "Male"
    elif (gender == "F"):
        return "Female"
    else:
        return "Other"

def get_race_label(race):
    race = race.replace("\r","").replace("\n","")

    if (race == "W"):
        return "Caucasian"
    elif (race == "B"):
        return "African American"
    elif (race == "H"):
        return "Hispanic/Latino"
    else:
        return "Other"

def get_date_label(date):
    months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
              '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    return months[date[:2].replace("0", "").replace("/", "")]

def check_missing(entry_data):
    return not(entry_data[0] == "" or entry_data[1] == "" or entry_data[2] == "" or entry_data[3] == "" or
            entry_data[5]  == "" or entry_data[7] == "" or entry_data[9] == "" or entry_data[11] == "" or
            entry_data[12] == "" or entry_data[13] == "")

with codecs.open(path + "LAPD Modified Dataset.csv", 'r', encoding='utf8') as myFile:
    labels = myFile.readline().replace("\r","").replace("\n","").split(',') # first line

    file_content = labels[0] + "," + labels[1] + "," + labels[2] + "," + labels[3] + "," +\
    labels[5] + "," + labels[7] + "," + labels[9] + "," + labels[11] + "," + labels[12] +\
    "," + labels[13]

    print(file_content)

    data = myFile.readlines()  # saves each line of the text into a list

    for entry in data:

        print("\n>INPUT => " + entry)

        entry_data = entry.split(',')

        if (filter or check_missing(entry_data)):

            output = "\n" + entry_data[0] + "," + get_date_label(entry_data[1]) + "," + get_time_label(entry_data[2]) + "," + entry_data[3] + "," \
                     + entry_data[5] + "," + entry_data[7] + "," + entry_data[9] + "," + entry_data[11] + "," + get_gender_label(entry_data[12]) + "," \
                     + get_race_label(entry_data[13])

            file_content += output

            print("<OUTPUT => " + output[1:])
            counter_in += 1
        else:
            print("<OUTPUT => Entry filtered out due to missing information!")
            counter_out += 1

# Save to disk
with open (path + "output.csv", 'w') as file:
    file.write (file_content)

# Print in Console
print ("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\nData Processing Completed in " + str(round((time.clock() - start),2)) + " seconds!")
print ("\nTotal entries read: " + str(counter_in + counter_out))
if (not filter):
    print("\n-------------------------\nTotal entries added -> " + str(counter_in))
    print ("Total entries filtered out -> " + str(counter_out))