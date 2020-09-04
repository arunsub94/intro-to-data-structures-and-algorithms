"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getUniquePhoneNumbersFromRecords(records):
    phoneNoList = []
    
    for record in records:
        if(record[0] not in phoneNoList):
            phoneNoList.append(record[0])
        if(record[1] not in phoneNoList):
            phoneNoList.append(record[1])
    
    return phoneNoList

telNoList_texts = getUniquePhoneNumbersFromRecords(texts)

Callers = [call[0] for call in calls]
Receivers = [call[1] for call in calls]

CallerList = list(set(Callers))
ReceiverList = list(set(Receivers))

TelemarketerList = []
for number in phone_number_record: 
    if((number in CallerList) and (number not in ReceiverList) or (number not in telNoList_texts)):
        TelemarketerList.append(number)

TelemarketerList.sort()

print("These numbers could be telemarketers: ")
for number in TelemarketerList:
    print(number)