import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, generated_password)


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=2, padx=10, pady=10)


password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()
