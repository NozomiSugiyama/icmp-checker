#! /usr/bin/python
import subprocess
from time import sleep
import datetime
import os

duration = 1  # second
freq = 440  # Hz

def is_connectable(host):
    ping = subprocess.Popen(["ping", "-w", "3", "-c", "1", host], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0

count = 0;
errorCount = 0;
while(True):
    count += 1
    result = is_connectable('8.8.8.8')
    print(count ,datetime.datetime.now(), count, ":", result)
    if not result:
        if errorCount > 3:
            for _ in range(3):
                for _ in range(3):
                    p = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", os.getcwd() + "/sound.mp3"], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                    p.poll()
                    sleep(.1)
                sleep(1)
            sleep(5)
        else:
            sleep(5)
        errorCount = errorCount + 1
    else:
        errorCount = 0;
        sleep(10)

