import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
my_email = "yoshijoshio@gmail.com"
password = "yvuaezmoxgimainh"


if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Weekly Motivation\n\n{quote}."
        )
