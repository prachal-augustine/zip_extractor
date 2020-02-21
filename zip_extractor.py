# from tkinter import *
from tkinter import *
import tkinter as tk
# import tkinter as tk
# import os
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from tkinter.ttk import *
import zipfile


class Frame:
    def extractor(self, filename, destination):
        # print(filename)
        # print(destination)
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(destination)
        self.progress_bar()
        return

    def progress_bar(self):
        # creating tkinter window
        self.pg = tk.Tk()
        self.pg.title('Extraction')
        # Progress bar widget
        progress = Progressbar(self.pg, orient=tk.HORIZONTAL, length=180, mode='determinate')

        # Function responsible for the updation
        # of the progress bar value
        def bar():
            import time
            for i in range(1, 110, 4):
                progress['value'] = i
                self.pg.update_idletasks()
                time.sleep(0.3)
            self.pg.destroy()
            msg = tk.Tk()
            msg.withdraw()
            messagebox.showinfo('Message', 'Congrats!! Files have been successfully extracted')
            msg.destroy()

        progress.pack(pady=10)
        # This button will initialize # the progress bar
        b1 = tk.Button(self.pg, text='Start Extracting', command=bar)
        b2 = tk.Button(self.pg, text='Cancel', width=10, command=self.pg.destroy)
        self.pg.geometry('200x100')
        b1.pack()
        b2.pack()
        b1.place(x=10, y=40)
        b2.place(x=120, y=40)
        # infinite loop
        self.pg.mainloop()
        return

    def select_folder(self):

        self.dummy_destination = askdirectory()
        print(self.dummy_destination)
        self.s.destroy()
        self.extractor(self.filename, self.dummy_destination)
        return

    def file_check(self, filename):
        if filename.lower().endswith('.zip'):
            # None
            self.second_window()
            # Extractor(filename)
            return 1
        elif filename.endswith(''):
            msg = tk.Tk()
            msg.withdraw()
            messagebox.showinfo('Error', 'Please select a file')
            msg.destroy()
            calling()
        else:
            msg = tk.Tk()
            msg.withdraw()
            messagebox.showinfo('Error', 'This is not a valid ZIP file')
            msg.destroy()
            calling()
            return 0

    def file_explorer(self):
        self.filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        # print(self.filename)
        self.r.destroy()
        self.file_check(self.filename)
        return

    def root_window(self):
        self.r = tk.Tk()
        self.r.title('ZIP Extractor')
        self.r.geometry('250x250')
        path = 'C:/Users/praugust/Desktop/unnamed.PNG'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(self.r, image=img)
        panel.pack()
        # tk_image = PhotoImage(file = 'C:/Users/praugust/Desktop/Capture3.PNG')
        # bg_image = PhotoImage(file = 'C:/Users/praugust/Desktop/Capture3.PNG')
        # w = Label(r, image = bg_image, width=50, height=50)
        select_button = tk.Button(self.r, text='Select File', width=15, command=self.file_explorer)
        exit_button = tk.Button(self.r, text='Exit', width=15, command=self.r.destroy)
        select_button.pack()
        exit_button.pack()
        select_button.place(x=60, y=100)
        exit_button.place(x=60, y=150)
        self.r.mainloop()
        return

    def second_window(self):
        # self.r.destroy()
        self.s = tk.Tk()
        self.s.title('Folder Selector')
        self.s.geometry('250x250')
        path = 'C:/Users/praugust/Desktop/unnamed.PNG'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(self.s, image=img)
        panel.pack()
        # tk_image = PhotoImage(file='C:/Users/praugust/Desktop/Capture3.PNG')
        # bg_image = PhotoImage(file='C:/Users/praugust/Desktop/Capture3.PNG')
        # w = Label(r, image = bg_image, width=50, height=50)
        choose_folder = tk.Button(self.s, text='Select Folder', width=15, command=self.select_folder)
        exit_button = tk.Button(self.s, text='Exit', width=15, command=self.s.destroy)
        choose_folder.pack()
        exit_button.pack()
        choose_folder.place(x=60, y=100)
        exit_button.place(x=60, y=150)
        self.s.mainloop()
        return


def calling():
    f = Frame()
    f.root_window()
    # Flag = f.FileCheck(f.filename)
    # if Flag == 1:
    #     f.second_window()
    #     f.Extractor(f.filename, f.dummy_destination)
    #     f.progress_bar()
    # elif Flag == 0:
    #     calling()
calling()
