import json
from datetime import *
import datetime
import os

today = date.today()
time = datetime.datetime.now()

print(today.year, today.month, today.day)
print(time.hour, time.minute)

id_file = open("ids.json", "r")
id_file_contents = json.load(id_file)

#get list of names
names = []
ids = []
for id in id_file_contents:
    names.append(id_file_contents[id])
    ids.append(id)

day_file_name = f'{today.year}-{today.month}-{today.day}.json'

#access by day
if not os.path.exists(day_file_name):
    # created json
    with open(day_file_name, "w") as day_file:
        day = {}
        for name in names:
            day[name]=[]
        json.dump(day, day_file)

day = None
with open(day_file_name, "r") as day_file:
    day = json.load(day_file)

with open(day_file_name, "w") as day_file:
    id_in = input().strip()
    index = ids.index(id_in)
    name = names[index]
    if name in day:
        if len(day[name]) in (0, 1):
            day[name].append([time.hour, time.minute])
            print("Signed in!")
        else:
            day[name][1] = [time.hour, time.minute]
            print("Signed out!")
    else:
        print("Not valid name or ID!")
    json.dump(day, day_file)