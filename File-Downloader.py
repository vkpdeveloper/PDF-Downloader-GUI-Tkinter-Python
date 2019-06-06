from tkinter import ttk
from tkinter import *
import time
import requests
from tqdm import tqdm
import os
from tkinter import messagebox as m_box
import re

win = Tk()
win.title("PDF Downloader")
win.geometry("500x360")
win.minsize(500,360)
win.maxsize(500,360)
frame = ttk.LabelFrame(win, width=290)
frame.pack(padx=30, pady=90)
label1 = ttk.Label(frame, text="Enter The File URL : ")
label1.grid(row=0, column=0,sticky=W)
url = StringVar()
edit_txt = ttk.Entry(frame, width=50, textvariable=url)
edit_txt.grid(row=1, columnspan=4, padx=2, pady=3)
label2 = ttk.Label(frame, text="Enter The File Name : ")
label2.grid(row=2, column=0,sticky=W)
filename = StringVar()
file_name = ttk.Entry(frame, width=50, textvariable=filename)
file_name.grid(row=3, columnspan=4, padx=2, pady=3)

def onClick():
    os.chdir(r"C:\Users\virat\Downloads")
    file_url = url.get()
    file_name_aft_click = filename.get()
    if re.search(".pdf", file_url):
        if (os.path.exists(file_name_aft_click + ".pdf") == False):
            r = requests.get(file_url, stream= True)
            total_size = int(r.headers['content-length'])
            status = Label(win, text="Downloading PDF File...", font="Arial 11", relief=SUNKEN, anchor=W)
            status.pack(side=BOTTOM, fill=X)
            with open(file_name_aft_click + ".pdf", 'wb') as f:
                for data in tqdm(iterable=r.iter_content(chunk_size = 1024), total=total_size/1024, unit="KB"):
                    f.write(data)
            m_box.showinfo("Download Compleated","Your File Successfully Downloaded")
            status.forget()
        else:
            m_box.showerror("Error","File Name Already Exist in Downloading Path !")
    else:
        m_box.showerror("Error", "Only PDF Files are Allowed to Download !")


btn1 = ttk.Button(frame, width=30, text="Download File", command=onClick)
btn1.grid(row=4, columnspan=4, padx=30, pady=5)
win.mainloop()