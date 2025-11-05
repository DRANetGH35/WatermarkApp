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
        self.watermark_size = (100, 100)
        self.watermark_position = self.PILimgobj.size[0] - self.watermark_size[0] * 2, self.PILimgobj.size[1] - self.watermark_size[1] * 2
        self.watermark = ImageOps.contain(self.watermark, self.size, method=Image.Resampling.BICUBIC).convert('RGBA')
        self.watermark = self.watermark.resize(self.watermark_size)
        self.transparent = Image.new('RGBA', self.PILimgobj.size)
        self.transparent.paste(self.PILimgobj, (0, 0))
        self.transparent.paste(self.watermark, self.watermark_position, mask=self.watermark)
        self.transparent = self.transparent.convert('RGB')
        self.PILimgobj = ImageOps.contain(self.PILimgobj, self.size, method=Image.Resampling.BICUBIC)
        self.imgobj = ImageTk.PhotoImage(self.transparent)
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
        self.PILimgobj = Image.open(filename)
        self.PILimgobj = ImageOps.contain(self.PILimgobj, self.size, method=Image.Resampling.BICUBIC)
        self.imgobj = ImageTk.PhotoImage(self.PILimgobj)
        self.label.configure(image=self.imgobj)
        self.label.image = self.imgobj

root = tk.Tk()
root.title("Watermark App")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky="NWES")

image_viwer = ImageViewer(mainframe)


root.mainloop()