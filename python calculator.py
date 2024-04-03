import tkinter as tk
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
row = 1
col = 0
for button_label in buttons:
    button = tk.Button(root, text=button_label, padx=20, pady=10, font=("Arial", 12))
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
