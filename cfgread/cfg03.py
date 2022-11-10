#!/usr/bin/env python3
## create file object in "r"ead mode
CNT = 0
with open("vlanconfig.cfg", "r") as configfile:
    CNT = CNT + 1 
    ## readlines() creates a list by reading target
    ## file line by line

    configlist = configfile.readlines()
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(CNT)
print(len(configlist))

