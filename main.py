import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Watermark App")

imgobj = tk.PhotoImage(file='images/OIP.png')


mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

label = tk.Label(mainframe)
label['image'] = imgobj
label.grid(column=0, row=0)

file = tk.Button(mainframe, text="Browse")
file.grid(column=1, row=0, padx=10, pady=10)


root.mainloop()