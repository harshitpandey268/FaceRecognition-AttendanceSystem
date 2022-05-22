from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class Train:  
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Face Recognition -- Training Database")

        heading = Label(self.root, text="TRAIN DATASET", font=("Bradley Hand ITC", 40, "bold", "italic", "underline"),bg="white",fg="red")
        heading.place(x= 10,y=10, width=1500, height=80)

        img1 = Image.open(r"images\trains.jpg")
        img1 = img1.resize((800,300))
        self.pictureimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root, image= self.pictureimg1)
        first_lbl.place(x=350,y=100, width = 800, height=300)


        trainbtn=Button(self.root,command=self.train_image,cursor="hand2", text="CLICK HERE TO TRAIN THE DATASET", width=30,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="white",fg="blue")
        trainbtn.place(x=500,y=500, width = 500, height=100)



    def train_image(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img= Image.open(image).convert('L')
            imageNP= np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training Image",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # train 
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Training Dataset Completed", parent=self.root)

if  __name__ == "__main__":
    root = Tk()
    P = Train(root)
    root.mainloop()