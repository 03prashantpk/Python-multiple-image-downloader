# Not in Use currently
from tkinter import *

master = Tk()
master.title('Multi Image Downloader')
l=Label(master, text='Enter No of files you want to download: ').grid(row=0,column=0)
button = Button(master, text='Download', width=25)
button.grid(row=1,column=0,columnspan=2)
e1 = Entry(master,width=30)
e1.grid(row=0, column=1)
master.mainloop()