import random
import time
import schedule as sched
import email, smtplib, ssl, os
from email.message import EmailMessage
from datetime import datetime


# credentials
sender = r"jomfarlane@gmail.com"
passwd = r"pmywogbaafvuakat"
receipients = ["inf_email@telegmail.com","ghostvansisher@telegmail.com"]

host = "smtp.gmail.com"
port = 465 #use 587 tls, 465 is for ssl?

##############################
##############################

random_facts = [
    "Every journalist has a movel in him, which is an excellent place for it. - Ryssel Lynes",
    "Just because someone doesn't react, doesn't mean they didn't notice.",
    "I got kicked out of a ballet class because I pulled a groin muscle. it wasn't mine. - Rita Rudner",
    "80% of all serious or fatal car craches are caused by men.",
    "Nothing is impossible. Some things are just more likely than others. - Jonathan Winters",
    "A person that truly loves you will let you go, no matter how hard the situation is.",
    "A psychiatrist is a fellow who asks you a lot of expensive questions your wife asks for nothing. - Joey Adams",
    "Girls who have high trust with their fathers also have tend to have high trust with their boyfriends."
    ]


def select_random_fact(random_fact: list):
    return random.choice(random_fact)

def send_fact_as_email():
    email = EmailMessage()
    email["From"] = sender
    #email["To"] = receipients
    email['To'] = ', '.join(receipients)
    email['Subject'] = "Random Facts! - with Python"
    email.set_content(select_random_fact(random_facts))
    
    # for secure connection
    context = ssl.create_default_context()
    
    
    def time_now():
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp
    
    
    


    # exit()
    
    ###################
 
    # using context manager
    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receipients, email.as_string())
        print(f"Fact sent! at {time_now()}")
    
 
if __name__ == "__main__":
    print("Running...")
    sched.every(120).seconds.do(send_fact_as_email)
    # sched.every().day.at("00:10:55").do(send_fact_as_email)
    
    while True:
        sched.run_pending()
        time.sleep(1)
    





"""
def job():
    print("doing job")
    print("Reading time...\n")

# time
sched.every(5).seconds.do(job)
sched.every(10).seconds.do(coding)
sched.every().day.at("11:20:35").do(playing)


while True:
    sched.run_pending()
    time.sleep(1)

#count = 1
#while count <= 6:
    #print(random.choice(messages))
    #count += 1


#for message in messages:
    #print(message)
"""
