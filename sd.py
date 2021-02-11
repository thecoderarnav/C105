import csv
import math 

with open ("data2.csv", newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean (data):
    n = len ( data ) 
    total = 0
    for x in data:
        total += int (x)
    mean  = total/n
    return mean       

sqaure_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    sqaure_list.append(a)

sum = 0
for i in sqaure_list:
    sum  = sum+i 

result = sum / (len(data)-1) 
sd = math.sqrt(result)
print(sd)



