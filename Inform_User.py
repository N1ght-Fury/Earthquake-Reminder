import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_mail(user,text):
    try:

        message = MIMEMultipart()
        message["From"] = "Deprem Bildirim"
        message["To"] = user
        message["Subject"] = "Bölgenizde Deprem Oldu"
        message_text = text
        message_content = MIMEText(message_text, "html")
        message.attach(message_content)
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("enter mail address here", "enter password here")
        mail.sendmail(message["From"], message["To"], message.as_string())
        mail.close()

    except:
        sys.stderr.write("Something unexpected happend!")
        sys.stderr.flush()
