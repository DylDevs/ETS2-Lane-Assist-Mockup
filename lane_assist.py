#Import required modules
from logger import print
print("Importing Modules...")
import os
import variables
import tkinter as tk
import customtkinter as ctk
import colorama
import webbrowser
import keyboard
print("Imported")

#Set theme
print("Default theme: Dark")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.title("Lane Assist")
root.geometry("850x600")
print('Main window created')

def destroyall():
    homeframe.destroy()
    homeframe2.destroy()
    print("Frame destroyed")

#Make Frame
print("Creating Franes...") 
buttonframe=ctk.CTkFrame(master=root, height=570, width=175)
buttonframe.grid_propagate (False) 
buttonframe.grid(pady=13, padx=20, row=0, column=0)

homeframe=ctk.CTkFrame(master=root, height=400, width=600)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="N", pady=13, padx=0, row=0, column=1)

homeframe2=ctk.CTkFrame(master=root, height=150, width=600)
homeframe2.grid_propagate (False) 
homeframe2.grid(sticky="S", pady=13, padx=0, row=0, column=1)
print("Frames created")

print("Creating sidebar buttons...")
#Make sidebar buttons 
enable = ctk.CTkButton(master=buttonframe,text="Enable", height=50, font=("Roboto", 25))
enable.grid(padx=17, pady=10)

def panelspage():
    print("Creating panels page...")
    root.destroy()
    import panels

panels = ctk.CTkButton(master=buttonframe,text="Panels", height=50, font=("Roboto", 25), command=panelspage)
panels.grid(padx=17, pady=10)

def pluginsspage():
    print("Creating plugins page...")
    root.destroy()
    import plugins

plugins = ctk.CTkButton(master=buttonframe,text="Plugins", height=50, font=("Roboto", 25), command=pluginsspage)
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

def link():
    print("Opeing discord invite...")
    command=webbrowser.open("https://discord.com/invite/DpJpkNpqwD")

discord= ctk.CTkButton(master=buttonframe,text="Discord", height=50, font=("Roboto",24), command=link)
discord.grid (padx=17, pady=10)

buttonlabel=ctk.CTkLabel(master=buttonframe, text="ETS2 Lane Assist")
buttonlabel.configure(font=("Arial",15))
buttonlabel.grid()

buttonlabelcred=ctk.CTkLabel(master=buttonframe, text="@Tumppi066 2023")
buttonlabelcred.configure(font=("Arial",15))
buttonlabelcred.grid()
print("Sidebar buttons created")

print("Creating home buttons")
panelmanager = ctk.CTkButton(master=homeframe,text="Panel Manager", height=50, width=200, font=("Roboto", 25))
panelmanager.grid(padx=17, pady=10)

pluginmanager = ctk.CTkButton(master=homeframe,text="Plugin Manager", height=50, width=200, font=("Roboto", 25))
pluginmanager.grid(padx=17, pady=10)

firstsetup = ctk.CTkButton(master=homeframe,text="First Time Setup", height=50, width=200, font=("Roboto", 25))
firstsetup.grid(padx=17, pady=10)

language = ctk.CTkButton(master=homeframe,text="Language", height=50, width=200, font=("Roboto", 20))
language.grid(padx=17, pady=10)

def theme(self):
    self.themeselect.get("Light")
    print("Theme Selected: Light")
    ctk.set_appearance_mode("light")

themeselect=ctk.CTkComboBox(master=homeframe, height=50, width=200, font=("Roboto", 22), command=theme)
themeselect.configure(values=["Dark", "Light", "System"]) 
themeselect.set("Default")
themeselect.grid(pady=10, padx=0)

f5refresh=ctk.CTkLabel(master=homeframe2, text="You can use F5 to refresh the UI and come back to this page ", font=("Roboto", 20))
f5refresh2=ctk.CTkLabel(master=homeframe2, text="(As long as the app is disabled)", font=("Roboto", 20))
f5refresh.grid(pady=30, padx=25)
f5refresh2.grid(pady=0, padx=0)
print("Home buttons created")

def closepopup():
    print("Exit window created")
    def closewindow():
        print("Closed window")
        root.destroy()
        
    def cancelclose():
        print("Close Cancelled")
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

#Make the code run in a window
root.mainloop()