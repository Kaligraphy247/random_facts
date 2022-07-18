import os
import random
import smtplib
import ssl
import time
import schedule as sched

from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import Callable
from datetime import datetime
from dotenv import load_dotenv, find_dotenv


# FUNCTIONS
def check_files(root_dir: str) -> list[str]:
    """Checks for files in given directory,
        excluding all folders.
    """
    my_files = [file for file in os.listdir(root_dir) if os.path.isfile(f"{root_dir}/{file}")]
    return my_files

def select_quote_image(func) -> Callable:
    """ Randomly selects  a file (image) for the qoute."""
    return f"{ROOT_DIR}/{random.choice(func)}"

def select_random_fact(random_fact: list) -> str:
    return random.choice(random_fact)

def send_fact_as_email():
    email = MIMEMultipart()
    email["From"] = sender
    email['To'] = ', '.join(receipients)
    email['Subject'] = "Random Facts! - with Python"
    body = MIMEText(select_random_fact(random_facts), "plain")
    email.attach(payload=body)
    
    # for secure connection
    context = ssl.create_default_context()
    
    def time_now():
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp


    # using a context manager
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receipients, email.as_string())
        print(f"Fact sent at {time_now()}")


def send_quote_image() -> None:
    """ Sends slected quote images to defined email addresses"""
    body="\nQuotes - Credit to https://t.me/Quotes"

    # email content
    email = MIMEMultipart()
    email['From'] = sender
    email['To'] = ', '.join(receipients)
    email['Subject'] = "Random Facts! - with Python"
    body = MIMEText(body, "plain")
    email.attach(payload=body)


    # email attachments
    attachment = select_quote_image(func=check_files(root_dir=ROOT_DIR))

    with open(attachment, 'rb') as file:
        part = MIMEApplication(file.read(), name=os.path.basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'

    email.attach(payload=part)

    def time_now():
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp

    # for secure connection
    context = ssl.create_default_context()
    # using a context manager
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receipients, email.as_string())
        print(f"Quote sent at {time_now()}")


# load .env
load_dotenv()

# Credentials
sender = os.environ.get('EMAIL_SENDER') # sender email
passwd = os.environ.get('APP_PASSWORD')


# GLOBAL VARIABLES
ROOT_DIR = r"/home/james/facts/random_facts/files"

# server stuff
host = "smtp.gmail.com"
port = 465 #use 587 tls, 465 is for ssl?

receipients = [
    "inf_email@telegmail.com",
    "mzvdyxpe@hi2.in",
    "james_cvzone@telegmail.com",
    "arjancode@telegmail.com"
    ]


##############################
random_facts = [
    "Every journalist has a movie in him, which is an excellent place for it. - Ryssel Lynes",
    "Just because someone doesn't react, doesn't mean they didn't notice.",
    "I got kicked out of a ballet class because I pulled a groin muscle. It wasn't mine. - Rita Rudner",
    "80% of all serious or fatal car craches are caused by men.",
    "Nothing is impossible. Some things are just more likely than others. - Jonathan Winters",
    "A person that truly loves you will let you go, no matter how hard the situation is.",
    "A psychiatrist is a fellow who asks you a lot of expensive questions your wife asks for nothing. - Joey Adams",
    "Girls who have high trust with their fathers also have tend to have high trust with their boyfriends.",
    "You've gotta dance like there's nobody watching. - William W. Purkey",
    "When a man learns to love, he must bear the risk of hatred.",
    "Books can also provoke emotions.And emotions sometimes are even more troublesome than ideas. Emotions have led people to do all sorts of things they later regret-like, oh, throwing a book at someone else.",
    ]



if __name__ == "__main__":
    print("Running...")
    sched.every(28800).seconds.do(send_fact_as_email)
    sched.every(21600).seconds.do(send_quote_image)
    # print(sender, passwd)
    # exit()
    # send_fact_as_email()
    # send_quote_image(email_sender=sender, password=passwd)

    while True:
        sched.run_pending()
        time.sleep(1)