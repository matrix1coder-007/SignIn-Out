import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sign_out_time = "6:00 PM EST"

subject = "Ishita Katyal - " + sign_out_time + " Software Developer - Sign Out"
message = """Hi!\nI signed out at """ + str(sign_out_time) + """.\nRegards\nIshita Katyal"""
sender_address = "iskatyal@enhanceit.com"
password = "Qap25301"

receiver_emails = [
    "armusgrove@enhanceit.com", 
    "TopSourceAttendance@BrighterBrain.com"
    ]

for receiver_email in receiver_emails:
    receiver_address = receiver_email
    email = MIMEMultipart()
    email["From"] = sender_address
    email["To"] = receiver_address 
    email["Subject"] = subject

    email.attach(MIMEText(message, "plain"))
    text = email.as_string()

    session = smtplib.SMTP('smtp.office365.com', 587) 
    session.starttls()
    session.login(sender_address, password) 
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')