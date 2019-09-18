#######################################################################################################
# Python program to create long biographies from the provided .csv file                               #
# Code adapted from Jia Zhang                                                                         #
# Written by Zainab Alasadi                                                                           #
# Saturday 14th September 2019                                                                        #
#######################################################################################################

import csv    
import random
import numpy as np
from random import shuffle

VISCURCF = 122

def clearInts(row, indexStart, indexEnd):
    if indexStart == indexEnd:
        row[indexStart] = ""
    else:
        for i in range(indexStart, indexEnd):
            row[i] = ""

def randomPop(array, num):
    shuffle(array)
    for i in range(0, len(array)):
        if len(array) >= num:
            array.pop()

def joinStrings(string, array):
    if array is None or len(array) == 0:
        return("")
    elif len(array) == 1:
        return(string + array[0] + ".")
    elif len(array) == 2:
        return(string + array[0] + ' and ' + array[1] + ".")
    return(string + ', '.join(array[:-1]) + ' and ' + array[-1]  + ".")


def homeReturn(row, index, count):
    home = int([row[index]][0])
    if home == 10:
        if count == 0:
            return("I'm travelling")
        elif count >= 1:
            return("travel")
    elif home == 11:
        if count == 0:
            return("of work")
        elif count >= 1:
            return("work")
    elif home == 12:
        if count == 0:
            return("I'm house sitting")
        elif count >= 1:
            return("house sitting")
    elif home == 14:
        if count == 0:
            return("I recently moved")
        elif count >= 1:
            return("moving homes")
    elif home == 15:
        if count == 0:
            return("I'm renovating")
        elif count >= 1:
            return("renovations")
    elif home == 16:
        if count == 0:
            return("the tight housing market")
        elif count >= 1:
            return("tight housing market")     
    elif home == 17:
        if count == 0:
            return("of domestic violence")
        elif count >= 1:
            return("domestic violence")
    elif home == 18:
        if count == 0:
            return("of alcohol & drugs")
        elif count >= 1:
            return("alcohol & drugs")
    elif home == 19:
        if count == 0:
            return("of family problems")
        elif count >= 1:
            return("family problems")    
    elif home == 20:
        if count == 0:
            return("of financial problems")
        elif count >= 1:
            return("financial problems")
    elif home == 21:
        if count == 0:
            return("of mental illness")
        elif count >= 1:
            return("mental illness")
    elif home == 22:
        if count == 0:
            return("I lost my job")
        elif count >= 1:
            return("unemployment")
    elif home == 23:
        if count == 0:
            return("of gambling")
        elif count >= 1:
            return("gambling")
    elif home == 24:
        if count == 0:
            return("of eviction")
        elif count >= 1:
            return("eviction")
    elif home == 25:
        if count == 0:
            return("of natural disaster")
        elif count >= 1:
            return("natural disaster")
    else:
        return("")

# Reasons for ever being without a permanent place to live - ALLHOM
def withoutHome(row, index):
    homeless = int([row[index]][0])
    if homeless == 98:
        row[index] = "I've never been homeless."
    else:
        a = []
        count = 0
        # generate an array of problems
        for i in range(1, 17):
            addOn = homeReturn(row, index + i, count)
            if len(addOn) != 0:
                a.append(addOn)
                count = count + 1
        # add problems to base sentence
        if len(a) != 0:
            if len(a) >= 5:
                randomPop(a, 5)
            row[index] = joinStrings("I don't have a permanent place to live because ", a)
        else:
            row[index] = "I don't have a permanent place to live."
    clearInts(row, index + 1, index + 17)

# Victim of physical or threatened violence in last 12 months - ASSAULT
def assault(row, index):
    assault = int([row[index]][0])
    if assault == 1:
        row[index] = "I'm a victim of violence."
    else:
        row[index] = ""

# Perceived level of difficulty with transport - ATRQ01CF
def transportDifficulty(row, index):
    transport = int([row[index]][0])
    if transport == 3:
        row[index] = "I have difficulty travelling."
    elif transport == 4:
        row[index] = "I'm housebound."
    else:
        row[index] = ""    

# Family composition of household - FAMCOMB
def familyComp(row, index):
    family = int([row[index]][0])
    clearInts(row, index, index)
    if family == 1:
        return("my partner and children.")
    elif family == 2:
        return("my children.")
    elif family == 3:
        return("my partner.")
    elif family == 4:
        return("my extended family.")
    elif family == 5:
        return("multiple families.")
    elif family == 6:
        return("alone")
    elif family == 7:
        return("my friends.")

