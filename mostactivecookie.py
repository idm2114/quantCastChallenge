import sys
import os
from datetime import datetime, timedelta

def countCookies(filename, date):
    cookies = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = lines[1:] # getting rid of the header
        for line in lines:
            vals = line.strip().split(',')
            cookie = vals[0]
            timestamp = datetime.strptime(vals[1], "%Y-%m-%dT%H:%M:%S%z")
            # handling timezone offsets
            if str(timestamp.tzinfo) != 'UTC':
                if "+" in str(timestamp.tzinfo):
                    difference = str(timestamp.tzinfo).split("+")[1]
                    hours = int(difference.split(":")[0])
                    minutes = int(difference.split(":")[1])
                    timestamp = timestamp - timedelta(hours=hours, minutes=minutes)
                elif "-" in str(timestamp.tzinfo):
                    difference = str(timestamp.tzinfo).split("-")[1]
                    hours = int(difference.split(":")[0])
                    minutes = int(difference.split(":")[1])
                    timestamp = timestamp + timedelta(hours=hours, minutes=minutes)
            if timestamp.strftime("%Y-%m-%d") == date:
                if cookie not in cookies: 
                    cookies[cookie] = 0
                cookies[cookie] += 1

    # finding the top cookies by iterating through hashmap and keeping track of best so far
    topCookies = []
    topVal = 0
    for cookie in cookies: 
        if cookies[cookie] > topVal: # reset list if you find a more frequent cookie
            topVal = cookies[cookie]
            topCookies.clear()
            topCookies.append(cookie)
        elif cookies[cookie] == topVal: # add to existing list if you find a cookie with same freq
            topCookies.append(cookie)
    # formatting output in correct format
    print()
    for c in topCookies:
        print(c)

if __name__=='__main__':
    # ensure that input format is correct
    if len(sys.argv) != 4: 
        print("Usage is as follows: ./most_active_cookie <csvfile> -d <date>")
    else:
        countCookies(sys.argv[1], sys.argv[-1])
