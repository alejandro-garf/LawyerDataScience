import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_lawyers():
    url = "https://www.lawyers.com/immigration/fullerton/california/law-firms/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    listings = soup.select(".law-firm-card")

    for item in listings:
        name = item.select_one(".law-firm-name")
        reviews = item.select_one(".star-rating-review-count")
        rating = item.select_one(".star-rating-stars")
        location = item.select_one(".locality")

        results.append({
            "name": name.get_text(strip=True) if name else None,
            "rating": rating.get("data-rating") if rating else None,
            "reviews": reviews.get_text(strip=True) if reviews else None,
            "location": location.get_text(strip=True) if location else None,
            "source": "Lawyers.com"
        })

    return pd.DataFrame(results)
