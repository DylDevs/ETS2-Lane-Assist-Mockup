#Import required modules
from logger import print
print("Importing modules")
import tkinter as tk
import customtkinter as ctk
import webview
print("Imported")

#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.geometry("850x600")
print('Main window created')

#Create Frame
print("Creating Frame...")
aboutframe=ctk.CTkFrame(master=root, height=570, width=600)
aboutframe.grid_propagate (False) 
aboutframe.grid(sticky="N", pady=13, padx=200, row=0, column=1)

abouttitle=ctk.CTkLabel(master=aboutframe, text="About", font=("Roboto", 50))
abouttitle.grid(padx=240, pady=10)

about1=ctk.CTkLabel(master=aboutframe, text="The app backend was made by Tumppi066. In addition to the following plugin developers:", font=("Roboto", 14))
about1.grid()

about2=ctk.CTkLabel(master=aboutframe, text="Tumppi066, DTheIcyDragon, Cloud-121", font=("Roboto", 14))
about2.grid()

about3=ctk.CTkLabel(master=aboutframe, text="To all those who supported me:", font=("Roboto", 14))    
about3.grid() 

about4=ctk.CTkLabel(master=aboutframe, text="Thank you, from the bottom of my heart", font=("Roboto", 30)) 
about4.grid(pady=20)

about5=ctk.CTkLabel(master=aboutframe, text="In addition this app wouldn't be possible without the work of ibaiGorordo, who translated ", font=("Roboto", 14))
about5.grid()

about6=ctk.CTkLabel(master=aboutframe, text="all the models I used in the default plugins to pytorch and onnx.", font=("Roboto", 14))
about6.grid()

about7=ctk.CTkLabel(master=aboutframe, text="And of course the researchers who made those models in the first place!", font=("Roboto", 14))
about7.grid()

about8=ctk.CTkLabel(master=aboutframe, text="I'm also going to give a shoutout to the developers of sv_ttk and dxcam. They have been essential ", font=("Roboto", 13))
about8.grid()

about9=ctk.CTkLabel(master=aboutframe, text="in the development of this app.", font=("Roboto", 14))
about9.grid()

def kofilink():
    webview.create_window('Support me on Ko-Fi', 'https://ko-fi.com/tumppi066')
    webview.start()

supportkofi=ctk.CTkButton(master=aboutframe, text="Support me on Ko-Fi", font=("Roboto", 20), height=50, width=200, command=kofilink)
supportkofi.grid(pady=30)
print("Frame created")

def closepopup():
    def closewindow():
        root.destroy()
        
    def cancelclose():
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