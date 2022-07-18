import random
import time
import schedule as sched
import email, smtplib, ssl, os
from email.message import EmailMessage
from datetime import datetime

# Credentials
sender = os.environ.get('EMAIL_SENDER') # sender email
passwd = os.environ.get('APP_PASSWORD')

# receipients
receipients = [
    "inf_email@telegmail.com",
    "mzvdyxpe@hi2.in",
    "james_cvzone@telegmail.com"
    ]

# server stuff
host = "smtp.gmail.com"
port = 465 #use 587 tls, 465 is for ssl?

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


def select_random_fact(random_fact: list) -> str:
    return random.choice(random_fact)

def send_fact_as_email():
    email = EmailMessage()
    email["From"] = sender
    email['To'] = ', '.join(receipients)
    email['Subject'] = "Random Facts! - with Python"
    email.set_content(select_random_fact(random_facts))
    
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
        print(f"Fact sent! at {time_now()}")
    

if __name__ == "__main__":
    print("Running ...")
    sched.every(28800).seconds.do(send_fact_as_email)
    # sched.every().day.at("00:10:55").do(send_fact_as_email)
    
    while True:
        sched.run_pending()
        time.sleep(1)
