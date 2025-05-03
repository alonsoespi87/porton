import sqlite3

def get_menu():
    conn = sqlite3.connect("data/menu.db")
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM menu")
    results = cur.fetchall()
    conn.close()
    return results
