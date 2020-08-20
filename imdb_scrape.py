import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.imdb.com/'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for title in soup.findAll(class_="ipc-poster-card__title"):
        print(title.text)
    for rating in soup.findAll(class_="ipc-rating-star"):
        print(rating.text)
        return str(rating.text)
        rating + rating
    print(f"Rating sum is {rating}")


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    render_email = 'adiamar2005@gmail.com'
    render_pass = 'AmarAdi19122005'
    receiver_email = 'skarf.business@gmail.com'

    server.login(render_email, render_pass)

    subject = "IMDB Movies Rating"
    body = f"Check out IMDB's website: {URL}"
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