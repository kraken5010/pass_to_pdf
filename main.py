from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk

# Налаштування вікна
root = tk.Tk()
root.title('Пароль на pdf файл')
root.geometry(f'420x400')
root.minsize(670, 400)
# win.config(bg='#2b2b2b')
photo = tk.PhotoImage(file='image/icon.png')
root.iconphoto(True, photo)


# Встановлення паролю
def encrypt_file(file_path, password, file_name):

    file_dir = file_path.split('/')[:-1]
    file_dir = '/'.join(file_dir)

    new_file_name = file_name

    if '.' in file_name:
        new_file_name = ''.join(file_name.split('.')[:-1])

    file_writer = PdfFileWriter()

    file_reader = PdfFileReader(file_path)

    for page in range(file_reader.numPages):
        file_writer.addPage(file_reader.getPage(page))

    file_writer.encrypt(password)

    with open(f'{file_dir}/{new_file_name}.pdf', "wb") as file:
        file_writer.write(file)

    messagebox.showinfo('Вітаю', "Пароль успішно встановленно!")


# Зняття паролю
def decrypt_file(file_path, password, file_name):

    new_file_name = file_name

    if '.' in file_name:
        new_file_name = ''.join(file_name.split('.')[:-1])

    file_writer = PdfFileWriter()
    file_reader = PdfFileReader(file_path)

    if file_reader.isEncrypted:
        file_reader.decrypt(password)

    for page in range(file_reader.numPages):
        file_writer.addPage(file_reader.getPage(page))

    with open(f'{new_file_name}.pdf', "wb") as file:
        file_writer.write(file)

    messagebox.showinfo('Вітаю', "Пароль успішно знято!")


def get_data():
    file_path = file_path_input.get()

    file_path_check = file_path.split('.')[-1]

    if file_path == '' or file_path_check != 'pdf':
        messagebox.showinfo('Увага', "Невірно вказаний файл!")

    password = password_input.get()
    if password == '':
        messagebox.showinfo('Увага', "Встановіть пароль!")
        password = None

    file_name = new_file_name_input.get()
    if file_name == '':
        messagebox.showinfo('Увага', "Введіть ім'я файлу!")

    else:
        action = action_text.get()
        if action == 'encrypt':
            encrypt_file(file_path, password, file_name)
        elif action == 'decrypt':
            decrypt_file(file_path, password, file_name)
        else:
            messagebox.showinfo('Увага', "Не вибрано дію!")


def choice_path():
    file = filedialog.askopenfilename()
    file_path_input.delete(0, tk.END)
    file_path_input.insert(0, file)


# Текст з підказками
tk.Label(root, text='Виберіть файл:', justify=tk.LEFT, font=('Arial', 13, 'bold')).grid(row=0, column=0, sticky='w', padx=5, pady=5)
tk.Label(root, text='Введіть пароль:', justify=tk.LEFT, font=('Arial', 13, 'bold')).grid(row=1, column=0, sticky='w', padx=5, pady=5)
tk.Label(root, text="Введіть нове ім'я файлу:", justify=tk.LEFT, font=('Arial', 13, 'bold')).grid(row=2, column=0, sticky='w', padx=5, pady=5)
tk.Label(root, text="Необхідна дія:", justify=tk.LEFT, font=('Arial', 13, 'bold')).grid(row=3, column=0, sticky='w', padx=5, pady=5)

# Поля для вводу
file_path_input = tk.Entry(root, bd=3, font=('Arial', 11, 'italic'))
tk.Button(root, text='Пошук', command=choice_path, border=2, font=('Arial', 12, 'bold'), cursor='hand1').grid(row=0, column=4, sticky='ew')

password_input = tk.Entry(root, bd=3, font=('Arial', 11, 'italic'))

new_file_name_input = tk.Entry(root, bd=3, font=('Arial', 11, 'italic'))

# Реєстрація полів
file_path_input.grid(row=0, column=1, sticky='ew', columnspan=2, padx=5, pady=5)
password_input.grid(row=1, column=1, sticky='ew', columnspan=2, padx=5, pady=5)
new_file_name_input.grid(row=2, column=1, columnspan=2, sticky='ew', padx=5, pady=5)

# Радіо кнопки вибору
action_text = tk.StringVar()

tk.Radiobutton(root, text='Встановити пароль', variable=action_text, value='encrypt', font=('Arial', 12, 'bold')).grid(row=3, column=1, sticky='w')
tk.Radiobutton(root, text='Зняти пароль', variable=action_text, value='decrypt', font=('Arial', 12, 'bold')).grid(row=3, column=2, sticky='w')

# Кнопка підтредження
tk.Button(root, text='Виконати', command=get_data, bg='red', border=5, pady=15, activebackground='green', font=('Arial', 15, 'bold'), cursor='hand1').grid(row=4, column=1, columnspan=2, sticky='ew')

# Розділення вікна
root.grid_columnconfigure(0, minsize=130)
root.grid_columnconfigure(1, minsize=150)
root.grid_columnconfigure(2, minsize=150)


def main():
    root.mainloop()


if __name__ == '__main__':
    main()
