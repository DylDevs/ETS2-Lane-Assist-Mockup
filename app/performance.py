"""
This file holds code for the performance page of the program 
Credits for this code: Tumppi066, Dylanb92010
"""

from logger import print
import customtkinter as ctk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
from PIL import Image, ImageTk
import os

FOLDER = os.path.dirname(__file__)
frames = []
idleTime = []
background = "#2B2B2B" 
foreground = "#ffffff"

#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.title("Lane Assist")
root.geometry("1000x635")
root.resizable(False, False)
print('Performance window created')

homeframe=ctk.CTkFrame(master=root, height=605, width=750)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=0, row=0, column=1)

buttonframe=ctk.CTkFrame(master=root, height=605, width=175)
buttonframe.grid_propagate (False) 
buttonframe.grid(pady=13, padx=20, row=0, column=0)

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

disclaimer=ctk.CTkLabel(master=homeframe, text="*This page is non functional")
disclaimer.grid(sticky="n")

dev_x = [0, 20, 36, 40, 67, 70, 84, 90, 96, 100]
dev_y = [0, 19, 20, 35, 41, 45, 62, 80, 100, 76]

def CreateGraph():
    # Almost everything in this function is from Tumppi066's app
    # I simply adjusted some figures to make it fit my program
    
    # Open Matplotlib style file that contains graph style
    os.chdir(FOLDER)
    plt.style.use("assets\MatPlotLib Style (Performance).mplstyle")
    # Make a graph (also support blitting)
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 2)
    # Set axis text colors to white
    ax.tick_params(axis='x', colors=foreground)
    ax.tick_params(axis='y', colors=foreground) 
    # Remove the small black lines around the graph
    ax.spines['top'].set_color(background)
    ax.spines['right'].set_color(background)  
    # Set axis labels and values    
    ax.set_ylabel("Time (ms) Idle (%)")        
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)
    ax.set_autoscale_on(False)
    # Plot values
    ax.plot(dev_x, dev_y)   
    # Display graph in UI
    canvas = FigureCanvasTkAgg(fig, master=homeframe)
    canvas.get_tk_widget().grid(row=0, column=0, padx=23, pady=20)
    canvas.draw()

CreateGraph()

fps=ctk.CTkLabel(master=homeframe, text="-- FPS (-- ms)", font=('Consolas', 30, 'bold'))
fps.grid()

processframe=ctk.CTkFrame(master=homeframe, height=250, width=580)
processframe.grid_propagate(False)
processframe.grid(pady=10)

allprocess=ctk.CTkLabel(master=processframe, text='All', font=("Roboto", 16))
allms=ctk.CTkLabel(master=processframe, text='-- ms', font=("Roboto", 16))
allprocess.grid(sticky='n', column=0, row=0, padx=10, pady=10)
allms.grid(sticky='n', column=1, row=0, padx=490, pady=10)

lastframe=ctk.CTkLabel(master=homeframe, text="*All information is for the last frame")
lastframe.grid(sticky='n', pady=0)

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