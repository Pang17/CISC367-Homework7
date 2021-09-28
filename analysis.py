from input import data, thread, timestamp, message, speaker


keywords= ["?", "who", "what", "when", "why", "where", "which"]

thread_id= []
thread_characteristic = []

#remove duplicates
for i in thread:
    if i not in thread_id:
        thread_id.append(i)

total_count = 0
for i in range(0, len(thread_id)):
    count = 0
    for row in data:
        if str(thread_id[i]) == row[0]:
            if any(x in row[3] for x in keywords):
                count+=1
                total_count+=1
                #print("thread_id: ", thread_id[i], " count = ", count)
    thread_characteristic.append([thread_id[i], count])

#print(thread_characteristic)
#print(total_count)