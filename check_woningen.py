import smtplib
from email.mime.text import MIMEText
import os

# E-mailgegevens via GitHub Secrets
EMAIL_FROM = os.environ["EMAIL_FROM"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
EMAIL_TO = "katinka_blom@hotmail.com"

# Dummy bericht
msg_content = "🎉 Dit is een testmail van je GitHub Actions workflow! Alles werkt."
message = MIMEText(msg_content)
message["Subject"] = "Test woning-alert"
message["From"] = EMAIL_FROM
message["To"] = EMAIL_TO

# Verstuur e-mail via Outlook SMTP
try:
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()  # versleuteling inschakelen
        server.login(EMAIL_FROM, EMAIL_PASS)
        server.send_message(message)
    print("Testmail succesvol verzonden!")
except Exception as e:
    print("Fout bij verzenden van e-mail:", e)
    raise
