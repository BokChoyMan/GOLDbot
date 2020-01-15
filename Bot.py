import pyautogui as py
import numpy as np
import time
import sys
from selenium import webdriver
from datetime import datetime
from PIL import ImageGrab

# establishes whether to debug or not
DEBUGGING = True

# establishes the pathname
path = '/Users/bindingoath/Downloads/chromedriver'
sys.path.append(path)


# begins the program
def begin():
    openBrowser()
    login()
    # Allows time for webpage to load
    time.sleep(1)
    # Clicks on the registration button
    py.click(420, 219)
    # terminates program after purpose is done
    terminate(2)


# opens the chrome browser
def openBrowser():
    browser.maximize_window()
    browser.get('https://my.sa.ucsb.edu/gold/login.aspx')
    # Allows time for webpage to load
    time.sleep(1)


# logs into account
def login():
    py.write(username)
    py.press('tab')
    py.write(password)
    py.press('return')


def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def holdKey(duration, key1, key2, key3='', key4=''):
    start = time.time()
    while time.time() - start < duration:
        py.hotkey(key1, key2, key3, key4)


def terminate(sec):
    time.sleep(sec)
    holdKey(0.35, 'command', 'q')



def timer(month, day, hour, min, sec):
    now = datetime.now()
    sMonth = int(now.strftime("%m"))
    sDay = int(now.strftime("%d"))
    sHour = int(now.strftime("%H"))
    sMin = int(now.strftime("%M"))
    sSec = int(now.strftime("%S"))
    while not (sMonth == month and sDay == day and sHour == hour and sMin == min and sSec == sec):
        while sSec < 60:
            time.sleep(1)
            print(sMonth, sDay, sHour, sMin, sSec)
            sSec = sSec + 1
            if sSec == sec:
                return
        sSec = 0
        sMin = sMin + 1
        if sMin > 60:
            sMin = 0
            sHour = sHour + 1
            if sHour > 24:
                sHour = 0
                sDay = sDay + 1



def debug(str):
    if DEBUGGING:
        print(str)


if not DEBUGGING:
    username = input('Username: ')
    password = input('Password: ')
    timer(1, 38, 3)
    browser = webdriver.Chrome(path)
    begin()

now = datetime.now()
print(int(now.strftime("%m")))
print("begin")
timer(1, 15, 1, 15, 50)
print("time is up")
