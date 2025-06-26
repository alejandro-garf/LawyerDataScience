import mysql.connector
import pandas as pd

def save_to_mysql(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="del49for",  # 🔁 Replace with your password
        database="lawyers"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lawyer_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            organization VARCHAR(255),
            location TEXT,
            state VARCHAR(10),
            is_pro_bono BOOLEAN,
            wage_estimate FLOAT,
            source VARCHAR(100)
        );
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO lawyer_data (
                name, organization, location, state,
                is_pro_bono, wage_estimate, source
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['name'] if pd.notna(row['name']) else None,
            row['organization'] if pd.notna(row['organization']) else None,
            row['location'] if pd.notna(row['location']) else None,
            row['state'] if pd.notna(row['state']) else None,
            bool(row['is_pro_bono']) if pd.notna(row['is_pro_bono']) else None,
            float(row['wage_estimate']) if pd.notna(row['wage_estimate']) else None,
            row['source'] if pd.notna(row['source']) else None
    ))


    conn.commit()
    cursor.close()
    conn.close()
