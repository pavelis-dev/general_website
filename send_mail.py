import smtplib
from setting import my_mail, password_mail
from email.mime.text import MIMEText


def send_email(name, mail, message):
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    message = f'{name}\n{mail}\n\n{message}'
    try:
        server.login(my_mail, password_mail)
        msg = MIMEText(message)
        msg['Subject'] = 'Письмо с главного сайта'
        server.sendmail(my_mail, my_mail, msg.as_string())
        return 'ok'
    except Exception as _ex:
        return 'no'
