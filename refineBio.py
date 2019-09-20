#######################################################################################################
# Python program to refine biographies from the provided .csv file                                    #
# Code adapted from Jia Zhang                                                                         #
# Written by Zainab Alasadi                                                                           #
# Saturday 14th September 2019                                                                        #
#######################################################################################################

import csv
import random

states = ['input']
currentFile = 0
fileRoot = ''
priority1 = []
priority2 = []
priority3 = []

# Method to derive tweets from columns
# Returns none
def reduceDataByColumn(infile,outfile):
    existingTweets = []
    with open(outfile, 'w') as outputFile:
        spamwriter = csv.writer(outputFile)
        with open(infile, 'r') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                newRow = []
                newRowText = ""
                for column in row:
                    if len(column) > 6:
                        newRow.append(column)
                        newRowText += column
                shortTweet = ""
                rowLength = len(newRow)
                sampling = random.sample(range(1, len(newRow)), rowLength - 1)
                for i in sampling:
                    if len(shortTweet) == 0:
                            shortTweet = str(newRow[i])
                    else:
                        shortTweet += " " + str(newRow[i])
                # append sentences to each other         
                while len(newRowText) > 270 and rowLength > 5:
                    sampling = random.sample(range(1, len(newRow)), rowLength - 1)
                    rowLength = rowLength - 1
                    shortTweet = ""
                    for i in sampling:
                        if len(shortTweet) == 0:
                            shortTweet = str(newRow[i])
                        else:
                            shortTweet += " " + str(newRow[i])
                if shortTweet in existingTweets:
                    print("Repeat tweet...")
                else:
                    spamwriter.writerow([shortTweet])
                
infile = fileRoot + states[currentFile] + "_filledin.csv"
outfile = fileRoot + states[currentFile] + "_refined.csv"
reduceDataByColumn(infile, outfile)
maxLength = 31

# Method to create tweets from columns
# Returns none
def findCompleteRow(infile):
    maxLength = 0
    with open(infile, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            rowLength = len(row)
            for column in row:
                if column == "":
                    rowLength = rowLength - 1
            if rowLength > 30:
                print(row)
        print(maxLength)