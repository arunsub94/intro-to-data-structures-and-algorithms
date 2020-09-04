"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def getUniquePhoneNumbersFromRecords(records):
    phoneNoList = []
    
    for record in records:
        if(record[0] not in phoneNoList):
            phoneNoList.append(record[0])
        if(record[1] not in phoneNoList):
            phoneNoList.append(record[1])
    
    return phoneNoList

phone_number_record = getUniquePhoneNumbersFromRecords(calls) 

timeSpentDict = {}
for phone_no in phone_number_record: 
    timeSpent = 0
    for call in calls: 
        if(phone_no == call[0]):
            timeSpent += int(call[3])
        if(phone_no == call[1]):
            timeSpent += int(call[3])
    timeSpentDict[phone_no] = timeSpent

max_timeSpent_phoneNo = max(timeSpentDict, key = timeSpentDict.get)

print("%s spent the longest time, %d seconds, on the phone during September 2016." %(max_timeSpent_phoneNo,timeSpentDict[max_timeSpent_phoneNo]))