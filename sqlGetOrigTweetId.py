#!/C:/Pyhton27/337/Project1

#sqlGetOrigTweetId.py
#This file is used to get the original tweet Id to count faster than using text
#Created by: Victor Abecassis
#Date: 2/13/2013
import string
import sqlite3 as lite
import sys
import re

from countRT import rtdText1, rtdText1Sz

#Create an array to store all original tweet numbers
otIdNum = []

#Connect to the database containing your golden globes tweet data
con = lite.connect('tweets.db')
cur = con.cursor()

placeholder = '?'
placeholders = ', '.join(placeholder for unused in rtdText1)

sql = 'SELECT tweet_id FROM tweets WHERE tweet_text LIKE (%s)' % placeholders
cur.execute(sql)
    
otId = cur.fetchall()
otIdNum.append(otId)

#Close and delete curser and database
cur.close()
del cur
con.close()
