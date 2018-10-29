# Data Analysis
# samples.py
# Created by Mauro J. Pappaterra on 29 of October 2018.
import time
import sys
from random import *

# Ask user how many samples to create and path to save file
if (len(sys.argv) == 1):
    size = input("\nEnter no. of samples to create:")
    path = input("\nEnter path to save .csv file:")
else:
    path = sys.argv[1]
    size = sys.argv[2]

if (size!= ""):
    print ("\nCreating " + size + " samples...\n")

size = int (size)

def get_dr_number(index):
    return "S" + str(index + 100000000)[1:]

def get_date ():
    months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
              '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    return months[str(randint(1, 12))]

def get_time ():
    time = ["Night", "Morning", "Afternoon", "Evening", "Night"]
    return time[randint(0, 4)]

def get_area ():
    area = {'1': 'Central', '2': 'Rampart', '3': 'Southwest', '4': 'Hollenbeck', '5': 'Harbor', '6': 'Hollywood', '7': 'Wilshire',
            '8': 'West LA', '9': 'Van Nuys', '10': 'West Valley', '11': 'Northeast', '12': '77th Street', '13': 'Newton',
            '14':'Pacific','15':'N Hollywood','16':'Foothill','17':'Devonshire','18':'Southeast','19':'Mission','20':'Olympic','21':'Topanga'}

    index = str(randint(1, 21))
    return index +","+area[index]

def get_weapon ():
    weapons = {'1':'101,Revolver','2':'102,Hand Gun','3':'103,Rifle','4':'104,Shotgun','5':'105,Sawed Off Rifle/shotgun'
                ,'6':'106,Unknown Firearm','7':'107,Other Firearm','8':'108,Automatic Weapon/sub-machine Gun','9':'109,Semi-automatic Pistol'
                ,'10':'110,Semi-automatic Rifle','11':'111,Starter Pistol/revolver','12':'112,Toy Gun','13':'113,Simulated Gun'
                ,'14':'114,Air Pistol/revolver/rifle/bb Gun','15':'115,Assault Weapon/Uzi/AK47/etc','16':'117,Unknown Type Semiautomatic Assault Rifle'
                ,'17':'118,Uzi Semiautomatic Assault Rifle','18':'119,Mac-10 Semiautomatic Assault Weapon','19':'121,Heckler & Koch 91 Semiautomatic Assault Rifle'
                ,'20':'122,Heckler & Koch 93 Semiautomatic Assault Rifle','21':'200,Knife With Blade 6inches Or Less','22':'201,Knife With Blade Over 6 Inches In Length'
                ,'23':'202,Bowie Knife','24':'203,Dirk/dagger','25':'204,Folding Knife','26':'205,Kitchen Knife','27':'206,Switch Blade'
                ,'28':'207,Other Knife','29':'208,Razor','30':'209,Straight Razor','31':'210,Razor Blade','32':'211,Axe'
                ,'33':'212,Bottle','34':'213,Cleaver','35':'214,Ice Pick','36':'215,Machete','37':'216,Scissors','38':'217,Sword'
                ,'39':'218,Other Cutting Instrument','40':'219,Screwdriver','41':'220,Syringe','42':'221,Glass','43':'222,'
                ,'44':'223,Unknown Type Cutting Instrument','45':'300,Blackjack','46':'301,Belt Flailing Instrument/chain','47':'302,Blunt Instrument'
                ,'48':'303,Brass Knuckles','49':'304,Club/bat','50':'305,Fixed Object','51':'306,Rock/thrown Object','52':'307,Vehicle'
                ,'53':'308,Stick','54':'309,Board','55':'400,Strong-arm (Hands; Fist; Feet Or Bodily Force)','56':'500,Unknown Weapon/other Weapon'
                ,'57':'501,Bomb Threat','58':'502,Bow And Arrow','59':'503,Caustic Chemical/poison','60':'504,Demand Note','61':'505,Explosive Device'
                ,'62':'506,Fire','63':'507,Liquor/drugs','64':'508,Martial Arts Weapons','65':'509,Rope/ligature','66':'510,Scalding Liquid','67':'511,Verbal Threat',
                '68':'512,Mace/pepper Spray','69':'513,Stun Gun','70':'514,Tire Iron','71':'515,Physical Presence'}

    return weapons[str(randint(1, 71))]

def get_age ():
    age = ["Child","Adolescent","Young Adult","Adult","Eldery"]
    return age[randint(0, 4)]

def get_gender ():
    age = ["Male","Female","Other"]
    return age[randint(0, 2)]

def get_race ():
    race = ["Caucasian","African American","Asian","Native American","Pacific Islander","Hispanic/Latino","Other"]
    return race[randint(0, 6)]

header = "DR Number," \
         "Date Occurred," \
         "Time Occurred," \
         "Area ID," \
         "Area Name," \
         "Crime Code," \
         "Crime Code Description," \
         "Weapon Used Code," \
         "Weapon Description," \
         "Victim Age," \
         "Victim Sex," \
         "Victim Descent"

file_content = header + "\n"
sample_index = 1

start = time.clock() # start clock

while (sample_index <= size):
    new_sample = get_dr_number(sample_index) + "," + get_date() + "," + get_time() + "," + get_area() + ",,," + get_weapon() + "," +get_age() + "," +get_gender() + "," +get_race()
    print("=> " + new_sample)

    file_content += new_sample + "\n"

    sample_index += 1

# Save to disk
with open (path + "samples.csv", 'w') as file:
    file.write (file_content)

# Print in Console
print ("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\nData Sampling Completed in " + str(round((time.clock() - start),2)) + " seconds!")
print ("\nTotal Samples created: " + str (size))