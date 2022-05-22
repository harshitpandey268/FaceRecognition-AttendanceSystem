from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Face_Recognition:  
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Face Recognition -- Face Recognition")

        
        heading = Label(self.root, text="FACE DETECTOR", font=("Bradley Hand ITC", 40, "bold", "italic", "underline"),fg="green")
        heading.place(x= 10,y=10, width=1500, height=80)



        img1 = Image.open(r"images\crowd.png")
        img1 = img1.resize((800,500))
        self.pictureimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root, image= self.pictureimg1)
        first_lbl.place(x=350,y=100, width = 800, height=500)


        detectbtn=Button(self.root,cursor="hand2",command=self.detector ,text="CLICK HERE TO DETECT FACES", width=40,font=("Bradley Hand ITC", 25,"bold", "italic" ),fg="green")
        detectbtn.place(x=500,y=650, width = 500, height=100)

        # saving attendance information
    def attendance(self,i,d,n):
        with open("faceattendance.csv","r+", newline="\n") as f:
            mydata = f.readlines()
            name_list=[]
            for line in mydata:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)and (d not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d-%m-%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{d},{n},{d1},{dtString},{d1},present")
            


        #--------------------------------Function-------------------------
    def detector(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]


            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", username="root", password="8979", database="facerecognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select StudentID from student where StudentID="+str(id))
                i = my_cursor.fetchone()
                i ="+".join(i)


                my_cursor.execute("select Name from student where StudentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select department from student where StudentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)


               
                

                


                if confidence>77:
                    cv2.putText(img,f"ID:{i}" ,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{d}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{n}"      ,(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attendance(i,d,n)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                coord = [x,y,w,y]

            return coord

        def facedetection(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img 


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        vedio_cap = cv2.VideoCapture(0)

        while True:
            ret,img=vedio_cap.read()
            img=facedetection(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Detection",img)

            if cv2.waitKey(1)==13:
                break 
        vedio_cap.release()
        cv2.destroyAllWindows()



if  __name__ == "__main__":
    root = Tk()
    P = Face_Recognition(root)
    root.mainloop()