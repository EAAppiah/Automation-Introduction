import os
import yagmail

sender = 'emailautotesting8@gmail.com'
receiver = 'fahalykaheh2@10mail.xyz'

subject = """Automation Testing"""

contents = """This is a test email sent from Python"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")

 