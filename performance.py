import tkinter as tk
import customtkinter as ctk
from PIL import Image

#Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Make window
root=ctk.CTk()
root.geometry("850x600")
root.resizable()
print('Performance window created')

homeframe=ctk.CTkFrame(master=root, height=570, width=600)
homeframe.grid_propagate (False) 
homeframe.grid(sticky="E", pady=13, padx=215, row=0, column=1)

graph=tk.PhotoImage(file="C:\Users\Dylan\Documents\Lane Assist Mockup\graph.png")
graph.grid()

root.mainloop()