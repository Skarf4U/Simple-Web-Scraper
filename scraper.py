import requests
from bs4 import BeautifulSoup
import smtplib
import time


# Random Website URL to Scrape:
URL = ''

headers = {
    "User-Agent": 'YOUR_USER_AGENT'}


def check_price():
    global converted_price

    exp_price = 0 # Change to whatever you want

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="DynamicHeading_productTitle").get_text()
    price = soup.find(id="ProductPrice_productPrice_PriceContainer").get_text()
    converted_price = float(price[-6:-1])

    if (converted_price > exp_price):
        send_mail()

    print(converted_price)
    print(title)


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    render_email = 'RENDER_EMAIL@gmail.com'
    render_pass = 'RENDER_EMAIL_PASSWORD'
    receiver_email = 'RECEIVER_EMAIL@gmail.com'

    server.login(render_email, render_pass)

    subject = "YOUR_SUBJECT"
    body = f"YOUR_BODY"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        render_email,
        receiver_email,
        msg
    )
    print('Hey, email has been sent!')

    server.quit()


while (True):
    check_price()
    time.sleep(60 * 60)