# Number of bedrooms - BEDCURF
def numBedrooms(row, index):
    bedroom = int([row[index]][0])
    family = str(familyComp(row, 43))
    if bedroom == 1:
        if len(family) == 0:
            row[index] = "I live in a 1 bedroom home."
        elif family == "alone":
            row[index] = "I live alone in a 1 bedroom home."
        else:
            row[index] = "I live in a 1 bedroom home with " + family
    elif bedroom == 2:
        if len(family) == 0:
            row[index] = "I live in a 2 bedroom home."
        elif family == "alone":
            row[index] = "I live alone in a 2 bedroom home."
        else:
            row[index] = "I live in a 2 bedroom home with " + family
    elif bedroom == 3:
        if len(family) == 0:
            row[index] = "I live in a 3 bedroom home."
        elif family == "alone":
            row[index] = "I live alone in a 3 bedroom home."
        else:
            row[index] = "I live in a 3 bedroom home with " + family
    elif bedroom == 4:
        if len(family) == 0:
            row[index] = "I live in a 4 bedroom home."
        elif family == "alone":
            row[index] = "I live alone in a 4 bedroom home."
        else:
            row[index] = "I live in a 4 bedroom home with " + family
    elif bedroom == 5:
        if len(family) == 0:
            row[index] = "I live in a 5+ bedroom home."
        elif family == "alone":
            row[index] = "I live alone in a 5+ bedroom home."
        else:
            row[index] = "I live in a 5+ bedroom home with " + family
    else:
        row[index] = ""

def cashReturn(row, index):
    cash = int([row[index]][0])
    if cash == 1:
        return("basic bills")
    elif cash == 2:
        return("my mortage")
    elif cash == 3:
        return("insurance")
    elif cash == 4:
        return("my credit card")
    elif cash == 6:
        return("meals")
    else:
        return("")

# Type(s) of cash flow problem - CASHFLT
def cashProblems(row, index):
    cash = int([row[index]][0])
    if cash == 0 or cash == 11:
        row[index] = ""
    elif cash == 10:
        row[index] = "I've never had money problems."
    else:
        a = []
        # generate an array of problems
        for i in range(1, 11):
            addOn = cashReturn(row, index + i)
            if len(addOn) != 0:
                a.append(addOn)
        # add problems to base sentence
        if len(a) != 0:
            if len(a) >= 5:
                randomPop(a, 5)
            row[index] = joinStrings("I've had difficulty paying for ", a)
        else:
            row[index] = "I've had difficulty paying for my living."
    clearInts(row, index + 1, index + 11)

# Country of birth - COBBC
def birthCountry(row, index):
    birth = int([row[index]][0])
    if birth == 1:
        row[index] = "I was born in Australia."
    elif birth == 3:
        row[index] = "I wasn't born in an English-speaking country."
    else:
        row[index] = ""    

# Whether used a computer at home in last 12 months - COMHOM
def computerUse(row, index):
    computer = int([row[index]][0])
    if computer == 3:
        row[index] = "I don't have a computer at home."
    else:
        row[index] = ""

# Value of consumer debt - COTVALCF
def debtValue(row, index):
    debt = int([row[index]][0])
    if debt == 0:
        row[index] = "I don't have any consumer debt."
    elif debt == 2:
        row[index] = "I have $" + str(random.randint(5000, 9999)) + " in consumer debt."
    elif debt == 3:
        row[index] = "I have $" + str(random.randint(10000, 49999)) + " in consumer debt."
    elif debt == 4:
        row[index] = "I have more than $50K consumer debt."
    else:
        row[index] = ""

def disReturn(row, index):
    dis = int([row[index]][0])
    if dis == 1:
        return("sensory")
    elif dis == 2:
        return("physical")
    elif dis == 3:
        return("intellectual")
    elif dis == 4:
        return("psychological")
    else:
        return("")

# Disability type - DISTYPC
def disabilityType(row, index):
    dis = int([row[index]][0])
    if dis == 0:
        row[index] = ""
    elif dis == 6:
        row[index] = "I don't have any disabilities."
    else:
        a = []
        string = "I have "
        # generate an array of disabilities
        for i in range(1, 5):
            addOn = disReturn(row, index + i)
            if len(addOn) != 0:
                a.append(addOn)
        # add disabilities to base sentence
        if a is None or len(a) == 0:
            sentence = string + "a " + "disability."
        elif len(a) == 1:
            sentence = string + "a " + a[0] + " disability."
        else:
            a[-1] = a[-1] + " disabilities"
            sentence = joinStrings(string, a)
        row[index] = sentence
    clearInts(row, index + 1, index + 5)


# Dwelling structure - DWSTBC
def dwellingType(row, index):
    dwell = int([row[index]][0])
    if dwell == 1:
        row[index] = "I live in a house."
    elif dwell == 3:
        row[index] = "I live in a flat."
    else:
        row[index] = ""

