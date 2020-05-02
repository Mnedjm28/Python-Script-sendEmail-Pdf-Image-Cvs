import os
import smtplib, ssl, imghdr
from email.message import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = 'sender_email'
password = 'password'

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()# Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo()# Can be omitted
    server.login(sender_email, password)

    msg = EmailMessage()
    msg['Subject'] = "Rest Password"
    msg['From'] = sender_email
    msg['To'] = 'nadjmo'
    msg.set_content('hey you your password its **********')


    # For sending file have a foramt PDF
    with open('kko.pdf', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        print(file_name)
        print(file_type)
        msg.add_attachment(file_data,  maintype='application', subtype='octet-stream', filename=file_name)

    # For sending file have a foramt Xlsx CSV
    with open('all_books.xlsx', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        print(file_name)
        print(file_type)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


    # For sending file have a foramt Image
     with open('pp.jpg', 'rb') as f:
         file_data = f.read()
         file_type = imghdr.what(f.name)
         file_name = f.name
         print(file_name)
     msg.add_attachment(file_data,  maintype='application', subtype=file_type, filename=file_name)
     msg.add_attachment(file_data,  maintype='image', subtype=file_type, filename=file_name)


    server.sendmail(sender_email, 'recieve_email', msg.as_string())

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    print('done')
    server.quit()










