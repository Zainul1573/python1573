from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Demo login check
        if username == "admin" and password == "1234":
            return "Login Successful"
        else:
            return "Invalid Login"

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
