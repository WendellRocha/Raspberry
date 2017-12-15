#coding: utf-8
import os
import time

def getCPUTemp():
	temp = os.popen('vcgencmd measure_temp').readline()
	return (temp.replace('temp=','').replace("'C\n", "ºC"))

def getRAM():
    p = os.popen('free')
    i = 0
    while 1:
        i += 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])

def getCPUUse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i += 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])


while True:
	print(getCPUTemp())
        print(getRAM())
        print(getCPUUse())
        print(getDiskSpace())
	time.sleep(1)
