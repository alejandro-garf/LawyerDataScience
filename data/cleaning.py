def clean_data(df):
    df['reviews'] = df['reviews'].str.extract(r'(\d+)').astype(float)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df = df.dropna(subset=['name'])
    return df
