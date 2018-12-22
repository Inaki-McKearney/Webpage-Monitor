import smtplib
from email.mime import multipart
from email.mime import text


def send(body):
    username = 'EMAIL/USERNAME'
    password = 'EMAIL PASSWORD'
    fromaddr = 'SENDER EMAIL'
    toaddr = 'RECEIVER EMAIL'

    msg = multipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Page Modified'

    msg.attach(text.MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())


def main():
    pass


if __name__ == "__main__":
    main()
