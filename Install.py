print("Importing / Installing required GUI Elements..")
import os
import sys

from platform import python_version
if sys.version_info[0] != 3 or sys.version_info[1] < 9:
    try:
        import readchar
    except:
        os.system("pip install readchar")
    import readchar
    print("Python 3.9 or later is required")
    print("Python 3.11 and up will not work")
    print("Python version 3.9.13 is recomended")
    print("Press Any Key To Exit...")
    k = readchar.readchar()
    quit()
    
try:
    import customtkinter as ctk
except: 
    try:
        import readchar
    except:
        os.system("pip install readchar")
    os.system("pip install customtkinter")
    print("-------------------------")
    print("Please relaunch the app")
    print("-------------------------")
    print("Press Any Key To Exit...")
    k = readchar.readchar()
    quit()

print("Imported")

root=ctk.CTk()
root.title("Lane Assist Installer")
root.geometry("600x650")
root.resizable(False, False)

title = ctk.CTkLabel(master=root, text="ETS2 Lane Assist Installer", font=("Roboto", 30))
title.grid(padx=125, pady=15)

disclaimer = ctk.CTkLabel(master=root, text="Disclaimer: This program is a concept of an app made by Tumppi066")
disclaimer.grid()

disclaimer2 = ctk.CTkLabel(master=root, text="called ETS2/ATS Lane Assist, you can find the GitHub project here:")
disclaimer2.grid(pady=0)

githublink = ctk.CTkLabel(master=root, text="https://github.com/Tumppi066/Euro-Truck-Simulator-2-Lane-Assist")
githublink.grid()

def installredirect():
    destroytext()
installbutton=ctk.CTkButton(master=root, text="Install", height=50, width=200, font=("Roboto", 25), command=installredirect)
installbutton.grid(pady=10)

frame=ctk.CTkScrollableFrame(master=root, height=400, width=550)
frame.grid()

installtext=ctk.CTkLabel(master=frame, text="To install dependencies, click the above install button")
installtext.grid(sticky="W")

dependenciesb=ctk.CTkLabel(master=frame, text="Dependencies being installed are listed below:")
dependenciesb.grid(sticky="W")

dependencies=ctk.CTkLabel(master=frame, text="tkinter, customtkinter, readchar, sys, os, colorama, webbrowser, webview")
dependencies.grid(sticky="W")

dependencies2=ctk.CTkLabel(master=frame, text="keyboard, matplotlib, canvas, time, traceback, PIL, Image")
dependencies2.grid(sticky="W")

def destroytext():
    installtext.destroy()
    dependenciesb.destroy()
    dependencies.destroy()
    dependencies2.destroy()
    unresponsive=ctk.CTkLabel(master=frame, text="This window will be unresponsive, check CMD widnow for progress")
    unresponsive.grid(sticky="W")
    takeawhile=ctk.CTkLabel(master=frame, text="This could take awhile depending on how many modules you already have installed")
    takeawhile.grid(sticky="W")
    installdependencies()

def installdependencies():
    global os
    print("Checking for Tkinter module")
    try:
        import tkinter as tk
        print("Tkinter is already installed")
    except:
        print("Tkinter is not installed, installing now...")
        os.system("pip install tkinter")
        import tkinter as tk
        print("Tkinter has been installed")
    
    print("Checking for CustomTkinter module")
    try:
        import customtkinter as ctk
        print("CustomTkinter is already installed")
    except:
        print("CustomTkinter is not installed, installing now...")
        os.system("pip install customtkinter")
        import customtkinter as ctk
        print("CustomTkinter has been installed")

    print("Checking for Readchar module")
    try:
        import readchar
        print("Readchar is already installed")
    except:
        print("Readchar is not installed, installing now...")
        os.system("pip install readchar")
        import readchar
        print("Readchar has been installed")

    print("Checking for sys module")
    try:
        import sys
        print("sys is already installed")
    except:
        print("sys is not installed, installing now...")
        os.system("pip install sys")
        import sys
        print("sys has been installed")

    print("Checking for os module")
    try:
        import os
        print("os is already installed")
    except:
        print("os is not installed, installing now...")
        os.system("pip install os")
        import os
        print("os has been installed")

    print("Checking for Colorama module")
    try:
        import colorama
        colorama.init()
        print("Colorama is already installed")
    except:
        print("Colorama is not installed, installing now...")
        os.system("pip install Colorama")
        import colorama
        colorama.init()
        print("Colorama has been installed")

    print("Checking for Webbrowser module")
    try:
        import webbrowser
        print("Webbrowser is already installed")
    except:
        print("Webbrowser is not installed, installing now...")
        os.system("pip install webbrowser")
        import webbrowser
        print("Webbrowser has been installed")

    print("Checking for Webview module")
    try:
        import webview
        print("Webview is already installed")
    except:
        print("Webview is not installed, installing now...")
        os.system("pip install pywebview")
        import webview
        print("Webview has been installed")

    print("Checking for Keyboard module")
    try:
        import keyboard
        print("Keyboard is already installed")
    except:
        print("Keyboard is not installed, installing now...")
        os.system("pip install keyboard")
        import keyboard
        print("Keyboard has been installed")

    print("Checking for Matplotlib module")
    try:
        import matplotlib
        print("Matplotlib is already installed")
    except:
        print("Matplotlib is not installed, installing now...")
        os.system("pip install matplotlib")
        import matplotlib
        print("Matplotlib has been installed")

    print("Checking for Canvas module")
    try:
        import canvas
        print("Canvas is already installed")
    except:
        print("Canvas is not installed, installing now...")
        os.system("pip install canvas")
        import canvas
        print("Canvas has been installed")

    print("Checking for Time module")
    try:
        import time
        print("Time is already installed")
    except:
        print("Time is not installed, installing now...")
        os.system("pip install time")
        import time
        print("Time has been installed")

    print("Checking for Traceback module")
    try:
        import traceback
        print("Traceback is already installed")
    except:
        print("Traceback is not installed, installing now...")
        os.system("pip install traceback")
        import traceback
        print("Traceback has been installed")

    print("Checking for PIL module")
    try:
        import PIL
        print("PIL is already installed")
    except:
        print("PIL is not installed, installing now...")
        os.system("pip install pil")
        import PIL
        print("PIL has been installed")

    print("Checking for Image module")
    try:
        from PIL import Image
        print("Image is already installed")
    except:
        print("Image is not installed, installing now...")
        os.system("pip install image")
        from PIL import Image
        print("Image has been installed")
    import colorama
    print(colorama.Fore.GREEN,"All modules have been imported you can close the window")
    finished=ctk.CTkLabel(master=frame, text="All modules have been imported you can close the window")
    finished.grid(sticky="W")


root.mainloop()
