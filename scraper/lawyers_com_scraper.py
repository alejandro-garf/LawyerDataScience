import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_avvo():
    url = "https://www.lawyers.com/immigration/fullerton/california/law-firms/"
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    lawyers = []

    for profile in soup.select(".search-result"):
        name = profile.select_one(".v-card__name")
        rating = profile.select_one(".avvo-rating")
        reviews = profile.select_one(".review-count")
        location = profile.select_one(".v-card__address")

        lawyers.append({
            "name": name.text.strip() if name else None,
            "rating": rating.text.strip() if rating else None,
            "reviews": reviews.text.strip() if reviews else None,
            "location": location.text.strip() if location else None,
            "source": "Avvo"
        })

    return pd.DataFrame(lawyers)
