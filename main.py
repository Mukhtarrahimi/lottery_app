import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def select_winner():
    file = file_entry.get()
    
    try:
        num = int(winner_entry.get())
        if num <= 0:
            messagebox.showinfo('Invalid Number', 'Please enter a number greater than zero.')
            return
    except ValueError:
        messagebox.showinfo('Invalid Input', 'Please enter a valid number.')
        return

    try:
        with open(file, 'r') as f:
            name_list = f.read().splitlines()

        if len(name_list) < num:
            messagebox.showinfo('Error', 'The number of winners exceeds the number of participants.')
            return

        winner_list = random.sample(name_list, num)

        top_window = tk.Toplevel()
        top_window.title('List of Winners')
        top_window.geometry('400x400')
        top_window.configure(bg='#F0F8FF')  

        win_label = ttk.Label(top_window, text='🎉 Lottery Winners 🎉',
                              font=('Arial', 16, 'bold'))
        win_label.pack(pady=10)

        winners_text = '\n'.join(f"{i + 1}. {name}" for i, name in enumerate(winner_list))

        show_winner = tk.Text(top_window, height=15, width=40, font=('Arial', 12))
        show_winner.insert(tk.END, winners_text)
        show_winner.config(state='disabled', bg='#FFFFFF', fg='#333333')
        show_winner.pack(pady=10)

    except FileNotFoundError:
        messagebox.showwarning('File Not Found', 'The selected file was not found.')
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred:\n{str(e)}')

window = tk.Tk()
window.title("🎲 Lottery App")
window.geometry("500x300")
window.configure(bg='#E6F2FF') 

style = ttk.Style()
style.theme_use("clam")  
style.configure("TLabel", background='#E6F2FF', foreground='#333333', font=('Arial', 12))
style.configure("TButton", font=('Arial', 11), padding=6)
style.configure("TEntry", font=('Arial', 11))

file_label = ttk.Label(window, text="Select the participants file (.txt):")
file_label.pack(pady=10)

file_frame = ttk.Frame(window)
file_frame.pack()

file_entry = ttk.Entry(file_frame, width=40)
file_entry.grid(row=0, column=0, padx=5)

file_btn = ttk.Button(file_frame, text='Browse', command=select_file)
file_btn.grid(row=0, column=1)

winner_label = ttk.Label(window, text="Enter number of winners:")
winner_label.pack(pady=10)

winner_entry = ttk.Entry(window, width=10, justify='center')
winner_entry.pack()

select_btn = ttk.Button(window, text='🎯 Select Winners', command=select_winner)
select_btn.pack(pady=20)

window.mainloop()
