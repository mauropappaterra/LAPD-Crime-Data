# Data Pre-processing
# process.py
# Created by Mauro J. Pappaterra on 19 of October 2018.
import codecs
import time
import sys

# Ask user to enter path to external file
if (len(sys.argv) == 1):
    path = input("\nEnter path to 'LAPD Normalized Dataset.csv':")
else:
    path = sys.argv[1]

if (path!= ""):
    print ("\nUsing path: " + path)

counter_in = 0
counter_out = 0

start = time.clock() # start clock
file_content = ""

def get_time_label(time):
    if (len(time) == 3):
        time = '0' + time
    elif (len(time) == 2):
        time += '00'
    elif (len(time) == 1):
        time = '0' + time + '00'

    return time


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
    elif (race == "A" or race == "C" or race == "J" or race == "K" or race == "L"
          or race == "V" or race == "Z" or race == "F" or race == "D"):
        return "Asian"
    elif (race == "I"):
        return "Native American"
    elif (race == "G" or race == "P" or race == "S" or race == "U"):
        return "Pacific Islander"
    elif (race == "H"):
        return "Hispanic/Latino"
    else:
        return "Other"

with codecs.open(path + "LAPD Modified Dataset.csv", 'r', encoding='utf8') as myFile:
    file_content = myFile.readline().replace("\r","").replace("\n","") # first line

    labels = file_content.split(',')
    print(labels)

    data = myFile.readlines()  # saves each line of the text into a list

    for entry in data:

        print("\n>INPUT => " + entry)

        entry_data = entry.split(',')


        output = "\n" + entry_data[0] + "," + entry_data[1] + "," + get_time_label(entry_data[2]) + "," + entry_data[3] + "," \
                 + entry_data[5] + "," + entry_data[7] + "," + entry_data[9] + "," + entry_data[11] + "," + get_gender_label(entry_data[12]) + "," \
                 + get_race_label(entry_data[13])

        file_content += output

        print("<OUTPUT => " + output[1:])
        counter_in += 1

# Save to disk
with open (path + "output.csv", 'w') as file:
    file.write (file_content)

# Print in Console
print ("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\nData Processing Completed in " + str(round((time.clock() - start),2)) + " seconds!")
print ("\nTotal entries read: " + str(counter_in + counter_out) + "\n-------------------------")
print ("Total entries added -> " + str(counter_in))
print ("Total entries filtered out -> " + str(counter_out))