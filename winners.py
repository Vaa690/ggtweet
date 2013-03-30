#!/C:/Python27

# change above line to point to local
# python executable

import string, sqlite3 as lite
import re, sys
import award.py
from award.py import *
import regex.py
from regex.py import *

con = lite.connect('tweets.sqlite3')

#winners = [[,,]]
winnerScore = []
winRegExGroupIdx = [1,2]
catRegExGroupIdx = [-1,1]
showRegExGroupIdx = [-1,3]

sqlQueries = ["SELECT tweet FROM tweets WHERE tweet LIKE '%win%' AND tweet NOT LIKE 'RT @%'", "SELECT tweet FROM tweets WHERE tweet LIKE 'RT @eonline:%'"]

regexes = [r'(.*)\bwins (Golden Globe)?(.*)for(.*)', r'RT @eonline: (.*): (.*)for(.*)#GoldenGlobes(.*)']

with con:
   for query in sqlQueries:
      cur = con.cursor()
      cur.execute(query)
      rows = cur.fetchall()

      for row in rows:
	     i = 0
	     for regex in regexes:
                matchObj = re.match( regex, row[0]

            if matchObj:
                                     for winner in winners:
                                     if winRegExGroupIdx[i] < 0:

			      else if
                  if winner[0] ==
               cnt = winners.count(matchObj.group(1))

               if cnt == 0:
                  winners.append(matchObj.group(1))
                  winnerScore.append(1)
               else:
	              idx = winners.index(matchObj.group(1))
	              winnerScore[winners.index(matchObj.group(1))] = winnerScore[winners.index(matchObj.group(1))] + 1

            i = i + 1

j = 0

print "Winners: "
print "winners length ", len(winners)
print "winnerScore length ", len(winnerScore)

for w in winners:
   if winnerScore[j] > 3:
      print j, ": ", w, "score: ", winnerScore[j]

   j = j+1

### Done!
