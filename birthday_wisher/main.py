    `##################### Normal Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

today = dt.datetime.now()
today_tuple = (today.month, today.day)
my_email = "yoshijoshio@gmail.com"
password = "yvuaezmoxgimainh"
data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy Birthday!!!\n\n{contents}."
        )


