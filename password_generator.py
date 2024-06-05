import tkinter as tk
from tkinter import messagebox, font, simpledialog
import random
import string


def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    #create password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("successful","Password Copied")

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Eror", "Password length must be longer than 1.")
            return

        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

    except ValueError:
        messagebox.showerror("Eror", "Please enter a valid number.")

def on_generate_again():
    on_generate()

def save_password(name,password):
    if password:
        with open("password.txt", "a") as file:
            file.write(f"{name} ==> {password} \n")
            messagebox.showinfo("successful","Password saved")

def on_save():
    password = entry_password.get()
    if not password:
        messagebox.showerror("Eror","First you must create a password.")
        return
    name = simpledialog.askstring("Password name","Enter password name : ")
    if name:
        save_password(name,password)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12)

label_length = tk.Label(root, text="Password Length:", bg="#f0f0f0", font=("Arial", 12))
label_length.pack(pady= 0)

entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=3)

label_password = tk.Label(root, text="Generated Password:", bg="#f0f0f0", font=("Arial", 12))
label_password.pack(pady=0)

entry_password = tk.Entry(root, font=("Arial", 12))
entry_password.pack(pady=3)

#generate password button
button_generate = tk.Button(root, text="Generate Password", command=on_generate, font=("Arial", 12), bg="#4caf50",
                            fg="white", activebackground="#45a049")
button_generate.pack(pady=3)

button_generate_again = tk.Button(root, text="Recreate Password", command=on_generate_again, font=("Arial",12), bg="#FF9800", fg = "white", activebackground="#FB8C00")
button_generate_again.pack(pady=3)

#password copy button
button_copy = tk.Button(root, text="Copy",command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white", activebackground="#1e88e5")
button_copy.pack(pady=3)

button_save = tk.Button(root, text="Save", command=on_save, font=("Arial", 12), bg="#0356fc", fg="white",activebackground="#c9bc04")
button_save.pack()

root.mainloop()