# Main field of highest educational attainment - EDFIECF
def fieldEducation(row, index):
    field = int([row[index]][0])
    clearInts(row, index, index)
    if field == 1:
        return("sciences.")
    elif field == 2:
        return("IT.")
    elif field == 3:
        return("engineering.")
    elif field == 4:
        return("architecture")
    elif field == 5:
        return("environmental studies.")
    elif field == 6:
        return("health.")
    elif field == 7:
        return("education.")
    elif field == 8:
        return("commerce.")
    elif field == 9:
        return("society and culture.")
    elif field == 10:
        return("creative arts.")
    elif field == 11:
        return("hospitality.")
    else:
        return("")

# Main reason did not study although wanted to - MRDSTU
def whyStopStudy(row, index):
    stop = int([row[index]][0])
    clearInts(row, index, index)
    if stop == 17:
        return("I have a disability.")
    elif stop == 18:
        return("I had to care for my family.")
    elif stop == 19:
        return("I had no time.")
    elif stop == 20:
        return("of financial reasons.")
    elif stop == 23:
        return("I lacked basic skills.")
    elif stop == 24:
        return("of discrimination that I experienced.")
    elif stop == 97:
        return("I didn't like school.")
    else:
        return("")

# Highest educational attainment - EDATTBC
def educationHighest(row, index):
    edu = int([row[index]][0])
    field = fieldEducation(row, 41)
    whyStop = whyStopStudy(row, 60)
    if edu == 1:
        if len(field) != 0:
            row[index] = "I have a Postgraduate degree in " + fieldEducation(row, index)
        else: 
            row[index] = "I have a Postgraduate degree."
    elif edu == 2:
        if len(field) != 0:
            row[index] = "I have a Bachelor's degree in " + fieldEducation(row, index)
        else:
            row[index] = "I have a Bachelor's degree."
    elif edu == 3 or edu == 4 or edu == 5 or edu == 6:
        if len(field) != 0:
            row[index] = "I have a certificate in " + fieldEducation(row, index)
        else:
            row[index] = "I have a professional certification."
    elif edu == 7:
        if len(whyStop) == 0:
            row[index] = "I completed up to year 12."
        else:
            row[index] = "I completed up to year 12." + " I didn't finish studying because " + whyStop
    elif edu == 8:
        if len(whyStop) == 0:
            row[index] = "I completed up to year 11."
        else:
            row[index] = "I completed up to year 11." + " I didn't finish studying because " + whyStop
    elif edu == 9:
        if len(whyStop) == 0:
            row[index] = "I completed up to year 10."
        else:
            row[index] = "I completed up to year 10." + " I didn't finish studying because " + whyStop
    elif edu == 10:
        if len(whyStop) == 0:
            row[index] = "I completed up to year 9."
        else:
            row[index] = "I completed up to year 9." + " I didn't finish studying because " + whyStop
    elif edu == 11:
        if len(whyStop) == 0:
            row[index] = "I didn't finish primary school."
        else:
            row[index] = "I didn't finish primary school because " + whyStop
    else:
        row[index] = ""

# Whether ever experienced homelessness - EVRHMLES 
def homelessness(row, index):
    home = int([row[index]][0])
    if home == 1:
        row[index] = ("I've experienced homelessness.")
    else:
        row[index] = ""

# Full-time/part-time study - FPTSTUDY
def studyStatus(row, index):
    study = int([row[index]][0])
    if study == 1:
        row[index] = "I'm a full-time student."
    elif study == 2:
        row[index] = "I'm a part-time student."
    else:
        row[index] = ""

# Full-time/part-time status - FPTSTA
def workStatus(row, index):
    work = int([row[index]][0])
    if work == 1:
        row[index] = "I work full-time."
    elif work == 2:
        row[index] = "I work part-time." 
    elif work == 3 or work == 4:
        row[index] = "I'm currently looking for work."
    else:
        row[index] = ""

# Frequency of voluntary work for organisation - FREQVORG
def volunteer(row, index):
    volunteer = int([row[index]][0])
    if volunteer == 1:
        row[index] = "I volunteer at least once a week."
    elif volunteer == 2:
        row[index] = "I volunteer at least once fortnight." 
    elif volunteer == 3:
        row[index] = "I volunteer at least once every month."
    else:
        row[index] = ""

# Frequency in experiencing difficulty in paying bills - FSRQ03
def billPaying(row, index):
    bill = int([row[index]][0])
    if bill == 1 or bill == 2:
        row[index] = "I have little difficulty paying bills."
    elif bill == 3 or bill == 4:
        row[index] = "I've had some difficulties paying bills this year." 
    elif bill == 5 or bill == 6:
        row[index] = "I've had a lot of difficulties paying bills this year."
    else:
        row[index] = ""

