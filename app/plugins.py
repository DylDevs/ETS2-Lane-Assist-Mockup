"""
This file holds code for the plugins page of the program 
Credits for this code: Dylanb92010, Tumppi066
"""

from logger import print
import customtkinter as ctk
import os
import webbrowser
from PIL import Image, ImageTk

#Make window
root=ctk.CTk()
root.resizable(False, False)
root.title("Lane Assist")
root.geometry("1200x635")
print('Main window created')

FOLDER = os.path.dirname(__file__)
fg_color="transparent"
border_width=2
border_color="#1F6AA5"

buttonframe=ctk.CTkFrame(master=root, height=605, width=175)
buttonframe.grid_propagate (False) 
buttonframe.grid(pady=13, padx=20, row=0, column=0)

homeframe=ctk.CTkFrame(master=root, height=605, width=970)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=0, row=0, column=1)

miscframe=ctk.CTkFrame(master=homeframe, height=500, width=160)
miscframe.grid_propagate (False)
miscframe.grid(sticky="s", column=0, row=0, padx=15, pady=30)

detectionframe=ctk.CTkFrame(master=homeframe, height=500, width=160)
detectionframe.grid_propagate (False)
detectionframe.grid(sticky="s", column=1, row=0, padx=15, pady=30)

captureframe=ctk.CTkFrame(master=homeframe, height=500, width=160)
captureframe.grid_propagate (False)
captureframe.grid(sticky='s',column=2, row=0, padx=15, pady=30)

plugininfoframe=ctk.CTkFrame(master=homeframe, height=580, width=370)
plugininfoframe.grid_propagate (False) 
plugininfoframe.grid(sticky="n", column=3, row=0, padx=10, pady=10)

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

fg_color="transparent"
border_width=2
border_color="#1F6AA5"

def MakeButton(master, text):
    button = ctk.CTkButton(master=master, text=text, fg_color=fg_color, border_width=border_width, border_color=border_color, width=160, height=30)
    button.grid()
    return button

def MakeBigLabel(text):
    boldlabel = ctk.CTkLabel(master=plugininfoframe, text=text, font=("Roboto", 27))
    boldlabel.grid(sticky="w", padx=10)
    return boldlabel

def MakeLabel(text):
    label = ctk.CTkLabel(master=plugininfoframe, text=text, font=("Roboto", 12))
    label.grid(sticky="w", padx=10)
    return label

misc1=ctk.CTkLabel(master=homeframe, text="Misc. Plugins")
misc1.grid(sticky="n", column=0, row=0, pady=0, padx=0)
misc2=ctk.CTkLabel(master=homeframe, text="Optional")
misc2.grid(sticky="n", column=0, row=0, pady=30, padx=0)
MakeButton(miscframe, "Default Steering")
MakeButton(miscframe, "External API")
MakeButton(miscframe, "FPS Limiter")
MakeButton(miscframe, "HUD")
MakeButton(miscframe, "Lane Departure Warning")
MakeButton(miscframe, "LSTR Draw Lanes")
MakeButton(miscframe, "Map")
MakeButton(miscframe, "Show Image")
MakeButton(miscframe, "Truck Sim API")
MakeButton(miscframe, "UFLD Draw Lanes")
MakeButton(miscframe, "V Gamepad Controller")
MakeButton(miscframe, "Virtual Sim API")

misc1=ctk.CTkLabel(master=homeframe, text="Lane Detection Plugins")
misc1.grid(sticky="n", column=1, row=0, pady=0, padx=0)
misc2=ctk.CTkLabel(master=homeframe, text="Required for Lane Detection", text_color="#FF0000")
misc2.grid(sticky="n", column=1, row=0, pady=30, padx=0)
MakeButton(detectionframe, "LSTR Lane Detection")
MakeButton(detectionframe, "UFLD Lane Detection")
MakeButton(detectionframe, "Navigation Detection")

misc1=ctk.CTkLabel(master=homeframe, text="Screen Capture Plugins")
misc1.grid(sticky="n", column=2, row=0, pady=0, padx=0)
misc2=ctk.CTkLabel(master=homeframe, text="Required for Lane Detection", text_color="#FF0000")
misc2.grid(sticky="n", column=2, row=0, pady=30, padx=0)
MakeButton(captureframe, "DX Cam Screen Capture")
MakeButton(captureframe, "MSS Screen Capture")

title = ctk.CTkLabel(master=plugininfoframe, text="Plugins", font=("Roboto", 35))
title.grid(sticky="nw", padx=10, pady=10)

placeholderlabel=ctk.CTkLabel(master=plugininfoframe, text="")
placeholderlabel.grid()

MakeBigLabel("Description")
MakeLabel("This is the plugins page. It does not currently work.")
MakeLabel("(Coming in 2.0)")
MakeBigLabel("Version")
MakeLabel("0.1")
MakeBigLabel("Author")
MakeLabel("Dylanb92010")
MakeBigLabel("URL")
MakeLabel("github.com/dylanb92010/ETS2-ATS-Lane-Assist-Mockup")

loadplugin=ctk.CTkButton(master=plugininfoframe, text="Load Plugin UI", height=50, width=150, font=("Roboto", 23))
loadplugin.grid(sticky="w", padx=10, pady=20)
enableplugin=ctk.CTkButton(master=plugininfoframe, text="Enable/Disable Plugin", height=50, width=150, font=("Roboto", 23))
enableplugin.grid(sticky="w", padx=10, pady=0)

root.mainloop()