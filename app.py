from flask import Flask, request, jsonify
import sqlite3
import configs

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("notmot.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/notmot/addNote", methods=["POST"])
def add_note():
    username = request.form.get("username")
    password = request.form.get("password")
    data = request.form.get("data")

    if username in configs.users and password == configs.users[username]:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO nots (note) VALUES (?)", (data,))
        conn.commit()
        note_id = cursor.lastrowid
        conn.close()

        return jsonify({"status": "added", "id": note_id}), 201
    else:
        return jsonify({"error": "your username or password is incorrect"}), 403





@app.route("/notmot/delNote", methods=["POST"])
def del_note():
    username = request.form.get("username")
    password = request.form.get("password")
    note_id = request.form.get("id")

    if username in configs.users and password == configs.users[username]:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM nots WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()

        return jsonify({"status": "deleted", "id": note_id}), 200
    else:
        return jsonify({"error": "your username or password is incorrect"}), 403





@app.route("/notmot/listNote", methods=["POST"])
def list_note():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in configs.users and password == configs.users[username]:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nots")
        notes = cursor.fetchall()
        conn.close()

        return jsonify([dict(note) for note in notes]), 200
    else:
        return jsonify({"error": "your username or password is incorrect"}), 403

if __name__ == "__main__":
    with get_db_connection() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS nots (id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT)")
    app.run(debug=True, host="localhost", port=4444)
