import mysql.connector

def save_to_mysql(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="del49for",  
        database="lawyers"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lawyer_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            rating FLOAT,
            reviews INT,
            location TEXT,
            source VARCHAR(50)
        );
    """)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO lawyer_data (name, rating, reviews, location, source)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['name'], row['rating'], row['reviews'], row['location'], row['source']))

    conn.commit()
    cursor.close()
    conn.close()
