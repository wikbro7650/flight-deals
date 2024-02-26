from twilio.rest import Client
import smtplib

TWILIO_SID = "AC96611a5c71f3094b241844d61bb0b9db"
TWILIO_AUTH_TOKEN = "6685f4ba3f4e1e4dba7a0a5a3831ed43"
TWILIO_VIRTUAL_NUMBER = '+15015570573'
TWILIO_VERIFIED_NUMBER = '+48693240274'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "wiktoria.bronowska.py@gmail.com"
MY_PASSWORD = "Zaq12w$x"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )