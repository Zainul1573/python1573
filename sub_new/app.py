from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("subagents.db")

@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sub_agents")
    agents = cursor.fetchall()
    conn.close()
    return render_template("index.html", agents=agents)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sub_agents (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
