from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/lawyers')
def get_lawyers():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="del49for",
        database="lawyers"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lawyer_data")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
