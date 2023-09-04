from flask import Flask, render_template, request, redirect, url_for, flash, session
import random

app = Flask(__name__)
app.secret_key = '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'

users = []

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    user = {'username': username, 'email': email, 'password': password}
    users.append(user)
    flash('Registration successful. You can now log in.')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    for user in users:
        if user['email'] == email and user['password'] == password:
            session['user'] = user
            return redirect(url_for('dashboard'))
    flash('Login failed. Please check your email and password.')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/find_ride')
def find_ride():
    if 'user' not in session:
        return redirect(url_for('index'))
    available_rides = [
        {'driver': 'Driver 1', 'origin': 'Origin 1', 'destination': 'Destination 1'},
        {'driver': 'Driver 2', 'origin': 'Origin 2', 'destination': 'Destination 2'},
    ]
    return render_template('find_ride.html', user=session['user'], rides=available_rides)

if __name__ == '__main__':
    app.run(debug=True)
