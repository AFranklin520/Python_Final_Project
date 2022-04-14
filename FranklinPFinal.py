#FranklinFinalProject
#Programmer: Anthony Franklin
#Email: afranklin18@cnm.edu
#Purpose: allows the user to select a group of files, applications, or website and create a customized workspace that will open at the click of a button.

import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import font

#Creating custom fonts for visual appeal

my_font=('Arial', 15, 'bold')
my_font1=('Arial', 10, 'underline','bold')
my_font3=('Arial', 10, 'bold')
#Accessing/creating an external list which will interact with out internal listbox.

apps=[]

if os.path.isfile('workspaces.txt'):
    with open('workspaces.txt','r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]
        tempApps=[]
else:
    with open('workspaces.txt' ,'w') as fp:
        pass

#Creating our user interface/GUI

win = tk.Tk()
win.title("Your New Favorite Utility")
win.resizable(True, True)
win.wm_overrideredirect(0)
win.geometry("450x450")
WinHt=win.winfo_reqheight()
WinWd=win.winfo_reqwidth()
posR=int(win.winfo_screenwidth()/2-999/2)
posD=int(win.winfo_screenheight()/2 - 591/2)
win.geometry(f'+{posR}+{posD}')

bg = PhotoImage(file = "background.png")
#image_label = tk.Label(win , image =bg)
#image_label.place(x = 0 , y = 0)
#Welcome.configure(font=my_font)
#Welcome.pack(pady = 20, padx = 10, anchor = NW)

canv= Canvas(win, width = 450, height = 450)
canv.pack(fill='both',expand=True)
canv.create_image(0,0,image=bg, anchor ='nw')
canv.create_text(230,25,text = "Add app, sites, and docs to your workspace => \nLaunch them all with one click", font = ("Arial", 16), fill = 'white')





#Creating our listbox

lbox=Listbox(win,fg = "#483C32", bg="#B6B6B4",width=40, height =25)
lbox.configure(font=my_font1)
lbox_window=canv.create_window(10,120,anchor = 'nw', window = lbox, width=430,height=200)
#Exporting the list created from our external txt file into our listbox

for item in apps:
    lbox.insert(END,item)

#Creating function to write our changes to external txt file
def write():
    with open('workspaces.txt','w') as f:
        for app in apps:
            f.write(app+',')
           
            
#Lets the user select any kind of file from his computer for his workspace

def addApp():                       
    filename = filedialog.askopenfilename(initialdir="/",
     title = "Select File",)
    filetypes = ("all files", "*.*")
    apps.append(filename)
    lbox.insert(END,filename)
    write()

#Lets the user paste a hyperlink into his workspace. Writes changes to external txt file.

def addSite():
    link = simpledialog.askstring('Web Link',
        'Please paste the website you wish to add')
    apps.append(link)
    lbox.insert(END,link)
    write()

#Runs all desired items in the workspace. Writes changes to external txt file.

def runApps():
    for app in apps:
        os.startfile(app)

#Deletes the selected file from the workspace. Writes changes to external txt file.
def delete():
    
    x=lbox.get(ANCHOR)
    if x in apps:
        apps.remove(x)
    lbox.delete(ANCHOR)
    txt=open('workspaces.txt','r+')
    txt.truncate(0)
    write()


#Buttons

addFile = Button(win, text = 'Add file', fg = '#34282C', font= my_font3,command = addApp)
addLink = Button(win, text = 'Paste link', fg = '#34282C', font= my_font3,command = addSite)
runList = Button(win, text = 'Run Workspace', fg = '#34282C', bg = '#00FF00', font= my_font3,command=runApps)
delApps= tk.Button(win, text = "DELETE SELECTED\nITEM FROM YOUR WORKSPACE", fg = 'white', bg = "red",font =my_font3, command = delete)
addFile_window = canv.create_window(10,70,anchor = "nw", window = addFile)
addLink_window = canv.create_window(125,70,anchor = "nw", window = addLink)
runList_window = canv.create_window(250,70,anchor = "nw", window = runList)
delApps_window = canv.create_window(110,340, anchor='nw', window = delApps)

# Execute tkinter

win.mainloop()
#write()
