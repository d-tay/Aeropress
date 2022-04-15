# -*- coding: utf-8 -*-
"""
Aeropress 
Inspired by Caffiene

A program that keeps your computer from falling asleep by simulating a key press periodically
"""
import pyautogui
import time
from infi.systray import SysTrayIcon

interval = 60.0 * 4.5

def keyPress():
    starttime = time.time()
    while True:
        #print("tick")
        pyautogui.press('f15')  # press the f15 key
        time.sleep(interval - ((time.time() - starttime) % interval))
    
def sysTray():
    systray = SysTrayIcon("aeropress_wh.ico", "Aeropress")
    systray.start()
    keyPress()
    

def main():
    sysTray()
    
main()
