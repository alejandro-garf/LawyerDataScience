from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="del49for",  # 🔁 Replace with your MySQL password
        database="lawyers"
    )

@app.route("/lawyers", methods=["GET"])
def get_lawyers():
    state = request.args.get("state")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if state:
        cursor.execute("SELECT * FROM lawyer_data WHERE state = %s", (state,))
    else:
        cursor.execute("SELECT * FROM lawyer_data")

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route("/")
def home():
    return "✅ EOIR Lawyer API is running. Use /lawyers or /lawyers?state=CA"

if __name__ == "__main__":
    app.run(debug=True)
