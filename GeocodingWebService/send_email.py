import smtplib
from email.mime.text import MIMEText

def send_email(email, height, average_height, count):
#    from_email="john.goodman@gmail.com"
#    from_password="cleartextpasswordseemslikeabadidea"
#    to_email=email

#    subject="Height Data"
    message="Your height is <strong>%s</strong>. <br> Average height is <strong>%s</strong> out of <strong>%s</strong> people." % (height, average_height, count)
    print(message)
#    msg=MIMEText(message, 'html')
#    msg['Subject']=subject
#    msg['To']=to_email
#    msg['From']=from_email
#
#    gmail=smtplib.SMTP('smtp.gmail.com', 587)
#    gmail.elho()
#    gmail.starttls()
#    gmail.login(from_email, from_password)
#    gmail.send_email(msg)
