from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def read_csv(filename):
    users = {}
    with open(filename, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            users[username] = password
    return users

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    users = read_csv('passwords.csv')
    
    if username in users and users[username] == password:
        return f"Login successful! Welcome, {username}."
    else:
        return render_template('login.html', error='Invalid username or password')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)