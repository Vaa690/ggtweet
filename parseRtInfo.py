#parseRtInfo.py
#Creating regular expressions with 7 input strings to test split regex
#Created by: Victor Abecassis
#Date: 2/13/2012

from createRTInfo import rtInfo
import re

#Create two data arrays:
#rtdUsers to hold original user, rtdText to hold original tweet text
rtdUsers = []
rtdTexts = []

#regX1 used to match original user name and text
regX = r'(RT|Rt|rT|rt) @(.*?):? (.*)\b'
rtInfoSz = len(rtInfo)

#These tweets were pulled as retweets but arent
removedRT = [rtInfo[8712], rtInfo[59038]]
numRemRT = len(removedRT)

del rtInfo[8712]
del rtInfo[59038]

#Split rtInfo elements using the regex, Delete removed tweets from count
i = 0
while i < (rtInfoSz - numRemRT):
    line = rtInfo[i]
    rtText = re.split(regX, line)
    rtUN = rtText[2]
    rtTXT = rtText[3]
    rtdUsers.append(rtUN)
    rtdTexts.append(rtTXT)
    i+=1



