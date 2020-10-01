import smtplib
import email.utils
from email.mime.text import MIMEText

# import ssl # Used for secure connection


class Emailer:
  def __init__(self, source_email, port = 1025, server = "localhost"):
    self.port = port 
    self.smtp_server = server
    self.source_email = source_email

  def _send_message(self, reciever, subject, content):
    server = smtplib.SMTP(self.smtp_server, self.port)
        # Uncomment folllowing three lines and the ssl import,
        # if you would like to try with real modern servers 

        # context = ssl.create_default_context()        # create secure connection context
        # server.starttls(context=context)              # establish secure connection
        # server.login(sender_email, <PASSWORD>)        # log in
    msg = MIMEText(content)
    msg['From'] = email.utils.formataddr(('Author',  self.source_email))
    msg['To'] = email.utils.formataddr(('Recipient', reciever))
    msg['Subject'] = subject

    server.sendmail(self.source_email, [reciever], msg.as_string())
    server.quit()

  def on_alert(self, alert):
    pass