def homelessReturn(row, index):
    home = int([row[index]][0])
    if home == 10:
        return("stayed with relatives")
    elif home == 11:
        return("stayed at a friend's house")
    elif home == 12:
        return("stayed at a caravan park")
    elif home == 13:
        return("stayed at a hostel")
    elif home == 14:
        return("stayed in a night shelter")
    elif home == 15:
        return("stayed in a homeless shelter")
    elif home == 16:
        return("stayed at a refuge")
    elif home == 17:
        return("squatted in an abandoned building")
    elif home == 18:
        return("slept rough")
    else:
        return("")

# All situations ever experienced because did not have a permanent place to live - HOMQ01 
def homelessExperience(row, index):
    home = int([row[index]][0])
    if home == 0 or home == 20 or home == 19:
        row[index] = ""
    else:
        a = []
        # generate an array of problems
        for i in range(1, 10):
            addOn = homelessReturn(row, index + i)
            if len(addOn) != 0:
                a.append(addOn)
        # add problems to base sentence
        if len(a) != 0:
            if len(a) >= 4:
                randomPop(a, 4)
            row[index] = joinStrings("When I was homeless, I ", a)
        else:
            row[index] = ""
    clearInts(row, index + 1, index + 10)

# Hours usually worked in all jobs - HRSWKBC 
def hoursWork(row, index):
    hours = int([row[index]][0])
    if hours == 1:
        row[index] = "I work " + str(random.randint(1, 15)) + " hours a week."
    elif hours == 2:
        row[index] = "I work " + str(random.randint(16, 24)) + " hours a week."
    elif hours == 3:
        row[index] = "I work " + str(random.randint(25, 34)) + " hours a week."
    elif hours == 4:
        row[index] = "I work " + str(random.randint(35, 39)) + " hours a week."
    elif hours == 5:
        row[index] = "I work 40 hours a week."
    elif hours == 6:
        row[index] = "I work " + str(random.randint(41, 49)) + " hours a week."
    elif hours == 7:
        row[index] = "I work 50+ hours a week."
    else:
        row[index] = ""

# Acceptance of different cultures - LEVTOL 
def cultureAccept(row, index):
    culture = int([row[index]][0])
    if culture == 4 or culture == 5:
        row[index] = "I don't accept cultures other than my own."
    elif culture == 1:
        row[index] = "I embrace cultures outside my own."
    else:
        row[index] = ""

# Multiple job holder - MULTIJOB 
def multipleJobs(row, index):
    multWork = int([row[index]][0])
    if multWork == 1:
        row[index] = "I have multiple jobs."
    else:
        row[index] = ""

# Occupation in main job - OCCBC 
def mainOccupation(row, index):
    occup = int([row[index]][0])
    if occup == 1:
        row[index] = "I'm a manager."
    elif occup == 4:
        row[index] = "I'm a social worker."
    elif occup == 5:
        row[index] = "I'm a administrative worker."
    elif occup == 6:
        row[index] = "I'm a salesperson."
    elif occup == 8:
        row[index] = "I'm a labourer."
    else:
        row[index] = ""

# Overall Life Satisfaction - OLSQ01 
def lifeSatisfaction(row, index):
    life = int([row[index]][0])
    if life == 1 or life == 2:
        row[index] = "I'm happy with my life."
    elif life == 3:
        row[index] = "I'm mostly satisfied with my life."
    elif life == 7 or life == 6:
        row[index] = "I hate my life."
    else:
        row[index] = ""

# Frequency of telephone email and mail contact with family or friends - OTHRCON 
def familyContact(row, index):
    contact = int([row[index]][0])
    if contact == 1:
        row[index] = "I contact my family a few times a day."
    elif contact == 2:
        row[index] = "I contact my family everyday."
    elif contact == 3 or contact == 4:
        row[index] = "I contact my family every week."
    elif contact == 5 or contact == 6:
        row[index] = "I contact my family every year."
    elif contact == 7:
        row[index] = "I don't have contact with my family."
    elif contact == 8:
        row[index] = "I don't have any living family."
    else:
        row[index] = ""

# Registered marital status - REGMAR 
def maritalStatus(row, index):
    marry = int([row[index]][0])
    if marry == 1:
        row[index] = "I've never been married."
    elif marry == 2:
        row[index] = "I'm a widow."
    elif marry == 3:
        row[index] = "I'm divorced."
    elif marry == 4:
        row[index] = "I'm separated from my spouse."
    elif marry == 5:
        row[index] = "I'm married."
    else:
        row[index] = ""

