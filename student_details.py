from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2



class student_details:  
    def __init__(self, root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Students Management System")


        #variable

        self.var_department=StringVar()
        self.var_Semester=StringVar()
        self.var_Year=StringVar()
        self.var_Course=StringVar()
        self.var_Name=StringVar()
        self.var_StudentID=StringVar()
        self.var_Gender=StringVar()
        self.var_Mobile=StringVar()
        self.var_Photo=StringVar()
        self.var_DOB=StringVar()
        self.var_Address=StringVar()
        self.var_EMail=StringVar()
       


        img1 = Image.open(r"D:\Face Recognition - Tracking Attendence\images\po.png")
        img1 = img1.resize((500,200))
        self.pictureimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root, image= self.pictureimg1)
        first_lbl.place(x=520,y=0, width = 500, height=200)


        heading = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Bradley Hand ITC", 40, "bold", "italic", "underline"))
        heading.place(x= 10,y=210, width=1500, height=70)


        frameA = Frame(self.root, bd = 2, bg="light grey")
        frameA.place(x= 15,y=280, width=1500, height=550)

        frameB = LabelFrame(self.root, bd = 2, bg="white" ,relief=RIDGE, text="STUDENT DETAILS", font=("Bradley Hand ITC", 25, "bold", "italic", "underline"))
        frameB.place(x=25, y=300, width=780, height=500 )

        #course detail frame
        frameC  = LabelFrame(frameB, bd = 1, bg="white" ,relief=RIDGE, text="Course Details", font=("Bradley Hand ITC", 20,"bold", "italic", "underline" ))
        frameC.place(x=10, y=0, width=750, height=130 )

        department = Label(frameC , text="Department", font=("Bradley Hand ITC", 15,"bold", "italic"), bg="white")
        department.grid(row=0, column=0, padx=0, pady=5,sticky=W )
        
        department_combo = ttk.Combobox(frameC,textvariable=self.var_department, font=("Bradley Hand ITC", 15,"bold", "italic"), state="read only")
        department_combo["values"]=("Select department", "Computer Science Engineering", "Electronics and Communication Engineering" , "Electrical Engineering", "Mechanical Engineering", "Civil Engineering")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W )


        


        Semester = Label(frameC , text="Semester ", font=("Bradley Hand ITC", 15,"bold", "italic"), bg="white")
        Semester.grid(row=0, column=2, padx=0, pady=5, sticky=W )
        
        Semester_combo = ttk.Combobox(frameC,textvariable=self.var_Semester, font=("Bradley Hand ITC", 15,"bold", "italic"), state="read only")
        Semester_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        Semester_combo.current(0)
        Semester_combo.grid(row=0, column=3, padx=2, pady=5 ,sticky=W )



        year = Label(frameC , text="Year ", font=("Bradley Hand ITC", 15,"bold", "italic"), bg="white")
        year.grid(row=1, column=0, padx=0, pady=5, sticky=W )
        
        year_combo = ttk.Combobox(frameC,textvariable=self.var_Year, font=("Bradley Hand ITC", 15,"bold", "italic"), state="read only")
        year_combo["values"]=("Select Year", "2022-26", "2021-25", "2020-24", "2019-23", "2018-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W )

        course = Label(frameC , text="Course ", font=("Bradley Hand ITC", 15,"bold", "italic"), bg="white")
        course.grid(row=1, column=2, padx=0, pady=5, sticky=W )
        
        course_combo = ttk.Combobox(frameC,textvariable=self.var_Course, font=("Bradley Hand ITC", 15,"bold", "italic"), state="read only")
        course_combo["values"]=("Select Course", "Mathematics- 1", "Engineering Physics", "Basic of computer programming", "Data Structures and algorithms", "Software engineering" , "DBMS", "Operating System", "Computer Networking")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W )

