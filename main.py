from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter 
from student_details import student_details
from train import Train
from face_recognition import Face_Recognition
from helpdesk import Help_Desk


class FACE_RECOGNITION_TRACKING_ATTENDENCE:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("FACE RECOGNITION TRACKING ATTENDENCE")


#TITLE
        heading = Label(self.root, text="AUTOMATIC ATTENDENCE", font=("Bradley Hand ITC", 40, "bold", "italic", "underline"))
        heading.place(x= 10,y=10, width=1500, height=70)
        headinga = Label(self.root, text="Face Recognition", font=("Bradley Hand ITC", 30, "bold", "italic", "underline"))
        headinga.place(x= 10,y=80, width=1500, height=70)

#image 1 
        img0 = Image.open(r"D:\Face Recognition - Tracking Attendence\images\background..png")
        img0 = img0.resize((500,350))
        self.pictureimg0= ImageTk.PhotoImage(img0)

        first_lbl = Label(self.root, image= self.pictureimg0)
        first_lbl.place(x=500,y=150, width = 500, height=350)


#Buttons
        pic1= Image.open(r"D:\Face Recognition - Tracking Attendence\images\student.jpg")
        pic1= pic1.resize((240,150),Image.ANTIALIAS)
        self.photopic1 = ImageTk.PhotoImage(pic1)
        b = Button(self.root, image=self.photopic1,command=self.student, cursor="hand2")
        b.place(x=40,y=510,width=240,height=150)



        pic2= Image.open(r"D:\Face Recognition - Tracking Attendence\images\train.jpg")
        pic2= pic2.resize((240,150),Image.ANTIALIAS)
        self.photopic2 = ImageTk.PhotoImage(pic2)
        b2 = Button(self.root,image=self.photopic2,command=self.Train ,cursor="hand2")
        b2.place(x=340,y=510,width=240,height=150)



        pic3= Image.open(r"D:\Face Recognition - Tracking Attendence\images\attendance.jpg")
        pic3= pic3.resize((240,150),Image.ANTIALIAS)
        self.photopic3 = ImageTk.PhotoImage(pic3)
        b3 = Button(self.root, image=self.photopic3,command=self.face, cursor="hand2")
        b3.place(x=640,y=510,width=240,height=150)




        pic4= Image.open(r"D:\Face Recognition - Tracking Attendence\images\helpdesk.png")
        pic4= pic4.resize((240,150),Image.ANTIALIAS)
        self.photopic4 = ImageTk.PhotoImage(pic4)
        b4 = Button(self.root, image=self.photopic4,command=self.help, cursor="hand2")
        b4.place(x=940,y=510, width=240,height=150)


        pic5= Image.open(r"D:\Face Recognition - Tracking Attendence\images\exit.jpg")
        pic5= pic5.resize((240,150),Image.ANTIALIAS)
        self.photopic5 = ImageTk.PhotoImage(pic5)
        b5 = Button(self.root, image=self.photopic5,command=self.exit ,cursor="hand2")
        b5.place(x=1240,y=510, width=240,height=150)

#--------------------------               function for button                   -----------------------------------------

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit the window?", parent=self.root)
        if self.exit > 0:
                self.root.destroy()
        else:
                return

    def student(self):
        self.new_window=Toplevel(self.root)
        self.app=student_details(self.new_window)

    def Train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app= Help_Desk(self.new_window)



if __name__ == "__main__":
        root = Tk()
        P = FACE_RECOGNITION_TRACKING_ATTENDENCE(root)
        root.mainloop()






