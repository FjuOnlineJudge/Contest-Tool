# reference: https://geekflare.com/send-gmail-in-python/
# https://www.tutorialexample.com/send-email-to-others-by-outlook-email-python-smtp-tutorial/
import os, sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

class Mail:

    def __init__(self, port = 465, smtp_server_domain_name = "smtp.gmail.com", sender_mail = "", password = "", subject = ""):
        # # https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
        # # https://www.google.com/settings/security/lesssecureapps
        # # https://www.learncodewithmike.com/2020/02/python-email.html
        self.port = port
        self.smtp_server_domain_name = smtp_server_domain_name
        self.sender_mail = sender_mail
        self.password = password
        self.subject = subject

    def send(self, data):
        if self.port == 465:
            ssl_context = ssl.create_default_context()
            service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        elif self.port == 587:
            service = smtplib.SMTP(self.smtp_server_domain_name, self.port)
            service.ehlo()
            service.starttls()
            service.ehlo() 
        service.login(self.sender_mail, self.password)
        
        for idx,d in enumerate(data):
            if idx == 0:
                continue
            sid, teamid, passwd = d
            email = f"{sid}@m365.fju.edu.tw"

            ## MIMEMultipart instance
            mail = MIMEMultipart('alternative')
            mail['Subject'] = self.subject
            mail['From'] = self.sender_mail
            mail['To'] = email

            ## text and html templates
            text_template = """
            {0} 你好,
            """
            html_template = """
            <p>{0} 你好,</p>
            """

            ## MIMEText instances
            html_content = MIMEText(html_template.format(email.split("@")[0]), 'html')
            text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')
            
            ## attaching messages to MIMEMultipart
            mail.attach(text_content)
            mail.attach(html_content)

            ## attaching an attachment
            file_path_set = [] # f".out/submits/sample.zip"
            for file_path in file_path_set:
                if os.path.isfile(file_path):
                    mimeBase = MIMEBase("application", "octet-stream")
                    with open(file_path, "rb") as file:
                        mimeBase.set_payload(file.read())
                    encoders.encode_base64(mimeBase)
                    mimeBase.add_header("Content-Disposition", f"attachment; filename={Path(file_path).name}")
                    mail.attach(mimeBase)

            ## sending mail
            try:
                service.sendmail(self.sender_mail, email, mail.as_string())
                print("Have already sent to: " + email)
            except:
                print("Cannot send to: " + email)

        service.quit()

if __name__ == '__main__':
    data = [s.split(",") for s in sys.stdin]
    mail = Mail()
    mail.send(data)