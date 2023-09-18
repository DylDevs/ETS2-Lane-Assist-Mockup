import logger
import tkinter as tk
import customtkinter as ctk

#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.geometry("850x600")
root.resizable()
print('Settings window created')

homeframe=ctk.CTkFrame(master=root, height=570, width=600)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=215, row=0, column=1)

updatetext=ctk.CTkLabel(master=homeframe, text="UI Update Every x frames", font=("Roboto", 25))
updatetext.grid(sticky="W", pady=30, padx=20, column=0, row=0)

uiupdates=ctk.CTkEntry(master=homeframe, width=225, height=35)
uiupdates.grid(pady=0, padx=325, column=0, row=0)

printdebug=ctk.CTkCheckBox(master=homeframe, text= "Print Debug", height=25, width=100, font=("Roboto", 25))
printdebug.grid(sticky="W", pady=10, padx=22)


settingframe2=ctk.CTkFrame(master=homeframe, height=275, width=325)
settingframe2.grid_propagate (False) 
settingframe2.grid(sticky="W", column=0, padx=20, pady=40)

languageset=ctk.CTkButton(master=settingframe2, text="Translation Settings", height=50, width=300, font=("Roboto", 25))
languageset.grid(sticky="s", padx=10, pady=20)

reinstall=ctk.CTkButton(master=settingframe2, text="Reinstall plugins", height=50, width=300, font=("Roboto", 25))
reinstall.grid(sticky="s", pady=20)

restart=ctk.CTkButton(master=settingframe2, text="Save & Reload", height=50, width=300, font=("Roboto", 25))
restart.grid(sticky="s", pady=20)

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