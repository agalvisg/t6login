import sqlite3

def create_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()

    cursor.execute( """
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT UNIQUE,
            password TEXT NOT NULL,
            birthday TEXT NOT NULL,
            bloqueado INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    print("La base de datos y tabla 'users' han sido creados exitosamente")

if __name__ == '__main__':
    create_db()
