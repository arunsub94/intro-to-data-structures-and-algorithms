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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getUniquePhoneNumbersFromRecords(records):
    phoneNoList = []
    
    for record in records:
        if(record[0] not in phoneNoList):
            phoneNoList.append(record[0])
        if(record[1] not in phoneNoList):
            phoneNoList.append(record[1])
    
    return phoneNoList

unique_number_record = getUniquePhoneNumbersFromRecords(texts + calls)

#Number of distinct telephone numbers in records
count = len(unique_number_record)

print("There are %d different telephone numbers in the records." %count)