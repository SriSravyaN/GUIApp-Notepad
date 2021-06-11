from tkinter import scrolledtext
from tkinter import filedialog
#from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *

from PIL import Image,ImageTk

#Creating window
root=Tk()
root.title("Notepad App")
#root.iconbitmap('pad.ico')
root.geometry('600x600')
root.resizable(0,0)

#fonts and colors
textbox_color='#fffadc'
menu_color='#dbd9db'
root_color='#6c809a'

#define layouts
#define frames

menu_frame=Frame(root,bg=menu_color)
textbox_frame=Frame(root,bg=textbox_color)
menu_frame.pack(padx=5,pady=5)
textbox_frame.pack(padx=5,pady=5)

#functions
def change_font(event):
    if options_list.get() == 'none':
        my_font=(font_list.get(),sizes_list.get())
    else:
        my_font=(font_list.get(),sizes_list.get(),options_list.get())
    input_text.config(font=my_font)
    
def new_note():
    que=messagebox.askyesno("New Note","Are you sure you want to create new note?")
    if que ==1:
        input_text.delete("1.0",END)
def save_note():
    
    saveloc=filedialog.asksaveasfilename(initialdir='./',title="Save Note",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(saveloc,'w') as f:
        f.write(font_list.get()+ "\n")
        f.write(sizes_list.get() + "\n")
        f.write(options_list.get() + "\n")
        f.write(input_text.get("1.0",END))
        
        
def close_note():
    que=messagebox.askyesno("Close Note","Are you sure you want to close note?")
    if que ==1:
        root.destroy()
        
def open_file():
    openloc=filedialogue.askopenfilename(initialdir='./',title='open note',filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(openloc,'r') as f:
        input_text.delete("1.0",END)
        font_list.set(f.readline().strip())
        sizes_list.set(f.readline().strip())
        options_list.set(f.readline().strip())
        
        text=f.read()
        
        input_text.insert("1.0",text)


#layout for menubar
#open_image=ImageTk.PhotoImage(Image.open('open.png'))
open_button=Button(menu_frame,text="open",command=open_file)
open_button.grid(row=0,column=1,padx=5,pady=5 )

#new_image=ImageTk.PhotoImage(Image.open('new.png'))
new_button=Button(menu_frame,text="new",command=new_note)
new_button.grid(row=0,column=0,padx=5,pady=5 )

#save_image=ImageTk.PhotoImage(Image.open('new.png'))
save_button=Button(menu_frame,text="save",command=save_note)
save_button.grid(row=0,column=2,padx=5,pady=5 )

#close_image=ImageTk.PhotoImage(Image.open('close.png'))
close_button=Button(menu_frame,text="close",command=close_note)
close_button.grid(row=0,column=3,padx=5,pady=5 )

        

#fonts list
font_list=StringVar()
fonts=['Times New Roman','Courier','SimSun','Open Sans','Roboto','Serif','Georgia','Lato','Terminal']
font_list_drop=OptionMenu(menu_frame, font_list, *fonts,command=change_font)
font_list.set("Times New Roman")
font_list_drop.grid(row=0,column=4,padx=5,pady=5)
font_list_drop.config(width=16)

#sizes
sizes=[8,10,12,14,16,18,20,24,28,32,36,40,42,44,48,50,54,58,60,64]
sizes_list=IntVar()
sizes_list_drop=OptionMenu(menu_frame,sizes_list,*sizes,command=change_font)
sizes_list.set(8)
sizes_list_drop.grid(row=0,column=5,padx=5,pady=5)
sizes_list_drop.config(width=2)

#styles
options=['none','bold','italic']
options_list=StringVar()
options_list_drop=OptionMenu(menu_frame, options_list, *options,command=change_font)
options_list.set('none')
options_list_drop.grid(row=0,column=6,padx=5,pady=5)
options_list_drop.config(width=6)

#DEFINING textbox frame
my_font= (font_list.get(),sizes_list.get())
input_text=scrolledtext.ScrolledText(textbox_frame,width=1000,height=100,bg=textbox_color,font=my_font)
input_text.pack()


#root window's mainloop
root.mainloop()