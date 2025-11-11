from tkinter import *
from tkinter import messagebox
from controller import AuthController
from exceptions import UsuarioBloqueado, UsuarioMenorEdad, UsuarioInexistente, ContrasenaIncorrecta

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x250")

        Label(master, text="Usuario:").pack(pady=5)
        self.nickname_entry = Entry(master)
        self.nickname_entry.pack(pady=5)
        self.nickname_entry.focus()

        Label(master, text="Contraseña:").pack(pady=5)
        self.password_entry = Entry(master, show="*")
        self.password_entry.pack(pady=5)

        Button(master, text="Iniciar sesión", command=self.login).pack(pady=10)
        Button(master, text="Registrar nuevo usuario", command=self.open_register).pack(pady=5)

    def login(self):
        nickname = self.nickname_entry.get()
        password = self.password_entry.get()
        try:
            user = AuthController.login(nickname, password)
            messagebox.showinfo("Éxito", f"Bienvenido {user}")
            self.open_main_window(user)
        except UsuarioInexistente:
            messagebox.showerror("Error", "El usuario no existe")
        except ContrasenaIncorrecta:
            messagebox.showerror("Error", "Contraseña incorrecta")
        except UsuarioMenorEdad:
            messagebox.showerror("Error", "Usuario menor de edad")
        except UsuarioBloqueado:
            messagebox.showerror("Error", "Usuario bloqueado")

    def open_register(self):
        self.master.destroy()
        from register_view import RegisterView
        root = Tk()
        RegisterView(root)
        root.mainloop()

    def open_main_window(self, user):
        self.master.destroy()
        root = Tk()
        root.title("Ventana principal")
        Label(root, text=f"Bienvenido {user}", font=("Arial", 20)).pack(pady=50)
        root.mainloop()
