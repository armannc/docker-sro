import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "secret"),
        dbname=os.environ.get("DB_NAME", "postgres"),
    )

@app.route("/")
def index():
    return "Akmurat Arman SIB-31: app is running. Data: /students"

@app.route("/students")
def students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students;")
    rows = [{"id": r[0], "name": r[1]} for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
