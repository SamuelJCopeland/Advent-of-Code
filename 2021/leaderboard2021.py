
import json
from datetime import datetime
import requests


def printMember(member):
    if member["name"] == None:
        print(f'Anonymous User #{member["id"]}', member["local_score"])
    else:
        print(member["name"], member["local_score"])

    days = []
    for day in member["completion_day_level"]:
        days.append((day, member["completion_day_level"][day]))

    days.sort(key=lambda d: int(d[0]))

    for day in days:
        print("{:02d}".format(int(day[0])) + " ", end='')
        try:
            print(datetime.utcfromtimestamp(
                int(day[1]["1"]["get_star_ts"]) - 18000).strftime('%b %d %H:%M:%S'), " ", end='')
            print(datetime.utcfromtimestamp(
                int(day[1]["2"]["get_star_ts"]) - 18000).strftime('%b %d %H:%M:%S'), " ")
        except:
            print("")
    print("")


#cookie = {'session': '53616c7465645f5f7535bef1d46addb31f795f61aea89f8e373f3f654e1cd1bbdb21a5eb10bab585c6ef95688fb9808b'}
cookie = {'session': '53616c7465645f5fb0d19a9f251d0b1384c2f96d2a7f3caf99bbbe0c83264f3bd5cdbc0b5d5f0c81e4c7e4c6df3fb225'}
r = requests.get(
    'https://adventofcode.com/2021/leaderboard/private/view/668907.json', cookies=cookie)
	
data = r.content
response = json.loads(data)

members = []

for user in response["members"]:
    member = response["members"][user]
    members.append(member)

members.sort(key=lambda m: m["local_score"], reverse=True)
print("")
for member in members:
    printMember(member)

input()
