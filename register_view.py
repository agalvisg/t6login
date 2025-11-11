from tkinter import *
from tkinter import messagebox
from controller import AuthController

class RegisterView:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro")
        self.master.geometry("400x300")

        Label(master, text="Usuario:").pack(pady=5)
        self.nickname_entry = Entry(master)
        self.nickname_entry.pack(pady=5)
        self.nickname_entry.focus()

        Label(master, text="Contraseña:").pack(pady=5)
        self.password_entry = Entry(master, show="*")
        self.password_entry.pack(pady=5)

        Label(master, text="Fecha de nacimiento (YYYY-MM-DD):").pack(pady=5)
        self.birthday_entry = Entry(master)
        self.birthday_entry.pack(pady=5)

        Button(master, text="Registrar", command=self.register).pack(pady=10)

    def register(self):
        nickname = self.nickname_entry.get()
        password = self.password_entry.get()
        birthday = self.birthday_entry.get()
        try:
            msg = AuthController.register(nickname, password, birthday)
            messagebox.showinfo("Éxito", msg)
            # Autologin
            user = AuthController.login(nickname, password)
            self.open_main_window(user)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_main_window(self, user):
        self.master.destroy()
        root = Tk()
        root.title("Ventana principal")
        Label(root, text=f"Bienvenido {user}", font=("Arial", 20)).pack(pady=50)
        root.mainloop()
