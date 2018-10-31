# Data Analysis
# samples.py
# Created by Mauro J. Pappaterra on 29 of October 2018.
import time
import sys
from random import *

# example executions:
# > python samples.py "" 10000 C
# > python samples.py "Desktop/samples/" 1000000 W

# Ask user how many samples to create and path to save file
if (len(sys.argv) <= 3):
    path = input("\nEnter path to save .csv file: ")
    size = input("\nEnter no. of samples to create: ")
    mode = input("\nEnter 'C' for crime with missing weapon\nEnter 'W' for weapon with missing crime\n")
else:
    path = sys.argv[1]
    size = sys.argv[2]
    mode = sys.argv[3]

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

def get_crime ():
    crime = {'1':'331,Theft From Motor Vehicle - Grand ($400 And Over)', '2':'442,Shoplifting - Petty Theft ($950 & Under)', '3':'210,Robbery',
            '4':'251,Shots Fired At Inhabited Dwelling','5':'740,Vandalism - Felony ($400 & Over; All Church Vandalisms)',
            '6':'440,Theft Plain - Petty ($950 & Under)','7':'237,Child Neglect (See 300 W.i.c.)',
            '8':'626,Intimate Partner - Simple Assault','9':'230,Assault With Deadly Weapon; Aggravated Assault',
            '10':'901,Violation Of Restraining Order','11':'649,Document Forgery / Stolen Felony',
            '12':'341,Theft-grand ($950.01 & Over)','13':'330,Burglary From Vehicle',
            '14':'310,Burglary','15':'956,Letters; Lewd','16':'745,Vandalism - Misdeameanor ($399 Or Under)',
            '17':'510,Vehicle - Stolen','18':'900,Violation Of Court Order','19':'930,Criminal Threats - No Weapon Displayed',
            '20':'753,Discharge Firearms/shots Fired','21':'220,Attempted Robbery','22':'320,Burglary; Attempted',
            '23':'110,Criminal Homicide','24':'888,Trespassing','25':'122,Rape; Attempted','26':'623,Battery Police (Simple)',
            '27':'121,Rape; Forcible','28':'420,Theft From Motor Vehicle - Petty ($950 & Under)','29':'946,Other Miscellaneous Crime',
            '30':'860,Battery With Sexual Contact','31':'520,Vehicle - Attempt Stolen','32':'951,Defrauding Innkeeper/theft Of Services; $400 & Under',
            '33':'910,Kidnapping','34':'933,Prowler','35':'350,Theft; Person','36':'813,Child Annoying (17yrs & Under)','37':'438,Reckless Driving',
            '38':'410,Burglary From Vehicle; Attempted','39':'437,Resisting Arrest','40':'660,Counterfeit','41':'928,Threatening Phone Calls/letters',
            '42':'625,Other Assault','43':'648,Arson','44':'343,Shoplifting-grand Theft ($950.01 & Over','45':'433,Driving Without Owner Consent (Dwoc)',
            '46':'761,Brandish Weapon','47':'886,Disturbing The Peace','48':'351,Purse Snatching','49':'354,Theft Of Identity',
            '50':'627,Child Abuse (Physical) - Simple Assault','51':'666,Bunco; Attempt','52':'474,Theft; Coin Machine - Petty ($950 & Under)',
            '53':'820,Oral Copulation','54':'755,Bomb Scare','55':'662,Bunco; Grand Theft','56':'421,Theft From Motor Vehicle - Attempt',
            '57':'821,Sodomy/sexual Contact B/w Penis Of One Pers To Anus Oth','58':'850,Indecent Exposure','59':'347,Grand Theft / Insurance Fraud',
            '60':'932,Peeping Tom','61':'439,False Police Report','62':'664,Bunco; Petty Theft','63':'441,Theft Plain - Attempt',
            '64':'235,Child Abuse (Physical) - Aggravated Assault','65':'943,Cruelty To Animals','66':'436,Lynching - Attempted',
            '67':'950,Defrauding Innkeeper/theft Of Services; Over $400','68':'668,Embezzlement; Grand Theft ($950.01 & Over)','69':'810,Sex; Unlawful',
            '70':'471,Till Tap - Petty ($950 & Under)','71':'763,Stalking','72':'487,Boat - Stolen',
            '73':'812,Crm Agnst Chld (13 Or Under) (14-15 & Susp 10 Yrs Older)','74':'236,Intimate Partner - Aggravated Assault',
            '75':'434,False Imprisonment','76':'231,Assault With Deadly Weapon On Police Officer','77':'815,Sexual Pentration With A Foreign Object',
            '78':'670,Embezzlement; Petty Theft ($950 & Under)','79':'661,Unauthorized Computer Access','80':'949,Illegal Dumping',
            '81':'622,Battery On A Firefighter','82':'443,Shoplifting - Attempt','83':'345,Dishonest Employee - Grand Theft','84':'480,Bike - Stolen',
            '85':'762,Lewd Conduct','86':'805,Pimping','87':'647,Throwing Object At Moving Vehicle','88':'920,Kidnapping - Grand Attempt',
            '89':'922,Child Stealing','90':'870,Child Abandonment','91':'654,Credit Cards; Fraud Use ($950 & Under','92':'475,Theft; Coin Machine - Attempt',
            '93':'940,Extortion','94':'450,Theft From Person - Attempt','95':'954,Contributing','96':'653,Credit Cards; Fraud Use ($950.01 & Over)',
            '97':'352,Pickpocket','98':'756,Weapons Possession/bombing','99':'473,Theft; Coin Machine - Grand ($950.01 & Over)',
            '100':'902,Violation Of Temporary Restraining Order','101':'865,Drugs; To A Minor','102':'880,Disrupt School','103':'451,Purse Snatching - Attempt',
            '104':'840,Bestiality; Crime Against Nature Sexual Assault With Animals','105':'806,Pandering','106':'470,Till Tap - Grand Theft ($950.01 & Over)',
            '107':'353,Drunk Roll','108':'890,Failure To Yield','109':'444,Dishonest Employee - Petty Theft','110':'903,Contempt Of Court',
            '111':'250,Shots Fired At Moving Vehicle; Train Or Aircraft','112':'924,Telephone Property - Damage','113':'651,Document Worthless ($200.01 & Over)',
            '114':'944,Conspiracy','115':'452,Pickpocket; Attempt','116':'435,Lynching','117':'815,Sexual Penetration W/foreign Object',
            '118':'810,Sex; Unlawful (Including Mutual Consent); Penetration with Foreign Object','119':'956,Letters; Lewd  -  Telephone Calls; Lewd',
            '120':'942,Bribery','121':'446,Petty Theft - Auto Repair','122':'349,Grand Theft / Auto Repair','123':'113,Manslaughter; Negligent',
            '124':'472,Till Tap - Attempt','125':'652,Document Worthless ($200 & Under)','126':'948,Bigamy','127':'882,Inciting A Riot',
            '128':'453,Drunk Roll - Attempt'}

    return crime[str(randint(1, 128))]

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
    new_sample = get_dr_number(sample_index) + "," + get_date() + "," + get_time() + "," + get_area() + ","

    if (mode == 'C'):
        new_sample += get_crime() + ",,,"
    else:
        new_sample += ",," + get_weapon() + ","

    new_sample += get_age() + "," + get_gender() + "," + get_race() +","

    file_content += new_sample + "\n"

    print("=> " + new_sample)

    sample_index += 1

name = ""

if (mode == 'C'):
    name = "samples_C"
else:
    name = "samples_W"

# Save to disk
with open (path + name + ".csv", 'w') as file:
    file.write (file_content)

# Print in Console
print ("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\nData Sampling Completed in " + str(round((time.clock() - start),2)) + " seconds!")

if (mode == 'C'):
    print("\nSample Mode: With crime codes missing weapon code")
else:
    print("\nSample Mode: With weapon codes missing crime code")


print("Total Samples created: " + str(size))