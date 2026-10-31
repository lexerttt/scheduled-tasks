# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import random
import datetime as dt
import pandas
import smtplib

now = dt.datetime.now()
now_month = now.month
now_day = now.day
today = (now_month, now_day)
birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day):index for (index, row) in birthdays.iterrows()}
print(birthday_dict)

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

if today in birthday_dict:
    birthday_index = birthday_dict[today]
    birthday_name = birthdays['name'][birthday_index]
    birthday_email = birthdays['email'][birthday_index]
    print(birthday_name)
    print(birthday_email)

    template_choice = random.randint(1,3)
    with open(f"letter_templates/letter_{template_choice}.txt", mode='r') as file:
        base_letter = file.read()
        birthday_letter = base_letter.replace("[NAME]", birthday_name)
        

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_email,
                            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}"
                            )
