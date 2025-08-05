import tkinter as tk
from tkinter import ttk, filedialog, messagebox

window = tk.Tk()
window.title("lottery_app")
window.geometry("500 * 400")
window.resizable(True, True)
window.configure(background="blue")

file_label = ttk.Label(window, text= "Select the file participants.", font=('Arial', 12), background='', foreground='')
file_label.pack(pady=15)

window.mainloop()