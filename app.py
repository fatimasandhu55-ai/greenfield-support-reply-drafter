from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "tickets.db"


# Task 01 wala prompt function - yahi draft banayega
def generate_draft(ticket_text):
    # Ye tumhara Task 01 wala function hai, maine simple version rakha hai
    prompt = f"""You are a helpful support agent. Draft a polite, professional reply for this ticket:
    
Ticket: {ticket_text}
    
Reply:"""
    # Abhi ke liye rule-based draft, baad me AI se connect kar sakti ho
    draft = f"Hi, Thank you for contacting us. We have received your ticket: '{ticket_text}'. Our team is looking into it and will get back to you shortly with a solution. Thanks for your patience!"
    return draft

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  ticket_text TEXT NOT NULL,
                  draft_reply TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    draft = None
    ticket_text = ""
    if request.method == 'POST':
        ticket_text = request.form.get('ticket_text', '').strip()
        if not ticket_text:
            error = "Ticket text cannot be empty. Please paste a ticket."
        else:
            draft = generate_draft(ticket_text)
            # Save to SQLite
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute("INSERT INTO tickets (ticket_text, draft_reply) VALUES (?, ?)", (ticket_text, draft))
            conn.commit()
            conn.close()
    return render_template('index.html', error=error, draft=draft, ticket_text=ticket_text)

@app.route('/history')
def history():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM tickets ORDER BY id DESC")
    tickets = c.fetchall()
    conn.close()
    return render_template('history.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
