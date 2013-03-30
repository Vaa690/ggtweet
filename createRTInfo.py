#!/C:/Pyhton27/337/Project1

#createRTInfo.py
#This file is used to check the RT extraction and use for RT queries
#Created by: Victor Abecassis
#Date: 2/10/2013
import string
import sqlite3 as lite
import sys
import re

rtInfo = []

#Connect to the database containing your golden globes tweet data
con = lite.connect('tweets.db')
cur = con.cursor()

#Find all retweets by matching for the 'RT' tag in text
sqlRT = "SELECT tweet FROM tweets WHERE tweet LIKE '%RT @%'"
cur.execute(sqlRT)

reTweets = cur.fetchall()
numOfRt = len(reTweets)

#Store info in the array rtInfo
for row in reTweets:
    rtInfo.append(str(row))

#Close and delete curser and database
cur.close()
del cur
con.close()
