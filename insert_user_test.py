import sqlite3
import hashlib

#conectar a la BBDD

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

#datos del usuario de prueba
nickname = "alejandro"
password = "1234"
edad = 23
bloqueado = 0

#Hashear la pswdd
password_hash = hashlib.md5(password.encode()).hexdigest()

#Insertar
cursor.execute(
    "INSERT INTO users (nickname, password, edad, bloqueado) VALUES (?, ?, ?, ?)",
    (nickname, password_hash, edad, bloqueado)
)
conn.commit()
conn.close()

print("Usuario creado exitosamente")

