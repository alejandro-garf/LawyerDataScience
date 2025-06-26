import mysql.connector

def save_to_mysql(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",  # 🔁 Replace with your password
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
            row['name'],
            row['organization'],
            row['location'],
            row['state'],
            bool(row['is_pro_bono']),
            row['wage_estimate'],
            row['source']
        ))

    conn.commit()
    cursor.close()
    conn.close()
