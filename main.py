##################### Extra Hard Starting Project ######################
import datetime as dt
from random import *
import smtplib
import pandas

# Records created to store birthday information
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# Email login
USERNAME = ("clarenceswag1@gmail.com")
PASSWORD = "Fill in"

# Current date
now = dt.datetime.now()
today_date = (now.day, now.month, now.year)

# Check if today's date matches birthday
for birthday in birthdays:
    if birthday["day"] == today_date[0] and birthday["month"] == today_date[1]:

        # Letter randomly chosen and formatted with receivers names
        file_path = f"letter_templates/letter_{randint(1,3)}.txt"
        with open(file_path) as letter_file:
            letter = letter_file.read()
            letter.replace("[NAME]", birthday["name"])

        # Email sent
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=birthday["email"],
                msg=f"Subject: Happy {today_date[2] - birthday["year"]}th\n\n{letter}")





