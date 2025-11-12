from tkinter import Tk
from login_view import LoginView
from database import create_db

def main():
    # Crear base de datos si no existe
    create_db()

    # Iniciar ventana principal de login
    root = Tk() #Llama al módulo principal de tkinter
    app = LoginView(root) #Inicia la interfaz
    root.mainloop() #Bucle Constante que mantienen la interfaz abierta escuchando eventos

if __name__ == "__main__":
    main()
