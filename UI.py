
#from openpyxl import Workbook, load_workbook
#from openpyxl.utils import get_column_letter
#import pandas as pd
#import numpy as np

keywords={"Points":{"point","pts","ppg","how many points","score"},
            "Assists:":{"assist","ast","asg","how many assists","dimes"},
            "Rebounds":{"rebound","reb","rpg","how many rebounds","board"},
            "Minutes":{"minutes","min","mpg","how many minutes","time"}}

userRequest = input("What player stats are you interested in?")
userRequest=userRequest.lower().split()
inputList= []
  
     # loop till string values present in list userRequest
for i in userRequest:             
     # checking for the duplicacy
    if i not in inputList:
            # insert value in inputList
            inputList.append(i)

    # for loop that checks for the userinput in the dictionary
for i in inputList:
    for j, listOfKeywords in keywords.items():
        if i in listOfKeywords:
            requestedStat=keywords.key()

print(str(requestedStat))

#wb=load_workbook('/Users/trevorkasuku/Desktop/2Sigma/BasketballProject.xlsx')
#ws=wb.active
#for row in range(1,200):
 #   for col in range(1,7):
  #      char=get_column_letter(col)
 #       print(ws[char+str(row)].value)

#we check the values and return the key the key is used to get a certain row
#check name using dataframe
#str(int)==string
