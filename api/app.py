from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__, static_folder="../web/static", template_folder="../web/templates")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="del49for",  # replace
        database="lawyers"
    )

@app.route("/")
def home():
    return render_template("index.html", lawyers=None)

@app.route("/search")
def search():
    state = request.args.get("state")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lawyer_data WHERE state = %s", (state.upper(),))
    lawyers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", lawyers=lawyers, state=state.upper())


if __name__ == "__main__":
    app.run(debug=True)
