import os
import sys
import subprocess


APP_URL = "https://github.com/dylanb92010/Lane-Assist-Mockup"
FOLDER = os.path.dirname(__file__)


def printRed(text):
    print("\033[91m {}\033[00m" .format(text))
def printGreen(text):
    print("\033[92m {}\033[00m" .format(text))

# Check for path spaces
print("Checking for path spaces...")
if " " in os.getcwd():
    printRed("The path of this app includes spaces.")
    printRed("Please move the app to a folder path without spaces.")
    printGreen("For example 'C:/LaneAssist/'")
    print("Press Enter to exit...")
    input()
    quit()

# Check for special characters
print("Checking for special charachters in path")
if not os.getcwd().isascii():
    printRed("The path of this app includes special characters.")
    printRed("Please move the app to a folder path without special characters.")
    printGreen("For example 'C:/LaneAssist/'")
    print("Press Enter to exit...")
    input()
    quit()

print("Checking path for OneDrive")
if "OneDrive" in os.getcwd().lower():
    printRed("The path of this app includes 'OneDrive'.")
    printRed("OneDrive prevents the app from creating a virtual environment.")
    printRed("Please move the app to a folder path without 'OneDrive'.")
    printGreen("For example 'C:/LaneAssist/'")
    print("Press Enter to exit...")
    input()
    quit()

def CheckGit():
    try:
        subprocess.check_call(["git", "--version"])
        found = True
    except:
        found = False
    
    return found

print("Checking for git...")
foundGit = CheckGit()
if not foundGit:
    print("Git not found")
    print("Please install git and run the installer again.")
    print("Press Enter to exit...")
    input()
    quit()

print("Checking Python version")
print("Note: Python 3.11 and up may not work")
from platform import python_version
print(python_version)
if sys.version_info[0] != 3 or sys.version_info[1] < 9:
    print("Python 3.9 or later is required")
    print("Python 3.11 and up may not work")
    print("Python version 3.9.13 is recomended")
    print("Press Enter to exit...")
    input()
    quit()
    
print("Importing / Installing required GUI Elements..")
try:
    import customtkinter as ctk
except:
    os.system("pip install customtkinter")
    print("-------------------------")
    print("Please relaunch the app")
    print("-------------------------")
    print("Press Enter to exit...")
    input() 
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

frame=ctk.CTkFrame(master=root, height=400, width=550)
frame.grid_propagate(False)
frame.grid()

def destroyframe():
    frame.destroy()
    installbutton.destroy()
    installbutton2=ctk.CTkButton(master=root, text="Install App", height=50, width=200, font=("Roboto", 25), command=installprogram)
    installbutton2.grid(pady=10)
    newframe()

installtext=ctk.CTkLabel(master=frame, text="To install dependencies, click the above install button")
installtext.grid(padx=10, sticky="W")

dependenciesb=ctk.CTkLabel(master=frame, text="Dependencies being installed are listed below:")
dependenciesb.grid(padx=10, sticky="W")

dependencies=ctk.CTkLabel(master=frame, text="tkinter, customtkinter, readchar, sys, os, colorama, webbrowser, webview")
dependencies.grid(padx=10, sticky="W")

dependencies2=ctk.CTkLabel(master=frame, text="keyboard, matplotlib, canvas, time, traceback, PIL, Image")
dependencies2.grid(padx=10, sticky="W")

def destroytext():
    installtext.destroy()
    dependenciesb.destroy()
    dependencies.destroy()
    dependencies2.destroy()
    inst=ctk.CTkLabel(master=frame, text="This window will be unresponsive, check CMD widnow for progress")
    inst.grid(sticky="W")
    inst2=ctk.CTkLabel(master=frame, text="This could take awhile depending on how many modules you already have installed")
    inst2.grid(sticky="W")
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

    print("Checking for Git module")
    try:
        import git
        print("Git is already installed")
    except:
        print("Git is not installed, installing now...")
        os.system("pip install git")
        import git
        print("Git has been installed")
    import time
    print("Finalizing...")
    time.sleep(2)
    print("Check the install window for further steps")
    destroyframe()

def newframe():
    frame2=ctk.CTkFrame(master=root, height=400, width=550)
    frame2.grid_propagate(False)
    frame2.grid()
    appinstalltext=ctk.CTkLabel(master=frame2, text="Modules have been installed, now the app has to be installed")
    appinstalltext.grid(padx=10, sticky="W")
    appinstalltext2=ctk.CTkLabel(master=frame2, text="Press the Install App button to download app files")
    appinstalltext2.grid(padx=10, sticky="W")
    appinstalltext3=ctk.CTkLabel(master=frame2, text="This will download the files from my GitHub page using Git")
    appinstalltext3.grid(padx=10, sticky="W")

def installprogram():
    print("Downloading App, this could take awhile")
    os.chdir(FOLDER)
    os.system("git clone https://github.com/dylanb92010/Lane-Assist-Mockup")
    import time
    time.sleep(3)
    print("App has been downloaded")
    print("App files have been downloaded to the Lane_Assist_Mockup folder")
    print("Run lane_assist.py to open the Lane Assist")
    print("Press Enter to exit...")
    input()
    quit()

root.mainloop()
