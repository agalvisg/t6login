from datetime import datetime
import sqlite3
import hashlib
from exceptions import UsuarioBloqueado, UsuarioMenorEdad, UsuarioInexistente, UsuarioDuplicado,ContrasenaIncorrecta

class AuthController:
    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode()).hexdigest()

    @staticmethod
    def calculate_age(birthday_str):
        birth_date = datetime.strptime(birthday_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    @staticmethod
    def login(nickname, password):
        with sqlite3.connect('users.db') as conn:

            cursor = conn.cursor()

            cursor.execute("SELECT nickname, password, birthday, bloqueado FROM users WHERE nickname = ?",
                           (nickname,)
            )
            row = cursor.fetchone()


        #Validar existencia de usuario
        if not row:
            raise UsuarioInexistente("El usuario no existe")


        db_user, db_password, db_birthday, db_bloqueado = row

        #validar contraseña
        if db_password != AuthController.hash_password(password):
            raise ContrasenaIncorrecta("Contraseña incorrecta")

        #excepciones

        if AuthController.calculate_age(db_birthday) < 18:
            raise UsuarioMenorEdad("El usuario es menor de edad")

        if db_bloqueado ==1:
            raise UsuarioBloqueado("El usuario está bloqueado, hacer Bizum a dueño del programa")

        return db_user #login exitoso

    @staticmethod
    def register(nickname, password, birthday):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        password_hash = AuthController.hash_password(password)

        try:
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (nickname, password, birthday, bloqueado) VALUES (?, ?, ?, ?)",
                    (nickname, password_hash, birthday, 0)
                )
                conn.commit()
        except sqlite3.IntegrityError:
            raise UsuarioDuplicado("el nickname ya existe")

        return "Usuario registrado correctamente"