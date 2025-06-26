import pandas as pd
from scraper.avvo_scraper import scrape_avvo
from scraper.lawyers_com_scraper import scrape_lawyers
from data.cleaning import clean_data
from db.save_to_mysql import save_to_mysql
from eda.plot_ratings import plot_ratings
from eda.outlier_detection import flag_outliers

def main():
    avvo = scrape_avvo()
    lawyers_com = scrape_lawyers()
    merged = pd.concat([avvo, lawyers_com], ignore_index=True)
    clean = clean_data(merged)
    save_to_mysql(clean)
    plot_ratings(clean)
    outliers = flag_outliers(clean)
    print("Flagged Outliers:\n", outliers)

if __name__ == "__main__":
    main()
