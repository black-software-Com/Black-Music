#!/usr/bin/python3
# Black-Music
import os
import webbrowser
from pygame.constants import BUTTON_RIGHT
try:
    from tkinter import *
    from tkinter.ttk import Button as TButton,Label
    from tkinter.messagebox import showerror
    from tkinter import filedialog
except (ImportError,ModuleNotFoundError):
    os.system("pip install tk-tools")

try:
    from pygame.mixer import *
    init()
except ImportError:
    os.system("pip install pygame")
class black_music(Tk):
    def __init__(self):
        super(black_music,self).__init__()
        global click_right
        self.title('Black Music')
        self.photo = PhotoImage(file = './Scr/play-logo.png')
        click_right = Menu(self,tearoff=0)
        click_right.add_command(label='Import File',accelerator='Ctrl+o',command=self.open_file)
        click_right.add_separator()
        click_right.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext)
        menu = Menu(self)
        filemenu = Menu(menu,tearoff=0)
        aboutmenu = Menu(menu,tearoff=0)
        themefile = Menu(menu,tearoff=0)
        donatefile = Menu(menu,tearoff=0)
        filemenu.add_command(label='Import File',accelerator='Ctrl+O',command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext)
        aboutmenu.add_command(label='Black',accelerator='F1',command=self.black)
        aboutmenu.add_command(label='Dev',accelerator='F2',command=self.dev)
        themefile.add_command(label='Dark',command=self.dark)
        themefile.add_command(label='Light',command=self.light)
        donatefile.add_command(label='donate',accelerator='F3',command=self.donate)
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='About',menu=aboutmenu)
        menu.add_cascade(label='Theme',menu=themefile)
        menu.add_cascade(label='Donate',menu=donatefile)
        self.config(menu=menu)
        self.label_b = Label(self,text='Black-Music')
        self.label_b.pack(side = BOTTOM)
        self.play_b = Button(self,text='Play',width=9,height=3,command=self.play_music)
        self.play_b.place(bordermode=OUTSIDE,x=115,y=35)
        self.pause_b = Button(self,text='Pause',width=9,height=3,command=self.pause_music)
        self.pause_b.place(bordermode=OUTSIDE,x=115,y=95)
        self.exit_b = Button(self,text='Exit',width=9,height=3,command=self.ext)
        self.exit_b.place(bordermode=OUTSIDE,x=115,y=155)
        self.bind("<Button-3>",self.do_popup)
        self.bind("<Control-o>",lambda x: self.open_file_2(x))
        self.bind("<F1>",lambda x: self.black_2(x))
        self.bind("<F2>",lambda x: self.dev_2(x))
        self.bind("<F3>",lambda x: self.donate_2(x))
        self.resizable(False,False)
        self.iconphoto(False,self.photo)
        self.geometry("300x300")
        self.mainloop()
    def dark(self):
        self.config(bg='black')
        self.label_b.config(background='black',foreground='green')
        self.exit_b.config(background='black',foreground='green')
        self.pause_b.config(background='black',foreground='green')
        self.play_b.config(background='black',foreground='green')
    def light(self):
        self.config(bg='white')
        self.label_b.config(background='white',foreground='black')
        self.exit_b.config(background='white',foreground='black')
        self.pause_b.config(background='white',foreground='black')
        self.play_b.config(background='white',foreground='black')
    def donate(self):
        webbrowser.open_new_tab('https://idpay.ir/mrprogrammer2938')
    def donate_2(self,x):
        webbrowser.open_new_tab('https://idpay.ir/mrprogrammer2938')
    def do_popup(self,event):
        try:
            click_right.tk_popup(event.x_root,event.y_root,0)
        finally:
            click_right.grab_release()

    def open_file(self):
        try:
            self.file = filedialog.askopenfile(title='Choose File')
            music.load(self.file.name)
            # music.set_volume()
        except AttributeError:
            print(False)
    def black(self):
        webbrowser.open_new_tab('https://black-software.ir')
    def dev(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def black_2(self,x):
        webbrowser.open_new_tab('https://black-software.ir')
    def dev_2(self,x):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def open_file_2(self,x):
        try:
                self.file = filedialog.askopenfile(title='Choose File')
                music.load(self.file.name)
                # music.set_volume()
        except AttributeError:
            print(False)
    def play_music(self):
        try:
            music.play()
        except:
            showerror(title='Cannot Play',message='Please, Check Music File')
    def ext(self):
        self.destroy()
        self.quit()
        quit()
    def pause_music(self):
        music.pause()
if __name__ == '__main__':
    window = black_music()