def flag_outliers(df):
    high_cost = df[df['rating'] < 2]
    high_reviews = df[df['reviews'] > df['reviews'].quantile(0.95)]
    return pd.concat([high_cost, high_reviews]).drop_duplicates()
