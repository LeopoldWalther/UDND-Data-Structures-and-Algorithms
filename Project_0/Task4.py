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

# set of callers
callers = set()
called = set()
texted = set()

for call in calls:
    callers.add(call[0])
    called.add((call[1]))

for text in texts:
    texted.add(text[0])
    texted.add(text[1])

# union of sets of called, messengers, messaged
not_telemarketers = called.union(texted)

# difference of callers and rest
telemarketers = list(callers.difference(not_telemarketers))

print('These numbers could be telemarketers: ')

for num in sorted(telemarketers):
    print(num)
