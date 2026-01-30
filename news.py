import os
import requests


class NewsFeed:
    """
    Represents multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = os.environ["NEWS_KEY"]

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = (
            f"{self.base_url}"
            f"qInTitle={self.interest}&"
            f"from={self.from_date}&"
            f"to={self.to_date}&"
            f"sortBy=popularity&"
            f"language={self.language}&"
            f"apiKey={self.api_key}"
        )
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            articles = response.json().get("articles", [])[:10]
        except Exception as e:
            return f"<p>Error fetching news: {e}</p>"

        if not articles:
            return "<p>No news found.</p>"

        email_body = "<h2>Latest News</h2><ul>"
        for article in articles:
            title = article.get("title", "No title")
            url = article.get("url", "#")
            email_body += (
                f'<li style="margin-bottom:14px;">'
                f'<strong>{title}</strong><br>'
                f'<a href="{url}">{url}</a>'
                f'</li>'
            )
        email_body += "</ul>"
        return email_body