#Student Information
        frameD  = LabelFrame(frameB, bd = 1, bg="white" ,relief=RIDGE, text="Student Information", font=("Bradley Hand ITC", 20,"bold", "italic", "underline" ))
        frameD.place(x=10, y=170, width=750, height=230  )


        Name = Label(frameD , text="  Name ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        Name.grid(row=0, column=0, padx=0,pady=5, sticky=W )
        
        Name_entry = ttk.Entry(frameD,textvariable=self.var_Name, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        Name_entry.grid(row=0, column=1, padx=2, pady=5 , sticky=W)

        StudentID = Label(frameD , text="Student ID ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        StudentID.grid(row=0, column=2, padx=0,pady=5,  sticky=W )
        
        StudentID_entry = ttk.Entry(frameD,textvariable=self.var_StudentID ,width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        StudentID_entry.grid(row=0, column=3, padx=2, pady=5 , sticky=W)


        Gender = Label(frameD , text="Gender  ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        Gender.grid(row=1, column=0, padx=0,pady=5, sticky=W )

        Gender_combo = ttk.Combobox(frameD,textvariable=self.var_Gender,  font=("Bradley Hand ITC", 15,"bold", "italic"), state="read only")
        Gender_combo["values"]=("Select Gender", "Male", "Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=1, column=1, padx=2,pady=5, sticky=W )
        


        Mobile = Label(frameD , text="Mobile ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        Mobile.grid(row=1, column=2, padx=0,pady=5,sticky=W )
        
        Mobile_entry = ttk.Entry(frameD,textvariable=self.var_Mobile, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        Mobile_entry.grid(row=1, column=3, padx=2, pady=5 , sticky=W)

        alternateNO = Label(frameD , text="PHOTO ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        alternateNO.grid(row=2, column=0, padx=0 ,pady=5,sticky=W )
        
        alternateNO_entry = ttk.Entry(frameD,textvariable=self.var_Photo, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        alternateNO_entry.grid(row=2, column=1, padx=2, pady=5 ,sticky=W)

        DOB = Label(frameD , text="DOB ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        DOB.grid(row=2, column=2, padx=0,pady=5, sticky=W )
        
        DOB_entry = ttk.Entry(frameD,textvariable=self.var_DOB, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        DOB_entry.grid(row=2, column=3, padx=2, pady=5 , sticky=W)
     
        Address = Label(frameD , text="Address ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        Address.grid(row=3, column=0, padx=0,pady=5, sticky=W )
        
        Address_entry = ttk.Entry(frameD,textvariable=self.var_Address, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        Address_entry.grid(row=3, column=1, padx=2 ,pady=5,sticky=W)

        EMail = Label(frameD , text="E-Mail ", font=("Bradley Hand ITC", 15,"bold", "italic", ), bg="white")
        EMail.grid(row=3, column=2, padx=0,pady=5, sticky=W )
        
        EMail_entry = ttk.Entry(frameD,textvariable=self.var_EMail, width=20,font=("Bradley Hand ITC", 15,"bold", "italic"))
        EMail_entry.grid(row=3, column=3, padx=2, pady=5 , sticky=W)

        
 

       


        

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(frameD, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=4, column=0)
        
        radiobtn2=ttk.Radiobutton(frameD,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=4, column=1)

#buttons frame

        framebtn  = LabelFrame(frameB, bd = 1, bg="white" ,relief=RIDGE)
        framebtn.place(x=10, y=390, width=750, height=50  )

        savebtn=Button(framebtn, text="Save", command=self.add_data, width=5,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        savebtn.grid(row=0,column=0)

        deletebtn=Button(framebtn, text="Delete",command=self.delete_function, width=5,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        deletebtn.grid(row=0,column=1)

        resetbtn=Button(framebtn, text="Reset",command=self.reset_function, width=5,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        resetbtn.grid(row=0,column=2)

        uploadbtn=Button(framebtn, text="Upload", width=5,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        uploadbtn.grid(row=0,column=3)

        tsamplebtn=Button(framebtn, text="Take Photo",command=self.generate_dataset, width=10,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        tsamplebtn.grid(row=0,column=4)

        usamplebtn=Button(framebtn, text="Update Photo", width=10,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        usamplebtn.grid(row=0,column=5 )


    #right frame
        frameR = LabelFrame(self.root, bd = 1, bg="white" ,relief=RIDGE, text="STUDENT SEARCH", font=("Bradley Hand ITC", 15, "bold", "italic", "underline"))
        frameR.place(x=830, y=300, width=650, height=500 )

        frameS  = LabelFrame(frameR, bd = 1, bg="white" ,relief=RIDGE, text="SEARCH", font=("Bradley Hand ITC", 20,"bold", "italic", "underline" ))
        frameS.place(x=10, y=10, width=630, height=150  )

        search_label = Label(frameS,text="Search by:", font=("Bradley Handd ITC",15, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(frameS,font=("Bradley Handd ITC",15, "bold"),state="readonly")
        search_combo["values"]=("Select","StudentID","Name","Mobile")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)


        search_entry = ttk.Entry(frameS, width=15,font=("Bradley Hand ITC", 15,"bold", "italic"))
        search_entry.grid(row=0, column=2, padx=2, pady=5 ,sticky=W)

        searchbtn=Button(frameS, text="Search",command=self.reset_function, width=10,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        searchbtn.grid(row=1,column=1)

        showbtn=Button(frameS, text="Show", width=10,font=("Bradley Hand ITC", 15,"bold", "italic" ),bg="grey",fg="white")
        showbtn.grid(row=1,column=2)

        frameT  = LabelFrame(frameR, bd = 1, bg="white" ,relief=RIDGE)
        frameT.place(x=10, y=170, width=630, height=300  )

        scroll_x = ttk.Scrollbar(frameT, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frameT, orient=VERTICAL)

        self.student_table = ttk.Treeview(frameT, column=("Department", "Semester", "Year", "Course","StudentID","Name","Gender","Mobile","Photo","DOB","Address","EMail"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("StudentID", text="Student")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Mobile", text="Mobile")
        self.student_table.heading("Photo", text="Photo")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("EMail", text="Email")
        self.student_table.heading("Photo", text="PhotoSampleStatus") 
        self.student_table["show"]="headings" 

        self.student_table.column("Department", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("StudentID", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Mobile", width=100)
        self.student_table.column("Photo", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("EMail", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.show)
        self.calling_data()


        



    #function declaration

    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_Name.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error" ,"All Fields are required",parent=self.root )
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="8979", database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s )",(
                                                                                                                    self.var_department.get(),
                                                                                                                    self.var_Semester.get(),
                                                                                                                    self.var_Year.get(),
                                                                                                                    self.var_Course.get(),
                                                                                                                    self.var_StudentID.get(),
                                                                                                                    self.var_Name.get(),
                                                                                                                    self.var_Gender.get(),
                                                                                                                    self.var_Mobile.get(),
                                                                                                                    self.var_Photo.get(),
                                                                                                                    self.var_DOB.get(),
                                                                                                                    self.var_Address.get(),
                                                                                                                    self.var_EMail.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                    
                                                                                                                ))
                conn.commit()
                self.calling_data()
                conn.close()
                messagebox.showinfo("Data Saved","Data Successfully Saved",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)
#data calling

    def calling_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="8979", database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#update button 
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_Name.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error" ,"All Fields are required",parent=self.root )
        else:
            try:
                update = messagebox.askyesno("Update","Are you sure you want to Update this student?", parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="8979", database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s, semester=%s , Year=%s, Course=%s, Name=%s, Gender=%s, Mobile=%s, Photo=%s, DOB=%s, Address=%s, EMail=%s, PhotoSample=%s where  StudentID=%s",(

                                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                                            self.var_Semester.get(),
                                                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                                                            self.var_Course.get(),
                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                            self.var_Mobile.get(),
                                                                                                                                                                                            self.var_Photo.get(),
                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                            self.var_Address.get(),
                                                                                                                                                                                            self.var_EMail.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_StudentID.get(),

                                                                                                                                                                                     ))


                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Data Successfully Updated", parent=self.root)
                conn.commit()
                self.calling_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"DUe to:{str(es)}", parent=self.root)
        



#show data
    def show(self, event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0]),
        self.var_Semester.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Course.set(data[3]),
        self.var_StudentID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Gender.set(data[6]),
        self.var_Mobile.set(data[7]),
        self.var_Photo.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Address.set(data[10]),
        self.var_EMail.set(data[11]),
        self.var_radio1.set(data[12])


#delete Function

    def delete_function(self):
        if self.var_StudentID.get()=="":
            messagebox.showerror("Error","Student ID is not entered",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Info Delete",f"Are you sure want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="8979",database="facerecognition") 
                    my_cursor=conn.cursor()       
                    sql="delete from student where StudentID=%s"
                    val=(self.var_StudentID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                         return
                conn.commit()
                self.calling_data()
                conn.close()
                messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)



#--------------------RESET Function---------------------

    def reset_function(self):
        self.var_department.set("Select Department")
        self.var_Semester.set("Select semester")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        
        self.var_Name.set("")
        self.var_StudentID.set("")
        self.var_Gender.set("Select Gender")
        self.var_Mobile.set("")
        self.var_Photo.set("")
        self.var_DOB.set("")
        self.var_Address.set("")
        self.var_EMail.set("")


#------------Generate database
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_Name.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error" ,"All Fields are required",parent=self.root )
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="8979", database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,  Semester=%s, Year=%s,Course=%s, Name=%s, Gender=%s,  Mobile=%s,Photo=%s,  DOB=%s, Address=%s, EMail=%s where StudentID=%s",(

                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                            self.var_Semester.get(),
                                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                                            self.var_Course.get(),
                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                            self.var_Mobile.get(),
                                                                                                                                                                            self.var_Photo.get(),   
                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                            self.var_Address.get(),
                                                                                                                                                                            self.var_EMail.get(), 
                                                                                                                                                                            self.var_StudentID.get()==id+1,
                                                                                                                                                                    ))

                
                
                conn.commit()
                self.calling_data()
                self.reset_function()
                conn.close()  
                                                                                                                                                                 

#-------------------------------extracting predefine lib .haar cascade ----------------------

                facedetectionapi = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_croping(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=facedetectionapi.detectMultiScale(gray,1.3,5)
                                #scaling factor=1.3
                                #minimum neughbour = 5

                    for(x,y,w,h) in faces:
                        face_croping=img[y:y+h,y:x+w]
                        return face_croping

                cap = cv2.VideoCapture(0)
                img_id=0 
                while True:
                    ret,myframe=cap.read()
                    if face_croping(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_croping(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_ITALIC, 2,(0,255,0), 2)
                        cv2.imshow("Cropped image", face )

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Image Capture and updates to database")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

if  __name__ == "__main__":
        root = Tk()
        P = student_details(root)
        root.mainloop()