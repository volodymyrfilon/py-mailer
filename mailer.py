import smtplib
from email.mime.text import MIMEText

def send_email(message):
    # Put here your actual email adress from you want to send emails
    sender = "your_email@gmail.com"
    # Put here your password for email bot acc (NOT YOUR MAIN PASSWORD)
    password = "your_password"

    # If it is not gmail -> changr to your smtp domain
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # list of emails going to receive your email
    adresat = ["adresat_1@gmail.com", "adresat_2@gmail.com"]
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        # Add below Subject for mail (optional)
        msg["Subject"] = "Test Subject"
        server.sendmail(sender, adresat, msg.as_string())

        print("The message was sent successfully!")
    except Exception as _ex:
        print(f'{_ex}\nCheck your login or password please!')

def main():
    message = input("Enter your message: ")
    send_email(message=message)

if __name__ == '__main__':
    main()
