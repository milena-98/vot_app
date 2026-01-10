from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

@app.route("/messages", methods=["GET"])
def get_messages():
    cur = conn.cursor()
    cur.execute("SELECT content FROM messages;")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.json
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (data["content"],))
    conn.commit()
    return {"status": "ok"}

app.run(host="0.0.0.0", port=5000)
