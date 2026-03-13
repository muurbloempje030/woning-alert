import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

# URL van de woningpagina
URL = "https://your-house.nl/woning-huren"

# E-mailgegevens via environment variables
EMAIL_FROM = os.environ["EMAIL_FROM"]  # ← GitHub secret
EMAIL_PASS = os.environ["EMAIL_PASS"]  # ← GitHub secret
EMAIL_TO = "katinka_blom@hotmail.com"  # ← jouw e-mailadres

# Website ophalen
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

# Zoek links naar woningen
links = []
for a in soup.find_all("a", href=True):
    if "/woning/" in a["href"]:
        links.append("https://your-house.nl" + a["href"])

# Alleen mailen als er links zijn
if links:
    msg_content = "Nieuwe woningen gevonden:\n\n" + "\n".join(links[:5])
    message = MIMEText(msg_content)
    message["Subject"] = "Nieuwe woning op Your-House"
    message["From"] = EMAIL_FROM
    message["To"] = EMAIL_TO

    # Outlook SMTP verbinding
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()  # ← versleuteling
        server.login(EMAIL_FROM, EMAIL_PASS)  # ← login met secrets
        server.send_message(message)
