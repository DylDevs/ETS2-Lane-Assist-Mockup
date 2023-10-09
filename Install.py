"""
This is the installer. 
It gathers all of the files and modules needed to run the app.
Make sure that when you use install.py you have create.py in the same directory.
(Make sure you trust authors of all modules and files beforeusing the program)
Credits for this code: Dylanb92010, Tumppi066
"""

import os
import sys
import subprocess
import platform
try:
    import requests
except:
    os.system("pip install requests")
    import requests


APP_URL = "https://github.com/dylanb92010/Lane-Assist-Mockup"
FOLDER = os.path.dirname(__file__)
GOOGLE = "https://google.com"


def printRed(text):
    print("\033[91m {}\033[00m" .format(text))
def printGreen(text):
    print("\033[92m {}\033[00m" .format(text))

# Check for internet
print("Checking for internet connection...")
try:
    requests.get(GOOGLE, timeout=5)
    print("Connection found")
except:
    print("No connection was found")
    print("Please check your internet connection and try again.")
    print("Press enter to exit...")
    input()
    quit()

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
else:
    print("Git was found")
    
print("Checking Python version")
if not sys.version_info[0] != 3 or sys.version_info[1] < 9:
    print("Note: Python 3.11 and up will not work")
    print("Python", platform.python_version(), "is installed")
if sys.version_info[0] != 3 or sys.version_info[1] < 9:
    print("You are currently using", platform.python_version())
    print("Python 3.9 or later is required")
    print("Python 3.11 and up will not work")
    print("Python version 3.10.0 is recomended")
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

dependencies2=ctk.CTkLabel(master=frame, text="keyboard, matplotlib, canvas, time, traceback, PIL, ImageTK")
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

    print("Checking for ImageTK module")
    try:
        from PIL import Image, ImageTk
        print("ImageTK is already installed")
    except:
        print("ImageTK is not installed, installing now...")
        os.system("pip install imageTK")
        from PIL import Image, ImageTk
        print("ImageTK has been installed")

    print("Checking for Fonttools module")
    try:
        from fontTools.ttLib import TTFont
        print("Fonttools already installed")
    except:
        print("Fonttools is not installed, installing now...")
        os.system("pip install fonttools")
        from fontTools.ttLib import TTFont
        print("Fonttools has been installed")
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
    os.chdir(FOLDER)
    print("Checking connection to github...")
    try:
        requests.get(APP_URL, timeout=5)
        print("Connection to github successful")
    except:
        print("Connection to github failed")
        print("Please check your internet connection and try again.")
        print("You can also check githubstatus.com to check for outages")
        print("Press enter to exit...")
        input()
        quit()
    print("Downloading App, this could take awhile depending on your conection")
    os.chdir(FOLDER)
    os.system("git clone https://github.com/dylanb92010/Lane-Assist-Mockup")
    print("The app will now create files to run and update the program easier")
    from fontTools.ttLib import TTFont
    font = TTFont(r"Lane-Assist-Mockup\app\assets\Roboto-Regular.ttf")
    font.save
    import time
    if not os.path.exists(r"Lane-Assist-Mockup\run.py"):
        print("Run.py and/or update.py does not exist")
        print("Creating now...")
        os.chdir(FOLDER)
        time.sleep(2)
        import create
        quit()
    elif not os.path.exists(r"Lane-Assist-Mockup\update.py"):
        print("Update.py does not exist")
        print("Creating now...")
        os.chdir(FOLDER)
        time.sleep(2)
        import create
        quit()
    else:
        print("Run.py and Update.py exist")
        print("App has been downloaded")
        print("Use run.py to open the Lane Assist app")
        print("Use update.py to update the app whena new release is out")
        print("Press Enter to exit...")
        input()
        exit()
    
def closepopup():
    print("Exit window created")
    def closewindow():
        print("Closed window")
        exit()
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
root.mainloop()