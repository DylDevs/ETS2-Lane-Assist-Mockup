"""
This file holds code for the settings page of the program 
Credits for this code: Dylanb92010
"""

from logger import print
import customtkinter as ctk
import os
import webbrowser
from PIL import Image, ImageTk

#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.geometry("850x635")
root.resizable(False, False)
print('Settings window created')

FOLDER = os.path.dirname(__file__)

buttonframe=ctk.CTkFrame(master=root, height=605, width=175)
buttonframe.grid_propagate (False) 
buttonframe.grid(pady=13, padx=20, row=0, column=0)

homeframe=ctk.CTkFrame(master=root, height=605, width=600)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=0, row=0, column=1)

enable = ctk.CTkButton(master=buttonframe,text="Enable", height=50, font=("Roboto", 25))
enable.grid(padx=17, pady=10)

def panelspage():
    print("Creating panels page...")
    root.destroy()
    import panels

panels = ctk.CTkButton(master=buttonframe,text="Panels", height=50, font=("Roboto", 25), command=panelspage)
panels.grid(padx=17, pady=10)

def pluginspage():
    print("Creating plugins page...")
    root.destroy()
    import plugins

plugins = ctk.CTkButton(master=buttonframe,text="Plugins", height=50, font=("Roboto", 25), command=pluginspage)
plugins.grid(padx=17, pady=10)

def performancepage():
    print("Creating performance page...")
    root.destroy()
    import performance

performance = ctk.CTkButton(master=buttonframe,text="Performance", height=50, font=("Roboto", 20), command=performancepage)
performance.grid(padx=17, pady=10)

def settingspage():
    print("Creating Settings Page...")
    root.destroy()
    import settings


settings= ctk.CTkButton(master=buttonframe,text="Settings", height=50, font=("Roboto", 25), command=settingspage)
settings.grid(padx=17, pady=10)

def aboutpage():
    print("Creating about page...")
    root.destroy()
    import about

about= ctk.CTkButton(master=buttonframe,text="About", height=50, font=("Roboto", 25), command = aboutpage)
about.grid(padx=17, pady=10)

os.chdir(FOLDER)
image = Image.open("assets\image.png")
resized_image = image.resize((65,45))
discordimage = ImageTk.PhotoImage(resized_image)

def link():
    print("Opeing discord invite...")
    command=webbrowser.open("https://discord.com/invite/DpJpkNpqwD")

discord=ctk.CTkButton(master=buttonframe, text="", image=discordimage, height=50, font=("Roboto",24), command=link)
discord.grid (padx=17, pady=10)

buttonlabel=ctk.CTkLabel(master=buttonframe, text="ETS2 Lane Assist")
buttonlabel.configure(font=("Arial",15))
buttonlabel.grid()

buttonlabelcred=ctk.CTkLabel(master=buttonframe, text="© Tumppi066 2023")
buttonlabelcred.configure(font=("Arial",15))
buttonlabelcred.grid()
buttonlabelcred2=ctk.CTkLabel(master=buttonframe, text="© Dylanb92010 2023")
buttonlabelcred2.configure(font=("Arial",15))
buttonlabelcred2.grid()
v=ctk.CTkLabel(master=buttonframe, text="App Version: v1.0")
v.grid()

updatetext=ctk.CTkLabel(master=homeframe, text="UI Update Every x frames", font=("Roboto", 25))
updatetext.grid(sticky="W", pady=30, padx=20, column=0, row=0)

uiupdates=ctk.CTkEntry(master=homeframe, width=225, height=35)
uiupdates.grid(pady=0, padx=325, column=0, row=0)

printdebug=ctk.CTkCheckBox(master=homeframe, text= "Print Debug", height=25, width=100, font=("Roboto", 25))
printdebug.grid(sticky="W", pady=10, padx=22)


settingframe2=ctk.CTkFrame(master=homeframe, height=240, width=325)
settingframe2.grid_propagate (False) 
settingframe2.grid(sticky="W", column=0, padx=20, pady=40)

languageset=ctk.CTkButton(master=settingframe2, text="Translation Settings", height=50, width=300, font=("Roboto", 25))
languageset.grid(sticky="s", padx=10, pady=15)

reinstall=ctk.CTkButton(master=settingframe2, text="Reinstall plugins", height=50, width=300, font=("Roboto", 25))
reinstall.grid(sticky="s", pady=15)

restart=ctk.CTkButton(master=settingframe2, text="Save & Reload", height=50, width=300, font=("Roboto", 25))
restart.grid(sticky="s", pady=15)

def closepopup():
    def closewindow():
        print("Window closed")
        root.destroy()
        
    def cancelclose():
        print("Close cancelled")
        root2.destroy()

    root2 = ctk.CTkToplevel()
    root2.geometry("350x175")
    root2.title("Confitm Exit")
    root2.resizable(False,False)
    root2.attributes("-topmost", True)

    closetext=ctk.CTkLabel(master=root2, text="Are you sure you want to exit?", font=("Roboto", 20))
    closetext.grid(sticky="W", pady=40, padx=45)

    exitframe=ctk.CTkFrame(master=root2, height=90, width=400)
    exitframe.grid_propagate (False) 
    exitframe.grid(padx=0, pady=0)

    cancel_button = ctk.CTkButton(master=exitframe, text="Cancel", command=cancelclose)
    cancel_button.grid(sticky="W", column=0, row=1, pady=0, padx=13)
    exit_button = ctk.CTkButton(master=exitframe, text="Exit", command=closewindow)
    exit_button.grid(sticky="E", column=1, row=1, pady=23, padx=25)

root.protocol("WM_DELETE_WINDOW", closepopup)

root.mainloop()