# Weekly rent payments - RENTBCF 
def rent(row, index):
    rent = int([row[index]][0])
    if rent == 1:
        row[index] = "I pay less than $60 rent a week."
    elif rent == 2:
        row[index] = "I pay $" + str(random.randint(60, 99)) + " rent a week."
    elif rent == 3:
        row[index] = "I pay $" + str(random.randint(100, 149)) + " rent a week."
    elif rent == 4:
        row[index] = "I pay $" + str(random.randint(150, 199)) + " rent a week."
    elif rent == 5:
        row[index] = "I pay $" + str(random.randint(200, 249)) + " rent a week."
    elif rent == 6:
        row[index] = "I pay $" + str(random.randint(250, 399)) + " rent a week."
    elif rent == 7:
        row[index] = "I pay $" + str(random.randint(300, 349)) + " rent a week."
    elif rent == 8:
        row[index] = "I pay $" + str(random.randint(350, 399)) + " rent a week."
    elif rent == 9:
        row[index] = "I pay $" + str(random.randint(400, 449)) + " rent a week."
    elif rent == 10:
        row[index] = "I pay more than $500 rent a week."
    else:
        row[index] = ""

# Retirement status - RETSTACF 
def retireStatus(row, index):
    retired = int([row[index]][0])
    if retired == 4:
        row[index] = "I'm retired."
    elif retired == 5:
        row[index] = "I've never worked for more than 2 weeks in my life."
    else:
        row[index] = ""

# Feelings of safety at home alone during day - SAFEQ01 
def safeDay(row, index):
    safe = int([row[index]][0])
    if safe == 4 or safe == 5:
        row[index] = "I don't feel safe at home during the day."
    elif safe == 6:
        row[index] = "I'm never home during the day."
    else:
        row[index] = ""

# Feelings of safety at home alone after dark - SAFEQ02 
def safeNight(row, index):
    safe = int([row[index]][0])
    if safe == 4 or safe == 5:
        row[index] = "I don't feel safe at home at night."
    elif safe == 6:
        row[index] = "I'm never home during the night."
    else:
        row[index] = ""

# Feelings of safety walking alone in local area after dark - SAFEQ03 
def safeWalkNight(row, index):
    safe = int([row[index]][0])
    if safe == 4:
        row[index] = "I fear for my safety when walking home at night."
    elif safe == 5:
        row[index] = "I feel very unsafe when walking home at night."
    elif safe == 6:
        row[index] = "I'm never home during the night."
    else:
        row[index] = ""

def serviceReturn(row, index):
    service = int([row[index]][0])
    if service == 12:
        return("disability services")
    elif service == 13:
        return("dental services")
    elif service == 14:
        return("doctors")
    elif service == 16:
        return("hospitals")
    elif service == 15:
        return("employment services")
    elif service == 17:
        return("legal services")
    elif service == 18:
        return("mental health services")
    else:
        return("")

# Services had difficulty accessing - SERDIFF
def serviceAccess(row, index):
    service = int([row[index]][0])
    a = []
    # generate an array of service
    for i in range(1, 11):
        addOn = serviceReturn(row, index + i)
        if len(addOn) != 0:
            a.append(addOn)
    # add service to base sentence
    if len(a) != 0:
        if len(a) >= 4:
            randomPop(a, 4)
        row[index] = joinStrings("I have difficulty accessing ", a)
    else:
        row[index] = "I have difficulty accessing basic services."
    clearInts(row, index + 1, index + 11)

# Whether provided unpaid care help - SOHQ01A
def unpaidCarer(row, index):
    carer = int([row[index]][0])
    if carer == 1:
        row[index] = "I'm an unpaid carer."
    else:
        row[index] = ""

# Delayed medical consultation because could not afford it - SPHQ02
def medicalAfford(row, index):
    med = int([row[index]][0])
    if med == 1:
        row[index] = "I have trouble paying for healthcare."
    else:
        row[index] = ""

# Proficiency in spoken English - SPOKENG
def englishProf(row, index):
    english = int([row[index]][0])
    if english == 3:
        row[index] = "My English is poor."
    elif english == 4:
        row[index] = "I don't speak any English."
    else:
        row[index] = ""

# State or Territory of residence - STATEUR
def stateReside(row, index):
    state = int([row[index]][0])
    if state == 1:
        row[index] = "I live in NSW."
    elif state == 2:
        row[index] = "I live in Victoria."
    elif state == 3:
        row[index] = "I live in Queensland."
    elif state == 4:
        row[index] = "I live in South Australia."
    elif state == 5:
        row[index] = "I live in Western Australia."
    elif state == 6:
        row[index] = "I live in Tasmania."
    elif state == 7:
        row[index] = "I live in Northern Territory."
    elif state == 8:
        row[index] = "I live in Canberra."
    else:
        row[index] = ""

