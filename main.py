import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk, ImageOps

class ImageViewer:
    def __init__(self, master):
        self.size = (400, 300)
        self.master = master
        self.PILimgobj = Image.open('images/OIP.png')
        self.PILimgobj = ImageOps.contain(self.PILimgobj, self.size, method=Image.Resampling.BICUBIC).convert('RGBA')
        self.imgobj = ImageTk.PhotoImage(self.PILimgobj)
        self.label = tk.Label(mainframe)
        self.label.configure(image=self.imgobj)
        self.label.grid(column=0, row=0)
        self.watermark = Image.open('images/79-791983_draft-watermark-png-stencil-clipart.png').convert('RGBA')
        file = tk.Button(mainframe, text="Browse", command=self.select_file)
        file.grid(column=1, row=0, padx=10, pady=10)

        overlaybtn = tk.Button(mainframe, text="Overlay", command=self.overlay)
        overlaybtn.grid(column=1, row=1, padx=10, pady=10)

    def overlay(self):
        self.watermark = ImageOps.contain(self.watermark, self.size, method=Image.Resampling.BICUBIC).convert('RGBA')
        self.PILimgobj.paste(self.watermark, (0,0))
        self.PILimgobj = ImageOps.contain(self.PILimgobj, self.size, method=Image.Resampling.BICUBIC)
        self.imgobj = ImageTk.PhotoImage(self.PILimgobj)
        self.label.configure(image=self.imgobj)

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
        new_PILimage = ImageOps.contain(new_PILimage, self.size, method=Image.Resampling.BICUBIC)
        new_image = ImageTk.PhotoImage(new_PILimage)
        self.label.configure(image=new_image)
        self.label.image = new_image

root = tk.Tk()
root.title("Watermark App")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

image_viwer = ImageViewer(mainframe)


root.mainloop()