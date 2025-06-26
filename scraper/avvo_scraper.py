import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_avvo():
    url = "https://www.avvo.com/immigration-lawyer/ca/fullerton.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    listings = soup.select(".search-result")

    for item in listings:
        name = item.select_one(".v-card__name")
        rating = item.select_one(".avvo-rating")
        reviews = item.select_one(".review-count")
        location = item.select_one(".v-card__address")

        results.append({
            "name": name.get_text(strip=True) if name else None,
            "rating": rating.get_text(strip=True) if rating else None,
            "reviews": reviews.get_text(strip=True) if reviews else None,
            "location": location.get_text(strip=True) if location else None,
            "source": "Avvo"
        })

    return pd.DataFrame(results)

