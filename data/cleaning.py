import pandas as pd

def clean_data(df):
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['reviews'] = df['reviews'].str.extract(r'(\d+)').astype(float)
    df = df.dropna(subset=['name', 'rating'])
    return df
