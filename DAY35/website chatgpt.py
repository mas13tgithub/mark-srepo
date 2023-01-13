from flask import Flask, render_template, request, redirect, session
import hashlib

app = Flask(__name__)
app.secret_key = "mysecretkey"

# hardcoded users for demonstration purposes
users = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest()
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', error=True)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # check if the username is already taken
        if username in users:
            return render_template('register.html', error="Username already taken")
        # validate the password
        if len(password) < 8:
            return render_template('register.html', error="Password must be at least 8 characters long")
        # hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # add the new user to the users dictionary
        users[username] = hashed_password
        return redirect('/login')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)