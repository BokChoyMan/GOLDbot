import pyautogui as py
import numpy as np
import time
import sys
from selenium import webdriver
from datetime import datetime
from PIL import ImageGrab

# establishes whether to debug or not
DEBUGGING = False

# establishes the pathname
path = '/Users/bindingoath/Downloads/chromedriver'
sys.path.append(path)


# begins the program
def begin():
    openBrowser()
    login()
    # Allows time for webpage to load
    time.sleep(1)
    # terminates program after purpose is done
    terminate()


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


def terminate():
    holdKey(0.25, 'command', 'q')


def debug(str):
    if DEBUGGING:
        print(str)


if not DEBUGGING:
    username = input('Username: ')
    password = input('Password: ')
    browser = webdriver.Chrome(path)
    begin()
