import logging
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPResponseException

from dotenv import load_dotenv

from app.email_templates import get_template


load_dotenv(override=True)


class EmailClient:
    def __init__(self):
        self.user = os.getenv("ADMIN_USER")
        app_password = os.getenv("APP_PASSWORD")
        if not self.user or not app_password:
            raise ValueError(
                "Please, fill in your USER and APP_PASSWORD as environment variables"
            )
        self.server = SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        try:
            self.server.login(self.user, app_password.replace(" ", ""))
        except SMTPResponseException as exc:
            logging.error(f"Could not login to the mail server with error: {exc}")
            raise exc
        self.log_file = open(
            f"./logs/secret_santa_{time.strftime('%H_%M_%S', time.gmtime())}.log",
            "w",
        )

    def send_email(self, giver_name, giver_email, receiver_name):
        admin_email = f"{self.user}@gmail.com"
        title, body = get_template(
            os.getenv("LANG", "ES"), giver_name, receiver_name, admin_email
        )
        test_email = os.getenv("TEST_EMAIL")
        actual_recipient = giver_email if not test_email else test_email

        message = MIMEMultipart("alternative")
        message["From"] = admin_email
        message["To"] = actual_recipient
        message["Subject"] = title
        message["Reply-to"] = "noreply@gmail.com"
        message.attach(MIMEText(body, "html"))

        self.server.sendmail(admin_email, actual_recipient, message.as_string())
        self.log_file.write(
            f"Email sent to {giver_name}({giver_email}) with receiver {receiver_name}.\n"
        )

    def close(self):
        self.server.quit()
        self.log_file.close()
