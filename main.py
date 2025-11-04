import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.PILimgobj = Image.open('images/OIP.png')
        self.imgobj = ImageTk.PhotoImage(self.PILimgobj)
        self.label = tk.Label(mainframe)
        self.label.configure(image=self.imgobj)
        self.label.grid(column=0, row=0)

        file = tk.Button(mainframe, text="Browse", command=self.select_file)
        file.grid(column=1, row=0, padx=10, pady=10)


    def select_file(self):
        filetypes = (
            ('Png', '*.png'),
            ('Jpg', '*.jpg'),
            ('Jpeg', '*.jpeg')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            filetypes=filetypes)
        showinfo(
            title='Selected File',
            message=filename
        )
        new_PILimage = Image.open(filename)
        new_image = ImageTk.PhotoImage(new_PILimage)
        self.label.configure(image=new_image)
        self.label.image = new_image

root = tk.Tk()
root.title("Watermark App")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

image_viwer = ImageViewer(mainframe)


root.mainloop()