def stressReturn(row, index):
    stress = [row[index]][0]
    if stress == 10:
        return("a recent divorce")
    elif stress == 11:
        return("a recent death")
    elif stress == 12:
        return("an illness")
    elif stress == 13:
        return("a serious accident")
    elif stress == 14:
        return("alcohol and drug")
    elif stress == 15:
        return("mental illness")
    elif stress == 16:
        return("my disability")
    elif stress == 17:
        return("unemployment")
    elif stress == 18:
        return("involuntary redundancy")
    elif stress == 19:
        return("witnessing a violence")
    elif stress == 20:
        return("abuse")
    elif stress == 21:
        return("trouble with the police")
    elif stress == 22:
        return("a gambling problem")
    elif stress == 23:
        return("discrimination")
    else:
        return("")

# Personal stressors experienced in last 12 months - STRESS
def stress(row, index):
    stress = int([row[index]][0])
    if stress == 25:
        row[index] = "I haven't been stressed in the past year."
    else:
        a = []
        # generate an array of stresser
        for i in range(1, 16):
            addOn = stressReturn(row, index + i)
            if len(addOn) != 0:
                a.append(addOn)
        # add stresser to base sentence
        if len(a) != 0:
            if len(a) >= 5:
                randomPop(a, 5)
            row[index] = joinStrings("I have stress from ", a)
        else:
            row[index] = ""
    clearInts(row, index + 1, index + 16)

# Government support in last 2 years - TIMEGVBC
def govSupport(row, index):
    support = int([row[index]][0])
    if support == 4:
        row[index] = "I've been on government support for " + str(random.randint(9, 11)) + " months."
    elif support == 5:
        row[index] = "I've been on government support for " + str(random.randint(12, 17)) + " months."
    elif support == 6:
        row[index] = "I've been on government support for " + str(random.randint(18, 23)) + " months."
    elif support == 7:
        row[index] = "I've been on government support for the past 2 years."
    else:
        row[index] = ""

# Time travel work daily - TRAVEL
def travelWork(row, index):
    travel = int([row[index]][0])
    if travel == 1:
        row[index] = "I live 10 min away from work."
    elif travel == 2:
        row[index] = "My commute is " + str(random.randint(11, 29)) + " min long."
    elif travel == 3:
        row[index] = "My commute is " + str(random.randint(30, 59)) + " min long."
    elif travel == 4:
        row[index] = "My commute is several hours long."
    elif travel == 6:
        row[index] = "I work from home."
    else:
        row[index] = ""

# Level of trust in police in local area - TRSQ04
def trustPolice(row, index):
    trust = int([row[index]][0])
    if trust == 1:
        row[index] = "I trust the police in my area."
    elif trust == 5 or trust == 4:
        row[index] = "I don't trust the police in my area."
    else:
        row[index] = ""

# TYPORG
def volReturn(row, index):
    volunteer = int([row[index]][0])
    if volunteer == 10:
        return("heritage services")
    elif volunteer == 11:
        return("unions")
    elif volunteer == 12:
        return("welfare")
    elif volunteer == 13:
        return("education services")
    elif volunteer == 14:
        return("youth services")
    elif volunteer == 15:
        return("emergency services")
    elif volunteer == 16:
        return("environmental organisations")
    elif volunteer == 17:
        return("animal welfare")
    elif volunteer == 18:
        return("international aid")
    elif volunteer == 19:
        return("health services")
    elif volunteer == 20:
        return("justice")
    elif volunteer == 21:
        return("religious organisations")
    elif volunteer == 22:
        return("sports")
    elif volunteer == 24:
        return("ethnic groups")
    else:
        return("")

# Orgs volunteered for in last 12 months - TYPORG
def typeVolunteer(row, index):
    volunteer = int([row[index]][0])
    if volunteer == 25 or volunteer == 23:
        row[index] = "I volunteer in my free time."
    elif volunteer == 26:
        row[index] = ""
    else:
        a = []
        # generate an array of volunteer organisations
        for i in range(1, 16):
            addOn = volReturn(row, index + i)
            if len(addOn) != 0:
                a.append(addOn)
        # add volunteer organisations to base sentence
        if len(a) != 0:
            if len(a) >= 4:
                randomPop(a, 4)
            row[index] = joinStrings("I volunteer in ", a)
        else:
            row[index] = ""
    clearInts(row, index + 1, index + 16)

# Home broken into in past 12 months - VICTIM
def breakInVictim(row, index):
    breakIn = int([row[index]][0])
    if breakIn == 1:
        row[index] = "My home was broken into this year."
    else:
        row[index] = ""    

# Visa type - VISCURCF
def visaType(row, index):
    visa = int([row[index]][0])
    if visa == 1:
        return("permanent visa.")
    elif visa == 2:
        return("temporary visa.")
    else:
        return("")

