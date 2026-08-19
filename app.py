from flask import Flask, request
import sqlite3

app = Flask(__name__)

GITHUB_PERSONAL_TOKEN = "ghp_18weufuer6efdjdffjkdhyttgdhguZ"

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'superuser')")
    conn.commit()
    conn.close()

@app.route('/user')
def get_user():
    username = request.args.get('username', '')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str(result)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
