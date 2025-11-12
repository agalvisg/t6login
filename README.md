# t6login
t6login - Sistema de Login y Registro con SQLite y Tkinter

Sistema de autenticación de usuarios con **Python**, **Tkinter** y **SQLite**.  
Incluye login, registro, manejo de menores de edad y usuarios bloqueados.

---

## 📂 Estructura del proyecto

t6login/
.venv/
img/
login.png
user.png
controller.py
database.py
exceptions.py
insert_user_test.py
inspect_db.py
login_view.py
register_view.py
main.py
users.db
users_dict.py
README.md

yaml
Copiar código

---

## 🔄 Flujo de la aplicación

```text
         +------------------+
         |    main.py       |
         | Crear DB si no   |
         | existe           |
         +--------+---------+
                  |
                  v
         +------------------+
         |   LoginView      |
         | Ingresar usuario |
         | o registrar      |
         +--------+---------+
                  |
   +--------------+----------------+
   |                               |
   v                               v
RegisterView                   AuthController.login
 |                             (valida usuario, password,
 |                             birthday, bloqueado)
 v                               |
Autologin                        v
                                  +------------------+
                                  | Ventana Principal|
                                  | Nombre en rojo   |
                                  +------------------+
🛠 Requisitos
Python 3.x

Tkinter (incluido)

Pillow: pip install pillow

🚀 Cómo ejecutar
bash
Copiar código
git clone https://github.com/alejandrogalvis/t6login.git
cd t6login
python main.py
🔐 Base de datos
SQLite: users.db

Tabla users:

Campo	Tipo	Descripción
id	INTEGER	PK, autoincrement
nickname	TEXT	Único
password	TEXT	Hasheada MD5
birthday	TEXT	YYYY-MM-DD
bloqueado	INTEGER	0 = activo, 1 = bloqueado

Edad calculada dinámicamente desde birthday.

Usuarios bloqueados pueden loguearse pero no acceder al contenido.

🧪 Scripts auxiliares
insert_user_test.py → insertar usuarios manualmente.

inspect_db.py → inspeccionar base de datos.

users_dict.py → migración de usuarios antiguos.



##DEBUUGS RECIENTES

12-11-2025

1. Antes no se podía registrar un nuevo usuario. 
Se reemplaza en controller.py: AuthController.register
Edad --> Birthday
2. Se hacen comentarios en el main --> qué hace el módulo Tkinter
3. Dentro de register:

cursor.execute(
                    "INSERT INTO users (nickname, password, birthday, bloqueado) VALUES (?, ?, ?, ?)",
                    (nickname, password_hash, birthday, 0)
                )
                conn.commit()
 estaba fuera del bucle while.
Se mete dentro del bucle.
Ahora soporta múltiples excepciones al crear usuario y no rompe la base de datos.

