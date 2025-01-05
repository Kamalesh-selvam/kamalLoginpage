from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'kamal',
    'password': 'kamal975',
    'database': 'your_database_name'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to validate login
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return redirect(url_for('success'))
        else:
            return "Invalid login credentials, please try again."
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert into users table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
