"""
This file holds code for the panels page of the program 
Credits for this code: Dylanb92010, Tumppi066
"""

from logger import print
import os
import webbrowser
from PIL import Image, ImageTk
import customtkinter as ctk
print("Panels Page opened")

FOLDER = os.path.dirname(__file__)

#Set theme
print("Set Default theme: Dark")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.resizable(False, False)
root.title("Lane Assist Panels")
root.geometry("900x635")
print('Main window created')

buttonframe=ctk.CTkFrame(master=root, height=605, width=175)
buttonframe.grid_propagate (False) 
buttonframe.grid(pady=13, padx=20, row=0, column=0)

homeframe=ctk.CTkFrame(master=root, height=605, width=650)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=0, row=0, column=1)

panelsframe=ctk.CTkFrame(master=homeframe, height=480, width=200)
panelsframe.grid_propagate (False) 
panelsframe.grid(column=0, row=0, padx=30, pady=50)

panelinfoframe=ctk.CTkFrame(master=homeframe, height=540, width=360)
panelinfoframe.grid_propagate (False) 
panelinfoframe.grid(column=1, row=0)

#Make sidebar buttons 
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

selectpaneltext=ctk.CTkLabel(master=homeframe, text="Select a panel to load")
selectpaneltext.grid(sticky="N", row=0, pady=10)

fg_color="transparent"
border_width=2
border_color="#1F6AA5"

def MakeButton(text):
    button = ctk.CTkButton(master=panelsframe, text=text, fg_color=fg_color, border_width=border_width, border_color=border_color, width=200, height=37)
    button.grid()
    return button

MakeButton("About")
MakeButton("Changelog")
MakeButton("Deep Translator")
MakeButton("First Time Setup")
MakeButton("Panel Manager")
MakeButton("Performance")
MakeButton("Plugin Manager")
MakeButton("Profile Manager")
MakeButton("Screen Capture Placement")
MakeButton("Settings")
MakeButton("Settings JSON Viewer")
MakeButton("Switch Lane Detection Device")
MakeButton("Theme Selector")

def MakeBigLabel(text):
    boldlabel = ctk.CTkLabel(master=panelinfoframe, text=text, font=("Roboto", 27))
    boldlabel.grid(sticky="w", padx=10)
    return boldlabel

def MakeLabel(text):
    label = ctk.CTkLabel(master=panelinfoframe, text=text, font=("Roboto", 12))
    label.grid(sticky="w", padx=10)
    return label

title = ctk.CTkLabel(master=panelinfoframe, text="Panels", font=("Roboto", 35))
title.grid(sticky="nw", padx=10, pady=10)

placeholderlabel=ctk.CTkLabel(master=panelinfoframe, text="")
placeholderlabel.grid()

MakeBigLabel("Description")
MakeLabel("This is the panels page. It does not currently work.")
MakeLabel("(Coming in 2.0)")
MakeBigLabel("Version")
MakeLabel("0.1")
MakeBigLabel("Author")
MakeLabel("Dylanb92010")
MakeBigLabel("URL")
MakeLabel("github.com/dylanb92010/ETS2-ATS-Lane-Assist-Mockup")

loadplugin=ctk.CTkButton(master=panelinfoframe, text="Load Plugin", height=50, width=150, font=("Roboto", 23))
loadplugin.grid(sticky="w", padx=10, pady=10)

root.mainloop()