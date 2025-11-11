from tkinter import Tk
from login_view import LoginView
from database import create_db

def main():
    # Crear base de datos si no existe
    create_db()

    # Iniciar ventana principal de login
    root = Tk()
    app = LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
