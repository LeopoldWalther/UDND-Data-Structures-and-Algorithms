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

calling_time = {}

for call in calls:
    calling_time[call[0]] = calling_time.get(call[0], 0) + int(call[3])  # returns 0 if key call[0] is not found
    calling_time[call[1]] = calling_time.get(call[1], 0) + int(call[3])

m = max(calling_time, key=calling_time.get)

print('{0} spent the longest time, {1} seconds, on the phone during September 2016.'.format(m, calling_time[m]))

