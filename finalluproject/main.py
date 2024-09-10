import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class AdminFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#f0f0f0")

        self.logo_image = Image.open("я волонтер.jpg")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image.resize((100, 100)))
        self.logo_label = tk.Label(self, image=self.logo_photo, bg="#f0f0f0")
        self.logo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.show_projects_button = tk.Button(self, text="Показать проекты", command=self.show_projects, bg="#4CAF50", fg="#ffffff")
        self.show_projects_button.grid(row=1, column=0, padx=10, pady=10)

        self.add_project_button = tk.Button(self, text="Добавить проект", command=self.add_project, bg="#4CAF50", fg="#ffffff")
        self.add_project_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_project_button = tk.Button(self, text="Удалить проект", command=self.delete_project, bg="#f44336", fg="#ffffff")
        self.delete_project_button.grid(row=3, column=0, padx=10, pady=10)

        self.edit_project_button = tk.Button(self, text="Редактировать проект", command=self.edit_project, bg="#FFC107", fg="#ffffff")
        self.edit_project_button.grid(row=4, column=0, padx=10, pady=10)

        self.search_project_button = tk.Button(self, text="Поиск проекта", command=self.search_project, bg="#2196F3", fg="#ffffff")
        self.search_project_button.grid(row=5, column=0, padx=10, pady=10)

        self.sort_projects_button = tk.Button(self, text="Сортировать проекты", command=self.sort_projects, bg="#9C27B0", fg="#ffffff")
        self.sort_projects_button.grid(row=6, column=0, padx=10, pady=10)

        self.back_button = tk.Button(self, text="Назад", command=self.parent.back_to_login, bg="#f44336", fg="#ffffff")
        self.back_button.grid(row=7, column=0, padx=10, pady=10)

        self.logout_button = tk.Button(self, text="Выход из системы", command=self.parent.quit, bg="#f44336",
                                       fg="#ffffff")
        self.logout_button.grid(row=8, column=0, padx=10, pady=10)

    def show_projects(self):
        try:
            with open("projects.txt", "r") as file:
                projects = file.readlines()
            projects = [p.strip() for p in projects]
            if not projects:
                messagebox.showinfo("Проекты", "Нет доступных проектов.")
            else:
                messagebox.showinfo("Проекты", "\n".join(projects))
        except FileNotFoundError:
            messagebox.showinfo("Проекты", "Нет доступных проектов.")

    def add_project(self):
        project_name = simpledialog.askstring("Название проекта", "Введите название проекта:")
        if project_name:
            with open("projects.txt", "a") as file:
                file.write(f"{project_name}\n")
            messagebox.showinfo("Добавление проекта", "Проект успешно добавлен.")

    def delete_project(self):
        project_name = simpledialog.askstring("Удаление проекта", "Введите название проекта для удаления:")
        if project_name:
            try:
                with open("projects.txt", "r") as file:
                    projects = file.readlines()
                projects = [p.strip() for p in projects if p.strip() != project_name]
                with open("projects.txt", "w") as file:
                    file.write("\n".join(projects))
                messagebox.showinfo("Удаление проекта", "Проект успешно удален.")
            except FileNotFoundError:
                messagebox.showinfo("Удаление проекта", "Файл с проектами не найден.")

    def edit_project(self):
        old_name = simpledialog.askstring("Редактирование проекта", "Введите текущее название проекта:")
        if old_name:
            new_name = simpledialog.askstring("Редактирование проекта", "Введите новое название проекта:")
            if new_name:
                try:
                    with open("projects.txt", "r") as file:
                        projects = file.readlines()
                    projects = [new_name if p.strip() == old_name else p.strip() for p in projects]
                    with open("projects.txt", "w") as file:
                        file.write("\n".join(projects))
                    messagebox.showinfo("Редактирование проекта", "Проект успешно отредактирован.")
                except FileNotFoundError:
                    messagebox.showinfo("Редактирование проекта", "Файл с проектами не найден.")

    def search_project(self):
        search_term = simpledialog.askstring("Поиск проекта", "Введите название проекта для поиска:")
        if search_term:
            try:
                with open("projects.txt", "r") as file:
                    projects = file.readlines()
                projects = [p.strip() for p in projects]
                results = [p for p in projects if search_term.lower() in p.lower()]
                if results:
                    messagebox.showinfo("Результаты поиска", "\n".join(results))
                else:
                    messagebox.showinfo("Поиск проекта", "Проект не найден.")
            except FileNotFoundError:
                messagebox.showinfo("Поиск проекта", "Файл с проектами не найден.")

    def sort_projects(self):
        try:
            with open("projects.txt", "r") as file:
                projects = file.readlines()
            projects = [p.strip() for p in projects]
            projects.sort()
            with open("projects.txt", "w") as file:
                file.write("\n".join(projects))
            messagebox.showinfo("Сортировка проектов", "Проекты успешно отсортированы.")
        except FileNotFoundError:
            messagebox.showinfo("Сортировка проектов", "Файл с проектами не найден.")

class UserFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#f0f0f0")

        self.logo_image = Image.open("я волонтер.jpg")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image.resize((100, 100)))
        self.logo_label = tk.Label(self, image=self.logo_photo, bg="#f0f0f0")
        self.logo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.view_projects_button = tk.Button(self, text="Просмотр проектов", command=self.view_projects, bg="#4CAF50", fg="#ffffff")
        self.view_projects_button.grid(row=1, column=0, padx=10, pady=10)

        self.back_button = tk.Button(self, text="Назад", command=self.parent.back_to_login, bg="#f44336", fg="#ffffff")
        self.back_button.grid(row=2, column=0, padx=10, pady=10)

        self.logout_button = tk.Button(self, text="Выход из системы", command=self.parent.quit, bg="#f44336",
                                       fg="#ffffff")
        self.logout_button.grid(row=3, column=0, padx=10, pady=10)

    def add_project(self):
        project_name = simpledialog.askstring("Название проекта", "Введите название проекта:")
        if project_name:
            with open("projects.txt", "a") as file:
                file.write(f"{project_name}\n")
            messagebox.showinfo("Добавление проекта", "Проект успешно добавлен.")
    def view_projects(self):
        try:
            with open("projects.txt", "r") as file:
                projects = file.readlines()
            projects = [p.strip() for p in projects]
            if not projects:
                messagebox.showinfo("Проекты", "Нет доступных проектов.")
            else:
                messagebox.showinfo("Проекты", "\n".join(projects))
        except FileNotFoundError:
            messagebox.showinfo("Проекты", "Нет доступных проектов.")

class RegistrationFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#f0f0f0")

        self.logo_image = Image.open("я волонтер.jpg")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image.resize((100, 100)))
        self.logo_label = tk.Label(self, image=self.logo_photo, bg="#f0f0f0")
        self.logo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.username_label = tk.Label(self, text="Логин:", bg="#f0f0f0")
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self, text="Пароль:", bg="#f0f0f0")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Показать пароль", variable=self.show_password_var,
                                                     command=self.toggle_password_visibility, bg="#f0f0f0")
        self.show_password_checkbox.grid(row=2, column=2, padx=10, pady=10)

        self.confirm_password_label = tk.Label(self, text="Подтверждение пароля:", bg="#f0f0f0")
        self.confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.email_label = tk.Label(self, text="Email:", bg="#f0f0f0")
        self.email_label.grid(row=4, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=1, padx=10, pady=10)

        self.register_button = tk.Button(self, text="Регистрация", command=self.register, bg="#4CAF50", fg="#ffffff")
        self.register_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        self.back_button = tk.Button(self, text="Назад", command=self.parent.show_login_frame, bg="#f44336", fg="#ffffff")
        self.back_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
            self.confirm_password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            self.confirm_password_entry.config(show="*")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        email = self.email_entry.get()

        if not username or not password or not confirm_password or not email:
            messagebox.showwarning("Регистрация", "Пожалуйста, заполните все поля.")
            return

        if password != confirm_password:
            messagebox.showwarning("Регистрация", "Пароли не совпадают.")
            return

        # Проверка наличия администратора
        try:
            with open("admin.txt", "r") as file:
                admin_data = file.readlines()
            admin_exists = any(email == line.split(",")[2].strip() for line in admin_data)
        except FileNotFoundError:
            admin_exists = False

        # Регистрация
        if not admin_exists:
            with open("users.txt", "a") as file:
                file.write(f"{username},{password},{email}\n")
            messagebox.showinfo("Регистрация", "Регистрация прошла успешно.")
            self.parent.show_login_frame()
        else:
            messagebox.showwarning("Регистрация", "Пользователь с таким email уже существует.")

