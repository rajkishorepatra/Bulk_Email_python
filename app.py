#Below is the python program for sending bulk emailId by reading the email-Id and name from csv file

#Please read README file to know how to use


import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(name,rec_email):
    mail_content = f'''Hello {name},
    Here is a demo mail body
    Thank you'''

    sender_address = 'your email-id'
    sender_pass = 'email-Id Password'
    receiver_address = rec_email

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Subject'
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = f'path/to/any/file/to/attach/in/mail'
    with open(attach_file_name,'rb') as f:
        attachment = MIMEApplication(f.read(), Name=basename(attach_file_name))
        attachment['Content-Disposition'] = 'attachment; attach_file_name="{}"'.format(basename(attach_file_name))
    message.attach(attachment)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    session.send_message(message, sender_address, receiver_address)
    session.quit()



data = pd.read_csv(r'path/to/csv/file')
df = pd.DataFrame(data, columns= ['Name']) 
x=data[:]['Email-ID']
y=data[:]['Name']

j=0
for i in x:
    send_mail(y[j],i)
    print(f'Mail Sent {y[j]}')
    j++
    





# ©rajkishorepatra- 📧rpatrasm@gmail.com