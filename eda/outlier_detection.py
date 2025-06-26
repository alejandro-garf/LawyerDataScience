def flag_outliers(df):
    flagged = df[(df['rating'] < 2) | (df['reviews'] > df['reviews'].quantile(0.95))]
    return flagged
