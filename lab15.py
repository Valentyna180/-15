import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

# 12. Функція створення нового файлу
def new_file():
    text_area.delete(1.0, tk.END)

# 14. Відкрити файл
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# 16. Зберегти файл
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

# 18. Вийти

def exit_app():
    root.quit()

# 19. Зміна кольору тексту і фону

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

def change_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(bg=color)

# 21. Операції з буфером обміну

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

# 23. Довідка

def show_about():
    messagebox.showinfo("Про програму", "Це простий текстовий редактор на tkinter")

def show_help():
    messagebox.showinfo("Про автора", "Автор: Стаськова Валентина")

#Контекстне меню

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

#Головне вікно
root = tk.Tk()
root.title("Текстовий редактор")
root.geometry("600x400")

#Головне меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#Текстова область
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

#Пункт меню Файл
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

#Пункт меню Редагувати
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Редагувати", menu=edit_menu)

#Пункт меню Формат
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Формат", menu=format_menu)

#Пункт меню Довідка
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Довідка", menu=help_menu)

file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)

format_menu.add_command(label="Колір тексту", command=change_text_color)
format_menu.add_command(label="Колір фону", command=change_background_color)

edit_menu.add_command(label="Вирізати", command=cut_text)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)

help_menu.add_command(label="Про програму", command=show_about)
help_menu.add_command(label="Про автора", command=show_help)

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Колір тексту", command=change_text_color)
context_menu.add_command(label="Колір фону", command=change_background_color)
context_menu.add_command(label="Зберегти", command=save_file)

text_area.bind("<Button-3>", show_context_menu)

root.mainloop()
