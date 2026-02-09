from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("subagents.db")


# READ - List agents
@app.route("/")
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sub_agents")
    agents = cursor.fetchall()
    conn.close()
    return render_template("index.html", agents=agents)


# CREATE - Add agent
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sub_agents (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect("/")


# DELETE agent
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sub_agents WHERE sl_no=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


# UPDATE agent
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        cursor.execute(
            "UPDATE sub_agents SET name=? WHERE sl_no=?",
            (name, id),
        )
        conn.commit()
        conn.close()
        return redirect("/")

    cursor.execute("SELECT * FROM sub_agents WHERE sl_no=?", (id,))
    agent = cursor.fetchone()
    conn.close()
    return render_template("edit.html", agent=agent)


if __name__ == "__main__":
    app.run(debug=True)
