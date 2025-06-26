import os
import pandas as pd
from data.eoir_scraper import load_eoir_pdf
from db.save_to_mysql import save_to_mysql

def main():
    if os.path.exists("data/parsed_eoir_lawyers.csv"):
        print("⚡ Loading cached lawyer data from CSV...")
        df = pd.read_csv("data/parsed_eoir_lawyers.csv")
    else:
        print("📥 Extracting EOIR lawyer data from PDF...")
        df = load_eoir_pdf()
        df.to_csv("data/parsed_eoir_lawyers.csv", index=False)
        print("📝 Saved parsed data to cache: parsed_eoir_lawyers.csv")

    print(f"📊 Loaded {len(df)} entries.")
    print("📦 Saving to MySQL...")
    save_to_mysql(df)
    print("✅ Done.")

if __name__ == "__main__":
    main()
