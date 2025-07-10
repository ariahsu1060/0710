import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
sender ="aria.hsu1060@gmail.com"
receiver=["juanx20020110@gmail.com"]
msg["fROM"] = sender
msg["TO"]= receiver[0]
msg["Subject"] = Header("test mail","utf-8").encode()
body = "this is mail from python"
msg_content = MIMEText(body,_charset="utf-8")
msg.attach(msg_content)
ssl_context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    server.login(sender,"yiyw vflg yydx zvjk")
    server.sendmail(sender,receiver[0],msg.as_string())

print("success send mail")
