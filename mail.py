from datetime import datetime
import random
import smtplib
import pandas as pd

USER_EMAIL = "roxana.roxolana.py@gmail.com"
PASSW = "rcaa tqmb kreu lumt"
NAME_FIELD = '[NAME]'

today_tuple = (datetime.now().day, datetime.now().month)
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


def send_email(to_obj):
    msg_letter_path = f'letter_templates/{random.choice(letters)}'
    with open(msg_letter_path) as msg_template:
        msg = msg_template.read()
        msg = msg.replace(NAME_FIELD, to_obj["name"])
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=USER_EMAIL, password=PASSW)
    connection.sendmail(from_addr=USER_EMAIL,
                        to_addrs=to_obj["email"],
                        msg=f"Subject:Happy birthday!\n\n{msg}"
                        )
    connection.close()


birthdays_df = pd.read_csv("birthdays.csv")

birthdays = {(row["day"], row["month"]): row for i, row in birthdays_df.iterrows()}
if today_tuple in birthdays:
    send_email(birthdays[today_tuple])

