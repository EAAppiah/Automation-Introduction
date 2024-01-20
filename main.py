import os
import yagmail_outlook

sender = 'emailautotesting8@gmail.com'
receiver = 'fahalykaheh2@10mail.xyz'

subject = """Automation Testing"""

contents = """This is a test email sent from Python"""

password = os.getenv('PASSWORD')

yag = yagmail_outlook.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")

 