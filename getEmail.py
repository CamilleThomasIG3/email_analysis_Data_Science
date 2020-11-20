import imaplib
import base64
import os
import email
import getpass
from email.header import decode_header
import webbrowser
import csv 

output = open('mail.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(output)
col_names = ['expediteur','date et heure', 'sujet',  'destinataire', 'contenu']
csvwriter.writerow(col_names)

# https://www.thepythoncode.com/article/reading-emails-in-python
# email_user = input('Email: ')
# email_pass = getpass.getpass('password: ')

mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
N = 10
mail.login(email_user, email_pass)
status, messages = mail.select('INBOX')


nbMessages = int(messages[0])
print(nbMessages)



for i in range(nbMessages, 0, -1):
    mail_line = []
    mail_line.append(email_user)
    date = None 
    subject = None
    From = None
    body = None
    # fetch the email message by ID
    res, msg = mail.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            try:  
                subject = decode_header(msg["Subject"])[0][0]
            except:
                pass
            # subject = decode_header(msg["Subject"])[0][0]
            date = decode_header(msg["Date"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                try:  
                    subject = subject.decode()
                except:
                    pass
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    # if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        # mail_line.append(body)
                    # elif "attachment" in content_disposition:
                    #     # download attachment
                    #     filename = part.get_filename()
                    #     if filename:
                    #         if not os.path.isdir(subject):
                    #             # make a folder for this email (named after the subject)
                    #             os.mkdir(subject)
                    #         filepath = os.path.join(subject, filename)
                    #         # download attachment and save it
                    #         open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                try:
                        # get the email body
                        
                    body = msg.get_payload(decode=True).decode()
                except:
                        pass
                # if content_type == "text/plain":
                    # print only text email parts
                    # mail_line.append(body)
            # if content_type == "text/html":
            #     # if it's HTML, create a new HTML file and open it in browser
            #     if not os.path.isdir(subject):
            #         # make a folder for this email (named after the subject)
            #         os.mkdir(subject)
            #     filename = f"{subject[:50]}.html"
            #     filepath = os.path.join(subject, filename)
            #     # write the file
            #     open(filepath, "w").write(body)
            #     # open in the default browser
            #     webbrowser.open(filepath)
            # print("="*100)
# close the connection and logout
    mail_line.append(date)
    mail_line.append(subject)
    mail_line.append(From)
    mail_line.append(body)
    csvwriter.writerow(mail_line)
output.close()
mail.close()
mail.logout()