import sqlite3

def inspect_db():
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Mostrar las tablas existentes
        print("Tablas en la base de datos:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for t in tables:
            print(" -", t[0])
        print()

        # Si existe la tabla users, mostrar su contenido
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        if cursor.fetchone():
            print("Contenido de la tabla 'users':")
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("(La tabla está vacía)")
        else:
            print("La tabla 'users' no existe aún.")

        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    inspect_db()
