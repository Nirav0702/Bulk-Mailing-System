import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader

file = PdfFileReader("<enter file name>")
df = pd.read_csv("<Enter CSV")


def make_pdf(file, password):
    out = PdfFileWriter()
    num = file.numPages
    for i in range(num):
        page = file.getPage(i)
        out.addPage(page)
    passw = password
    out.encrypt(passw)
    with open("<saved_address>", "wb") as f:
        out.write(f)


def send_mail(name):
    mail_content = "Hello, " + name + "\n The password is your name DOB"
    sender_address = '<enter sender_mail'
    sender_pass = '<enter password>'
    receiver_address = df['Email'][i]
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Open me pls'

    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = '<enter saved address>'
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent to ' + df['Name'][i])


for i in range(len(df)):
    
    make_pdf(file, str(df['DOB'][i]))
    send_mail(df['Name'][i])
