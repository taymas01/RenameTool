import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import pygame
import subprocess

def change_extensions():
    global total_files, changed_files
    folder_path = folder_path_var.get()
    new_extension = extension_var.get().strip()
    if not folder_path:
        messagebox.showwarning("Ошибка", "Сначала выберите папку.")
        return

    if not new_extension:
        messagebox.showwarning("Ошибка", "Введите новое расширение для файлов.")
        return

    files = os.listdir(folder_path)
    total_files = len(files)
    changed_files = 0

    progress_bar["maximum"] = total_files

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            new_file_path = file_path
            if not file.endswith(f".{new_extension}"):
                if "." in file:
                    base, _ = os.path.splitext(file_path)
                    new_file_path = base + f".{new_extension}"
                else:
                    new_file_path = file_path + f".{new_extension}"

                os.rename(file_path, new_file_path)
                changed_files += 1

        progress_bar["value"] += 1
        progress_label.config(text=f"Изменено: {changed_files} / {total_files}")
        root.update_idletasks()

    messagebox.showinfo("Готово", f"Процесс завершён! Изменено {changed_files} из {total_files} файлов.")

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)
    update_file_list()

def open_folder():
    folder_path = folder_path_var.get()
    if folder_path and os.path.isdir(folder_path):
        if os.name == "nt":  # Windows
            subprocess.Popen(f'explorer "{folder_path}"')
        else:  # macOS or Linux
            subprocess.Popen(["open" if os.name == "posix" else "xdg-open", folder_path])
    else:
        messagebox.showwarning("Ошибка", "Сначала выберите корректную папку.")

def update_file_list():
    folder_path = folder_path_var.get()
    file_listbox.delete(0, tk.END)
    if folder_path and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_listbox.insert(tk.END, file)

def update_fields(event):
    selected_file = file_listbox.get(tk.ACTIVE)
    if selected_file:
        folder_path = folder_path_var.get()
        file_path = os.path.join(folder_path, selected_file)
        if os.path.isfile(file_path):
            base_name = os.path.splitext(selected_file)[0]
            name_var.set(base_name)
            author_var.set("")
            display_file(file_path)

def apply_name_changes():
    selected_file = file_listbox.get(tk.ACTIVE)
    if not selected_file:
        messagebox.showwarning("Ошибка", "Сначала выберите файл.")
        return

    folder_path = folder_path_var.get()
    file_path = os.path.join(folder_path, selected_file)
    if not os.path.isfile(file_path):
        messagebox.showwarning("Ошибка", "Выбранный файл недействителен.")
        return

    new_name = name_var.get().strip()
    author = author_var.get().strip()
    if not new_name:
        messagebox.showwarning("Ошибка", "Введите название файла.")
        return

    new_file_name = f"{new_name} - {author}".strip(" -") + os.path.splitext(file_path)[1]
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(file_path, new_file_path)
    messagebox.showinfo("Готово", "Имя файла успешно изменено.")
    update_file_list()

def display_file(file_path):
    # Определяем тип файла и выполняем соответствующее действие
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".mp3", ".wav"]:
        play_audio(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        display_image(file_path)
    else:
        messagebox.showinfo("Информация", "Неподдерживаемый формат файла.")

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    messagebox.showinfo("Воспроизведение", "Музыка воспроизводится. Закройте это окно для остановки.")
    pygame.mixer.music.stop()

def display_image(file_path):
    try:
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось отобразить изображение: {e}")

# Создание главного окна
root = tk.Tk()
root.title("Изменение расширений файлов / Изменение имен музыки")
root.geometry("600x700")

# Переменные для хранения данных
folder_path_var = tk.StringVar()
extension_var = tk.StringVar()
name_var = tk.StringVar()
author_var = tk.StringVar()

# Поле для выбора папки
folder_frame = tk.Frame(root)
folder_frame.pack(pady=10)

folder_label = tk.Label(folder_frame, text="Папка:")
folder_label.pack(side=tk.LEFT, padx=5)

folder_entry = tk.Entry(folder_frame, textvariable=folder_path_var, width=40)
folder_entry.pack(side=tk.LEFT, padx=5)

folder_button = tk.Button(folder_frame, text="Выбрать", command=select_folder)
folder_button.pack(side=tk.LEFT, padx=5)

open_button = tk.Button(folder_frame, text="Открыть", command=open_folder)
open_button.pack(side=tk.LEFT, padx=5)

# Список файлов
file_listbox = tk.Listbox(root, height=10, width=60)
file_listbox.pack(pady=10)
file_listbox.bind("<<ListboxSelect>>", update_fields)

# Поле для ввода нового расширения
extension_frame = tk.Frame(root)
extension_frame.pack(pady=10)

extension_label = tk.Label(extension_frame, text="Новое расширение (без точки):")
extension_label.pack(side=tk.LEFT, padx=5)

extension_entry = tk.Entry(extension_frame, textvariable=extension_var, width=10)
extension_entry.pack(side=tk.LEFT, padx=5)

# Кнопки для изменения расширений
change_button = tk.Button(root, text="Изменить", command=change_extensions)
change_button.pack(pady=10)

# Поля для изменения имени и автора
name_frame = tk.Frame(root)
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="Название:")
name_label.pack(side=tk.LEFT, padx=5)

name_entry = tk.Entry(name_frame, textvariable=name_var, width=20)
name_entry.pack(side=tk.LEFT, padx=5)

author_label = tk.Label(name_frame, text="Автор:")
author_label.pack(side=tk.LEFT, padx=5)

author_entry = tk.Entry(name_frame, textvariable=author_var, width=20)
author_entry.pack(side=tk.LEFT, padx=5)

apply_button = tk.Button(root, text="Применить изменения", command=apply_name_changes)
apply_button.pack(pady=10)

# Полоса прогресса
progress_bar = Progressbar(root, length=400, mode="determinate")
progress_bar.pack(pady=10)

# Метка для отображения количества изменённых файлов
progress_label = tk.Label(root, text="Изменено: 0 / 0")
progress_label.pack()

# Метка для отображения изображений
img_label = tk.Label(root)
img_label.pack(pady=10)

# Запуск главного цикла Tkinter
root.mainloop()
