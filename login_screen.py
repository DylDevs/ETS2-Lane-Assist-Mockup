#Import required modules
import customtkinter as ctk
print('Imported customtkinter module successfully (as ctk)')
import tkinter as tk
print('Imported tkinter module successfully (as tk)')
import time
print('Imported time module successfully')
import subprocess
print('Imported subprocess module successfully')



#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
print('Set theme Default')

root=ctk.CTk()
root.title("ETS2 Lane Assist Login")
root.geometry("600x400")
print('Created 900x600 window')

def login():
    username = entry1.get()
    password = entry2.get()
    print('Created Login function')

    # Check if the username and password are valid
    if username == "a" and password == "a":
        root.destroy()
        print('Valid login, loading main window...')
        import lane_assist
        


    else:
        textbox = ctk.CTkLabel(master=frame, text="Invalid Username or password please try again")
        textbox.configure(font=("Arial",20))
        textbox.pack(pady=10)
        print('Invalid Username or Passowrd')


frame=ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=ctk.CTkLabel(master=frame, text="ETS2 Lane Assist Login")
label.pack(pady=12,padx=10)

entry1=ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2=ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

checkbox=ctk.CTkCheckBox(master=frame,text= "Remember Me")
checkbox.pack(pady=12,padx=10)

checkbox2=ctk.CTkCheckBox(master=frame,text= "Show Password")
checkbox2.pack(pady=12,padx=10)
print('Created UI')

root.mainloop()


