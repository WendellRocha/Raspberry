#coding: utf-8
import os
import time

def measure_temp():
	temp = os.popen('vcgencmd measure_temp').readline()
	return (temp.replace('temp=','').replace("'C\n", "C"))

while True:
	print(measure_temp())
	time.sleep(1)
