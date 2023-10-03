# Web Scraper
A simple web scraper that checks whenever the price of a random game has gone down to less than $**_x_**.
I was using 3 libraries for the main system, **requests**, **BeautifulSoup** & **smtplib**.

# Instructions
- Choose the site you wish to get the product price of and past the URL in line **8**.
- Get your **User-Agent**. If you don't know how to get it, simply google "*My User-Agent*".
- Paste the outcome of your search into line **11** (```'YOUR_USER_AGENT'```).
- Get the **Product Title Tag ID** and the **Product Price Tag ID** by inspecting elemetns.
- Paste the Product Title Tag ID in line **22** (```id="PRODUCT_TITLE_TAG_ID"```).
- Paste the Product Price Tag ID in line **23** (```id="PRODUCT_PRICE_TAG_ID"```).
- Go over the code and change the **Render Email & Passowrd** and the **Receiver Email**.
- Edit the **subject**, **body** & the **msg* as you wish.


Run: ```python scraper.py```
