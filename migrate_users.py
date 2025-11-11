"""
Este programa es para migrar datos de un diccionario a una BBDD
"""


import sqlite3
from controller import AuthController
from users_dict import users

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

for user in users:
    try:
        cursor.execute(
            "INSERT INTO users (nickname, password, birthday, bloqueado) VALUES (?, ?, ?, ?)",
            (
                user["nickname"],
                AuthController.hash_password(user["passw"]),
                user["birthday"],
                1 if user["blocked"] else 0
            )
        )
        print(f"Usuario {user['nickname']} insertado correctamente")
    except sqlite3.IntegrityError:
        print(f"Usuario {user['nickname']} ya existe, se saltó")

conn.commit()
conn.close()
print("Migración completa")
