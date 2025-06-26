# main.py
from scraper.avvo_scraper import scrape_avvo
from scraper.lawyers_com_scraper import scrape_lawyers
from data.cleaning import clean_data
from db.save_to_mysql import save_to_mysql
from eda.plot_ratings import plot_ratings
from eda.outlier_detection import flag_outliers

def main():
    df_avvo = scrape_avvo()
    df_lawyers = scrape_lawyers()
    df = clean_data(df_avvo.append(df_lawyers, ignore_index=True))
    save_to_mysql(df)
    plot_ratings(df)
    flagged = flag_outliers(df)
    print(flagged)

if __name__ == "__main__":
    main()
