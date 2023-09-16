import os
try:
    import readchar
except:
    os.system("pip install readchar")
    import readchar

try:
    import customtkinter as ctk
except: 
    os.system("pip install customtkinter")
    print("-------------------------")
    print("Please relaunch the app")
    print("-------------------------")
    print("Press Any Key To Exit...")
    k = readchar.readchar()
    quit()

root=ctk.CTk()
root.title("Lane Assist Installer")
root.geometry("600x600")

title = ctk.CTkLabel(master=root, text="ETS2 Lane Assist Installer", font=("Roboto", 30))
title.grid(padx=125, pady=15)

disclaimer = ctk.CTkLabel(master=root, text="Disclaimer: This program is a concept of an app made by Tumppi066")
disclaimer.grid()

disclaimer2 = ctk.CTkLabel(master=root, text="called ETS2/ATS Lane Assist, you can find the GitHub project here:")
disclaimer2.grid()

githublink = ctk.CTkLabel(master=root, text="https://github.com/Tumppi066/Euro-Truck-Simulator-2-Lane-Assist")
githublink.grid()



root.mainloop()