# Year arrived in Australia - YRARRBC
def yearArrived(row, index):
    year = int([row[index]][0])
    visa = visaType(row, VISCURCF)
    if year == 1:
        row[index] = "I was born in Australia."
    elif year == 2:
        row[index] = "I moved to Australia before 1990."
    elif year == 3:
        if len(visa) == 0:
            row[index] = "I came to Australia in " + str(random.randint(1991, 1995)) + "."
        else:
            row[index] = "I came to Australia in " + str(random.randint(1991, 1995)) + \
            " with a " + visaType(row, index)
    elif year == 4:
        row[index] = "I moved to Australia in " + str(random.randint(1996, 2000)) + "."
    elif year == 5:
        row[index] = "I arrived in Australia in " + str(random.randint(2001, 2005)) + "."
    elif year == 6:
        if len(visa) == 0:
            row[index] = "I came to Australia in " + str(random.randint(2006, 2010)) + "."
        else: 
            row[index] = "I came to Australia in " + str(random.randint(2006, 2010)) + \
            " with a " + visa
    else:
        row[index] = ""

# Define headers in input .csv file
headers = ["ALLHOMA", "ALLHOMB", "ALLHOMC", "ALLHOMD", "ALLHOME", "ALLHOMF", "ALLHOMG",
        "ALLHOMH", "ALLHOMI", "ALLHOMJ", "ALLHOMK", "ALLHOML", "ALLHOMM", "ALLHOMN", "ALLHOMO",
        "ALLHOMP", "ALLHOMQ", "ASSAULT", "ATRQ01CF", "BEDCURF", "CASHFLTA", "CASHFLTB", "CASHFLTC",
        "CASHFLTD", "CASHFLTE", "CASHFLTF", "CASHFLTG", "CASHFLTH", "CASHFLTI", "CASHFLTJ", "CASHFLTK",
        "COBBC", "COMHOM", "COTVALCF", "DISTYPCA", "DISTYPCB", "DISTYPCC", "DISTYPCD", "DISTYPCE",
        "DWSTBC", "EDATTBC", "EDFIECF", "EVRHMLES", "FAMCOMB", "FPTSTA", "FPTSTUDY", "FREQVORG",
        "FSRQ03", "HOMQ01A", "HOMQ01B", "HOMQ01C", "HOMQ01D", "HOMQ01E", "HOMQ01F",
        "HOMQ01G", "HOMQ01H", "HOMQ01I", "HOMQ01J", "HRSWKBC", "LEVTOL", "MRDSTU",
        "MULTIJOB", "OCCBC", "OLSQ01", "OTHRCON", "REGMAR", "RENTBCF", "RETSTACF", "SAFEQ01", "SAFEQ02",
        "SAFEQ03", "SERDIFFA", "SERDIFFB", "SERDIFFC", "SERDIFFD", "SERDIFFE", "SERDIFFF", "SERDIFFG",
        "SERDIFFH", "SERDIFFI", "SERDIFFJ", "SERDIFFK", "SOHQ01A", "SPHQ02", "SPOKENG", "STATEUR",
        "STRESSA", "STRESSB", "STRESSC", "STRESSD", "STRESSE", "STRESSF", "STRESSG", "STRESSH",
        "STRESSI", "STRESSJ", "STRESSK", "STRESSL", "STRESSM", "STRESSN", "STRESSO", "STRESSOP",
        "TIMEGVBC", "TRAVEL", "TRSQ04", "TYPORGA", "TYPORGB", "TYPORGC", "TYPORGD", "TYPORGE", 
        "TYPORGF", "TYPORGG", "TYPORGH", "TYPORGI", "TYPORGJ", "TYPORGK", "TYPORGL", "TYPORGM",
        "TYPORGN", "TYPORGO", "TYPORGP", "VICTIM", "VISCURCF", "YRARRBC"]

