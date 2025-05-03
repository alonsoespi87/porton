import sqlite3
from config import MENU_DB_PATH

def init_menu_db():
    connection = sqlite3.connect(MENU_DB_PATH)
    cursor = connection.cursor()

    # Crear tabla de menú
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
    """)

    # Insertar algunos productos de ejemplo
    items = [
        ("Café americano", 25.0),
        ("Capuchino", 35.0),
        ("Latte", 30.0),
        ("Té chai", 28.0),
        ("Pan dulce", 15.0)
    ]

    cursor.executemany("INSERT INTO menu (name, price) VALUES (?, ?);", items)
    connection.commit()
    connection.close()
    print("Base de datos 'menu.db' inicializada correctamente.")

if __name__ == "__main__":
    init_menu_db()
