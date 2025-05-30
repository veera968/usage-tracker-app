# usage_tracker_backend.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)
DB_FILE = 'usage_tracker.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            action TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/track', methods=['POST'])
def track_usage():
    data = request.json
    user_id = data.get('user_id')
    action = data.get('action')
    timestamp = datetime.utcnow().isoformat()

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO usage (user_id, action, timestamp) VALUES (?, ?, ?)',
              (user_id, action, timestamp))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 201

@app.route('/usage', methods=['GET'])
def get_usage():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT user_id, action, timestamp FROM usage ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    usage = [{'user_id': r[0], 'action': r[1], 'timestamp': r[2]} for r in rows]
    return jsonify(usage)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)