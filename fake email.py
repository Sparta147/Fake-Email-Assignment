import smtplib

# Credentials from a service like Ethereal.email
smtp_server = "smtp.ethereal.email"
port = 587 
username = "faustino.cormier@ethereal.email"
password = "5HR3CDZmeac2HmdYc8"

message = """\
Subject: SALARY INCREMENT
To:  fredrick.ochieng@zetech.ac.ke
From: hr@zetech.ac.ke

Greetings, Mr. Fredrick Ochieng, this is to inform you that you have been awarded a salary increment of 10% effective from next month. Please contact the HR department for more details."""

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls() # Secure the connection
    server.login(username, password)
    server.sendmail("hr@zetech.ac.ke", "fredrick.ochieng@zetech.ac.ke", message)

print("Greetings, Mr. Fredrick Ochieng, this is to inform you that you have been awarded a salary increment of 10% effective from next month. Please contact the HR department for more details.")