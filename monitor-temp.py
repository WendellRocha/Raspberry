import os
import time

def measure_temp():
	temp = os.popen('vcgencmd measure_temp').readline()
	temp.replace('\'','º')
	return (temp.replace('temp=',''))

while True:
	print(measure_temp())
	time.sleep(1)