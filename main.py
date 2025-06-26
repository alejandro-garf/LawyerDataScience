from data.eoir_scraper import load_eoir_csv
from db.save_to_mysql import save_to_mysql
import pandas as pd

def main():
    df = load_eoir_csv()  # parses local CSV from EOIR PDF
    print("EOIR sample:\n", df.head())

    # Add wage estimate column
    wage_df = pd.read_csv("data/wage_data.csv")  # state, wage
    df = df.merge(wage_df, on="state", how="left")

    save_to_mysql(df)
    print("✅ Data loaded into MySQL.")

if __name__ == "__main__":
    main()
