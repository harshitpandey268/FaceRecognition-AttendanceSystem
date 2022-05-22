from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class Help_Desk:  
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Face Recognition -- Help-Desk")

        img1 = Image.open(r"images\help..jpg")
        img1 = img1.resize((1200,600))
        self.pictureimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root, image= self.pictureimg1)
        first_lbl.place(x=170,y=10, width = 1200, height=600)

        heading = Label(self.root, text="Email - pandeyharshit268@gmail.com", font=("Bradley Hand ITC", 30, "bold"),fg="blue")
        heading.place(x= 340,y=620, width=800, height=40)
        heading1= Label(self.root, text="LinkedIn - https://www.linkedin.com/in/harshit-pandey-6b0268187/       ||      Github - https://github.com/harshitpandey268", font=("Bradley Hand ITC", 15, "bold"),fg="green")
        heading1.place(x=150,y=660, width=1200, height=40)
        heading3= Label(self.root, text="Contact Number - +918979083738", font=("Bradley Hand ITC", 20, "bold"),fg="Red")
        heading3.place(x=150,y=700, width=1200, height=40)





if __name__ == "__main__":
        root = Tk()
        P = Help_Desk(root)
        root.mainloop()

