"""
cpu_monitor.py: Measures the temperature of the CPU and GPU
"""

__author__ = "Harry Ellerm"


import subprocess
import time
import re
import datetime


def measure_temp():

    print('CPU & GPU Temperature Stats')

    gpu_temp = None
    cpu_temp = None

    while True:

        gpu_temp = subprocess.run(['vcgencmd measure_temp'], 
                capture_output=True, shell=True, encoding='utf-8').stdout
        
        cpu_temp = round(int(subprocess.run(['cat /sys/class/thermal/thermal_zone0/temp'], 
            capture_output=True, shell=True, encoding='utf-8').stdout)/1000, 1)    
       
        print('***************************')
        print(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))        
        print(f'CPU temp={cpu_temp}\'C')
        print(f'GPU {gpu_temp}',end='')

        time.sleep(30)


try:
    measure_temp()
except KeyboardInterrupt:
    exit()