# Method to derive row of headers
# Returns row of headers
def dataHeaders():
    # open file, read binary
    # was rb
    with open('input.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            return row

# Method to get header indexes
# Returns int respresenting index
def getHeaderIndex():
    headerDictionary = {}
    indexList = []
    for header in headers:
        # print(header)
        headerIndex = dataHeaders().index(header)
        headerDictionary[header] = headerIndex
        indexList.append(headerIndex)
    # return headerDictionary
    return indexList

# Method to reduce the csv by column of needed headers
# Returns none
def reduceDataByColumn(infile, outfile):
    print("Reducing to useful columns...")
    indexList = getHeaderIndex()
    reducedRowsList = []
    # open output file for binary writing
    with open(outfile, 'w') as outputFile:
        spamwriter = csv.writer(outputFile)
        # open infile for binary reading
        with open(infile, 'r') as csvfile:
            spamreader = csv.reader(csvfile)
            # headerDictionary = replaceHeaderCodes()
            rowsDone = 0
            for row in spamreader:
                reducedRow = []
                for index in indexList:
                    reducedRow.append(row[index])
                if reducedRow in reducedRowsList:
                    print("Dupilicate row")
                else:
                    spamwriter.writerow(reducedRow)
                # print(reducedRow)

# Method to translate ints to sentences
# Returns none
def fillInData(infile, outfile):
    print("Filling in data ...")
    rowsDone = 0
    # open outfile for binary writing
    with open(outfile, 'w') as outputfile:
        w = csv.writer(outputfile)
        # open infile for binary reading
        with open(infile, 'r') as datafile:
            r = csv.reader(datafile)
            # headers = r.next()
            headers = next(r)
            print(headers)
            #print(currentIndex)
            for row in r:
                rowsDone += 1
                print("Computing row " + str(rowsDone) + "...")
                if rowsDone == 28404:
                    #28404
                    print("Computation complete.")
                    break
                for i in headers:
                    currentIndex = headers.index(i)                    
                    if i == "ALLHOMA":
                        withoutHome(row, currentIndex)
                    elif i == "ASSAULT":
                        assault(row, currentIndex)
                    elif i == "ATRQ01CF":
                        transportDifficulty(row, currentIndex)
                    elif i == "BEDCURF":
                        numBedrooms(row, currentIndex)
                    elif i == "CASHFLTA":
                        cashProblems(row, currentIndex)
                    elif i == "COBBC":
                        birthCountry(row, currentIndex)
                    elif i == "COMHOM":
                        computerUse(row, currentIndex)
                    elif i == "COTVALCF":
                        debtValue(row, currentIndex)
                    elif i ==  "DISTYPCA":
                        disabilityType(row, currentIndex)
                    elif i == "DWSTBC":
                        dwellingType(row, currentIndex)
                    elif i == "EDATTBC":
                        educationHighest(row, currentIndex)
                    elif i ==  "EVRHMLES":
                        homelessness(row, currentIndex)
                    elif i == "FPTSTA":
                        workStatus(row, currentIndex)
                    elif i == "FPTSTUDY":
                        studyStatus(row, currentIndex)
                    elif i == "FREQVORG":
                        volunteer(row, currentIndex)
                    elif i == "FSRQ03":
                        billPaying(row, currentIndex)
                    elif i ==  "HOMQ01A":
                        homelessExperience(row, currentIndex)
                    elif i == "HRSWKBC":
                        hoursWork(row, currentIndex)
                    elif i == "LEVTOL":
                        cultureAccept(row, currentIndex)
                    elif i == "MULTIJOB":
                        multipleJobs(row, currentIndex)
                    elif i == "OCCBC":
                        mainOccupation(row, currentIndex)
                    elif i == "OLSQ01":
                       lifeSatisfaction(row, currentIndex) 
                    elif i == "OTHRCON":
                       familyContact(row, currentIndex) 
                    elif i == "REGMAR":
                        maritalStatus(row, currentIndex)
                    elif i == "RENTBCF":
                        rent(row, currentIndex)
                    elif i == "RETSTACF":
                        retireStatus(row, currentIndex)
                    elif i == "SAFEQ01":
                        safeDay(row, currentIndex)
                    elif i == "SAFEQ02":
                        safeNight(row, currentIndex)
                    elif i == "SAFEQ03":
                       safeWalkNight(row, currentIndex) 
                    elif i ==  "SERDIFFA":
                       serviceAccess(row, currentIndex) 
                    elif i == "SOHQ01A":
                        unpaidCarer(row, currentIndex)
                    elif i == "SPHQ02":
                        medicalAfford(row, currentIndex)
                    elif i == "SPOKENG":
                        englishProf(row, currentIndex)
                    elif i == "STATEUR":
                        stateReside(row, currentIndex)
                    elif i == "STRESSA":
                        stress(row, currentIndex)
                    elif i == "TIMEGVBC":
                        govSupport(row, currentIndex)
                    elif i == "TRAVEL":
                        travelWork(row, currentIndex)
                    elif i == "TRSQ04":
                        trustPolice(row, currentIndex)
                    elif i == "TYPORGA":
                        typeVolunteer(row, currentIndex)
                    elif i == "VICTIM":
                        breakInVictim(row, currentIndex)
                    elif i == "VISCURCF":
                        visaType(row, currentIndex)
                    elif i == "YRARRBC":
                        yearArrived(row, currentIndex)
                        row[VISCURCF] = ""
                w.writerow(row)

states = ['input']
fileRoot = ''
for i in range(len(states)):
    print(i)
    infile = fileRoot+states[i]+ ".csv"
    outfile = fileRoot+states[i]+ "_out.csv"
    outfile2 = fileRoot+states[i]+ "_filledin.csv"
    print(infile, outfile, outfile2)
    reduceDataByColumn(infile, outfile)
    fillInData(outfile, outfile2)

