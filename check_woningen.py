import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

URL = "https://your-house.nl/woning-huren"

EMAIL_FROM = os.environ["EMAIL_FROM"]
EMAIL_PASS = os.environ["EMAIL_PASS"]
EMAIL_TO = os.environ["EMAIL_TO"]

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

links = []

for a in soup.find_all("a", href=True):
    if "/woning/" in a["href"]:
        links.append("https://your-house.nl" + a["href"])

if links:

    msg = "Nieuwe woningen gevonden:\n\n"

    for l in links[:5]:
        msg += l + "\n"

    message = MIMEText(msg)
    message["Subject"] = "Nieuwe woningen alert"
    message["From"] = EMAIL_FROM
    message["To"] = EMAIL_TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_FROM, EMAIL_PASS)
        server.send_message(message)