class LoginFrame(tk.Frame):
    def __init__(self, parent, show_registration_frame_callback):
        super().__init__(parent)
        self.parent = parent
        self.show_registration_frame_callback = show_registration_frame_callback
        self.configure(bg="#f0f0f0")

        self.logo_image = Image.open("я волонтер.jpg")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image.resize((100, 100)))
        self.logo_label = tk.Label(self, image=self.logo_photo, bg="#f0f0f0")
        self.logo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.username_label = tk.Label(self, text="Логин:", bg="#f0f0f0")
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self, text="Пароль:", bg="#f0f0f0")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self, text="Показать пароль", variable=self.show_password_var,
                                                     command=self.toggle_password_visibility, bg="#f0f0f0")
        self.show_password_checkbox.grid(row=2, column=2, padx=10, pady=10)

        self.login_button = tk.Button(self, text="Войти", command=self.login, bg="#4CAF50", fg="#ffffff")
        self.login_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.register_button = tk.Button(self, text="Регистрация", command=self.show_registration_frame_callback, bg="#FFC107", fg="#ffffff")
        self.register_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Вход", "Пожалуйста, заполните все поля.")
            return

        # Проверка администратора
        try:
            with open("admin.txt", "r") as file:
                admin_data = file.readlines()
            admin_exists = any(username == line.split(",")[0].strip() and password == line.split(",")[1].strip() for line in admin_data)
        except FileNotFoundError:
            admin_exists = False

        # Проверка пользователя
        try:
            with open("users.txt", "r") as file:
                user_data = file.readlines()
            user_exists = any(username == line.split(",")[0].strip() and password == line.split(",")[1].strip() for line in user_data)
        except FileNotFoundError:
            user_exists = False

        if admin_exists:
            self.parent.show_admin_frame()
        elif user_exists:
            self.parent.show_user_frame()
        else:
            messagebox.showwarning("Вход", "Неверный логин или пароль.")

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Волонтерское приложение")
        self.geometry("400x300")
        self.iconbitmap("icon.ico")  # Устанавливаем иконку

        self.login_frame = LoginFrame(self, self.show_registration_frame)
        self.registration_frame = RegistrationFrame(self)
        self.admin_frame = AdminFrame(self)
        self.user_frame = UserFrame(self)

        self.show_login_frame()

    def show_login_frame(self):
        self.login_frame.pack(fill="both", expand=True)
        self.registration_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.user_frame.pack_forget()

    def show_registration_frame(self):
        self.login_frame.pack_forget()
        self.registration_frame.pack(fill="both", expand=True)
        self.admin_frame.pack_forget()
        self.user_frame.pack_forget()

    def show_admin_frame(self):
        self.login_frame.pack_forget()
        self.registration_frame.pack_forget()
        self.admin_frame.pack(fill="both", expand=True)
        self.user_frame.pack_forget()

    def show_user_frame(self):
        self.login_frame.pack_forget()
        self.registration_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.user_frame.pack(fill="both", expand=True)

    def back_to_login(self):
        self.login_frame.pack(fill="both", expand=True)
        self.registration_frame.pack_forget()
        self.admin_frame.pack_forget()
        self.user_frame.pack_forget()

app = MainApplication()
app.mainloop()