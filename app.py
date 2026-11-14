from flask import Flask, render_template, request
import sqlite3
# Task 1 wala function isi repo se le rahe hain
try:
    from main import draft_reply
except:
    from prompt_template import draft_reply

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("tickets.db")
    conn.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, ticket TEXT, draft TEXT)")
    conn.commit(); conn.close()
init_db()

@app.route("/", methods=["GET","POST"])
def index():
    error=None; draft=None; ticket_text=""
    if request.method=="POST":
        ticket_text=request.form.get("ticket","").strip()
        if not ticket_text:
            error="Ticket text khali hai, please likh ke submit karo."
        else:
            draft=draft_reply(ticket_text)
            conn=sqlite3.connect("tickets.db")
            conn.execute("INSERT INTO tickets (ticket,draft) VALUES (?,?)",(ticket_text,draft))
            conn.commit(); conn.close()
    return render_template("index.html", error=error, draft=draft, ticket=ticket_text)

@app.route("/history")
def history():
    conn=sqlite3.connect("tickets.db")
    conn.row_factory=sqlite3.Row
    rows=conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("history.html", rows=rows)

if __name__=="__main__":
    app.run(debug=True)
