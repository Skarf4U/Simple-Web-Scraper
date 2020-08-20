import smtplib


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    render_email_input = input("Please enter the sender Email: ") # 'adiamar2005@gmail.com'
    render_pass_input = input("Please enter the sender Email Password: ") # 'AmarAdi20051912'
    reveiver_email_input = input("Please enter the receiver Email: ") # 'skarf.business@gmail.com'
    email_title = input("Please enter the Email Title: ")
    email_body = input("Please enter the Email Body Text: ")

    render_email = render_email_input
    render_pass = render_pass_input
    receiver_email = reveiver_email_input

    server.login(render_email, render_pass)

    subject = email_title
    body = email_body
    msg = f"{subject}\n\n{body}"

    server.sendmail(
        render_email,
        receiver_email,
        msg
    )
    print('Email has been sent!')

    server.quit()

send_mail()