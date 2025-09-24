from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("reviews.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    review TEXT,
                    stars INTEGER)''')
    conn.commit()
    conn.close()


@app.route('/', methods=["GET", "POST"])
def home():
    conn = sqlite3.connect('reviews.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    if request.method == "POST": 
        name = request.form["name"]
        review = request.form["review"]
        stars = request.form.get("stars")  
        c.execute("INSERT INTO reviews (name, review, stars) VALUES (?, ?, ?)",
                  (name, review, stars))
        conn.commit()
        conn.close()
        return redirect("/")  

    c.execute("SELECT id, name, review, stars FROM reviews ORDER BY id DESC")
    reviews = c.fetchall()
    conn.close()

    return render_template("index.html", reviews=reviews)
    
    if __name__ == '__main__':
        init_db()
        app.run(host='0.0.0.0',debug=True)



