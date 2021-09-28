import csv
from analysis import thread_characteristic

header = ['Conversation ID', 'Characteristic Value']
f = open('results.csv', 'w')

writer = csv.writer(f)

writer.writerow(header)
for row in thread_characteristic:
    writer.writerow(row)

f.close