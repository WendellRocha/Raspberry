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

ram = getRAM()
disk = getDiskSpace()
while True:
	print("CPU Temp: " + getCPUTemp())
    print("Total RAM: " + ran[0] + "\nUsed RAM: " ram[1] + "\nFree RAM: " ram[2])
    print("CPU Use (porcent): " + getCPUUse())
    print("Total disk space: " + disk[0] + "\nUsed disk space: " + disk[1] + "\nRemaining disk space: " + disk[2] + "\nPercent of disk used: " + disk[3])
	time.sleep(5)


