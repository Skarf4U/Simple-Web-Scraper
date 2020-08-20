import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.microsoft.com/en-il/p/lego-marvel-super-heroes-2/c0g91v37489h?activetab=pivot:overviewtab'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


def check_price():
    global converted_price

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="DynamicHeading_productTitle").get_text()
    price = soup.find(id="ProductPrice_productPrice_PriceContainer").get_text()
    converted_price = float(price[-6:-1])

    if (converted_price > 92.87):
        send_mail()

    print(converted_price)
    print(title)


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    render_email = 'adiamar2005@gmail.com'
    render_pass = 'AmarAdi19122005'
    receiver_email = 'skarf.business@gmail.com'

    server.login(render_email, render_pass)

    subject = "Price Fell Down!"
    body = f"The price of LEGO Marvel Super Heroes 2 is now {converted_price}.\nCheck out the game link if you would like to purchase: {URL}"
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