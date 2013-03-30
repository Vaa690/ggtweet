#countRT.py
#Get a count for retweeted users and text
#Created by: Victor Abecassis
#Date: 2/13/2012

import string
import sys

from parseRtInfo import rtdUsers, rtdTexts

userCount = []
textCount = []

rtdUserSz = len(rtdUsers)
rtdTextSz = len(rtdTexts)

#rtdUser1 and rtdText1 delete the duplicates form RT to use in count
#Convert to set to delete duplicates then convert back to use list index
rtdUser1 = list(set(rtdUsers))
rtdText1 = list(set(rtdUsers))

rtdUser1Sz = len(rtdUser1)
rtdText1Sz = len(rtdText1)

i = 0
while i < rtdUser1Sz:
    ucount = rtdUsers.count(rtdUser1[i])
    user = rtdUser1[i]
    userCount.append([user, userCount])
    i+=1

##i = 0
##while i < rtdText1Sz:
##    tcount = rtdTexts.count(rtdText1[i])
##    text = rtdText1[i]
##    textCount.append([text, textCount])
##    i+=1
    

#Instead of this text count, pull the tweet Id of the riginal tweet and put that in a table with the count

#Write files for manual checks
##with open('RTUser.txt', 'w') as f:
##    for row in rtdUser1:
##        f.write(str(row) + "\n")
##    f.closed
##
##with open('RTText.txt', 'w') as f:
##    for row in rtdText1:
##        f.write(str(row) + "\n")
##    f.closed
    
