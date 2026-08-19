from flask import Flask, request
import sqlite3

app = Flask(__name__)

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "supersecretpassword123!"

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
