#!/usr/bin/python3
# Black-Music v1.0
import os,subprocess,platform
try:
    import wget
except ImportError:
    os.system("pip install wget")
try:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import showerror
except ImportError:
    subprocess.getoutput("pip update tk-tools")

class black_music(Tk):
    def __init__(self):
        super(black_music,self).__init__()
        self.title('Black-Music/Update')
        label_l = Label(self,text='Black-Music',background='white',foreground='black',font=("None",15))
        label_l.place(bordermode=INSIDE,x=120,y=20)
        self.update_b = Button(self,text='Update',command=self.update)
        self.update_b.place(bordermode=OUTSIDE,x=160,y=110)
        self.exit_b = Button(self,text='Exit',command=self.ext)
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=135)

        self.config(background='white')
        self.resizable(False,False)
        self.geometry("400x300")
        self.photo = PhotoImage(file = './Scr/black.png')
        self.iconphoto(False,self.photo)
        self.mainloop()
    def update(self):
        global pr,label_progressbar
        label_progressbar = Label(self,text='Updating...')
        label_progressbar.place(bordermode=INSIDE,x=105,y=40)
        pr = Progressbar(self,orient='horizontal',mode='determinate',length=200)
        pr.place(bordermode=INSIDE,x=105,y=65)
        pr.start(55)
        if platform.system() == 'Linux':
            pr.after(6000,self.update_2)
        else:
            pr.after(6000,self.update_window)
    def update_2(self):
        subprocess.getoutput("cd .. && rm -r Black-wikipedia && git clone https://github.com/black-woftware-company/Black-Music")
        label_progressbar.destroy()
        pr.stop()
        pr.destroy()
        label_mess = Label(self,text='Complete!',foreground='black',background='white')
        label_mess.place(bordermode=INSIDE,x=170,y=65)
        self.update_b.destroy()
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=110)
    def update_window(self):
        subprocess.getoutput("cd .. && rm -r Black-wikipedia")
        wget.download("https://github.com/black-software-Com/Black-Wikipedia/archive/refs/heads/master.zip")
        label_progressbar.destroy()
        pr.stop()
        pr.destroy()
        label_mess = Label(self,text='Complete!',foreground='black',background='white')
        label_mess.place(bordermode=INSIDE,x=170,y=65)
        self.update_b.destroy()
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=110)
    def ext(self):
        self.destroy()
        self.quit()
        quit()
if __name__ == '__main__':
    if platform.system() == 'Linux':
        if os.getuid() == 0:
          window = black_music()
        else:
            showerror(title='Cannot Running',message='Please, Check Root!')
    else:
        window = black_music()
