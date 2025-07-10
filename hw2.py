import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


sender ="aria.hsu1060@gmail.com"
with open("maillist.txt") as f:
    lines = f.readlines()
    receiver = []
    for i in lines:
        ans = i.split("\n")
        print(ans)
        receiver.append(ans[0])

print("total is"+str(len(receiver)))
for i in receiver:
    msg = MIMEMultipart()
    msg["fROM"] = sender
    msg["TO"]= i
    msg["Subject"] = Header("test mail","utf-8").encode()
    f = open("context.txt")
    body = f.read()
    print(body)
    f.close()
    msg_content = MIMEText(body,_charset="utf-8")
    msg.attach(msg_content)
    ssl_context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"yiyw vflg yydx zvjk")
        server.sendmail(sender,i,msg.as_string())

    print("success send mail")