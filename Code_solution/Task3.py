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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
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

#Part A
blr_fixed_number_list = [number for number in phone_number_record if number.startswith('(080)')]

AreaCodeList = []
MobileCodeList = []
for number in blr_fixed_number_list:
    for call in calls:
        if(number == call[0]):
            if('(' in call[1] and call[1][call[1].find("("):call[1].find(")")+1] not in AreaCodeList):
                AreaCodeList.append(call[1][call[1].find("("):call[1].find(")")+1])
            elif(' ' in call[1] and call[1][0:4] not in MobileCodeList):
                MobileCodeList.append(call[1][0:4])

CodeList = AreaCodeList + MobileCodeList

CodeList.sort()

print("The numbers called by people in Bangalore have codes:")
for code in CodeList:
    print(code)
print('\n')

#Part B
fixedLineCallerCounter = 0
fixedLineReceiverCounter = 0
for number in blr_fixed_number_list:
    for call in calls:
        if(number == call[0]):
            fixedLineCallerCounter  += 1 
            if(call[1][call[1].find("("):call[1].find(")")+1] == '(080)'):
                fixedLineReceiverCounter += 1
print("%f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." %round((fixedLineReceiverCounter/fixedLineCallerCounter)*100,2))