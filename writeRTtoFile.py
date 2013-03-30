#!/C:/Pyhton27/337/Project1

#wtiteRTtoFile.py
#Creates RT.txt 
#Created by: Victor Abecassis
#Date: 2/13/2013

from createRTInfo import rtInfo

#Create a text file with RT data just for checking the results
with open('RT.txt', 'w') as f:
    #Store info in the array rtInfo
    for row in rtInfo:
        f.write(str(row) + "\n")
    f.closed
    
print rtInfo[0]

