import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
msg["fROM"] = "aria.hsu1060@gmail.com"
msg["TO"]= "ps610127@gmail.com"
msg["Subject"] = Header("test mail","utf-8").encode()
body = "this is mail from python"
msg_content = MIMEText(body,_charset="utf-8")
msg.attach(msg_content)

ssl_context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context)
server.login("aria.hsu1060@gmail.com","yiyw vflg yydx zvjk")
server.sendmail("aria.hsu1060@gmail.com","ps610127@gmail.com",msg.as_string())
server.close()
print("success send mail")
