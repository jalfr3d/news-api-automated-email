from datetime import date, timedelta
from news import NewsFeed
from send_email import send_email
import pandas as pd

to_date = date.today()
from_date = to_date - timedelta(days=1)

df = pd.read_excel("people.xlsx")
"""
people.xlsx format email | interest
"""
required_columns = {"email","interest"}
if not required_columns.issubset(df.columns):
    raise ValueError("XLSX must contain: email, interest")

for _, row in df.iterrows():
    email = row["email"]
    interest = row["interest"]

    print(f"Sending news about '{interest}' to {email}")

    news_feed = NewsFeed(
        interest=interest,
        from_date=from_date.isoformat(),
        to_date=to_date.isoformat(),
        language="en"
    )

    email_body = news_feed.get()

    subject = f"Daily {interest.upper()} News"

    send_email(
        text_subject=subject,
        email_body=email_body,
        receiver=email
    )




