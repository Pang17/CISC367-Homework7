import csv


data = []
thread = []
timestamp = []
speaker = []
message = []
thread_messages = []

with open('merged-pythondev-help-concat-group.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        data.append(row)

for i  in range(1, len(data)):
    thread.append(data[i][0])
    timestamp.append(data[i][1])
    speaker.append(data[i][2])
    message.append(data[i][3])

#change threads to integers
for i in range(0, len(thread)):
    thread[i] = int(thread[i])

thread.sort()