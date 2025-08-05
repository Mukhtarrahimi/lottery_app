import tkinter as tk
from tkinter import ttk, filedialog, messagebox

window = tk.Tk()
window.title("lottery_app")
window.geometry("500 * 400")
window.resizable(True, True)
window.configure(background="blue")

file_label = ttk.Label(window, text= "Select the file participants.", font=('Arial', 12), background='', foreground='')
style = ttk.Style()
style.configure("TFream", background = '')

file_label.pack(pady=15)
file_frame = ttk.Frame(window)
file_frame.pack()
file_entry = ttk.Entry(file_frame, font=('Arial', 12))
file_entry.grid(row=0, column=0, padx=5, pady=5)

window.mainloop()