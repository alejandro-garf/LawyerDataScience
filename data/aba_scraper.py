import pdfplumber
import pandas as pd

def load_eoir_pdf(path="data/eoir_pro_bono.pdf"):
    all_rows = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    all_rows.append(row)

    # Convert to DataFrame and clean up
    df = pd.DataFrame(all_rows)

    # Drop rows where most values are None
    df = df.dropna(thresh=3)

    # Try to guess header if not present
    df.columns = ["name", "organization", "location", "state", "phone", "email", "other"]

    df["is_pro_bono"] = True
    df["wage_estimate"] = None
    df["source"] = "EOIR"

    return df[["name", "organization", "location", "state", "is_pro_bono", "wage_estimate", "source"]]
