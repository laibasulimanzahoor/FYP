from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #================variables==================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        # Load and display first image
        img = Image.open("./Images/student.jpg")
        img = img.resize((430, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=430, height=130)
        
        # Load and display second image
        img1 = Image.open("./Images/yahoo.jpg")
        img1 = img1.resize((430, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=430, y=0, width=430, height=130)

        # Load and display third image
        img2 = Image.open("./Images/smart-attendance.jpg")
        img2 = img2.resize((430, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=860, y=0, width=430, height=130)
        
        # bg image
        img3 = Image.open("./Images/bg.png")
        img3 = img3.resize((1450, 540), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1450, height=540)
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 33, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1450, height=45)
        
        self.main_frame_width = 1450 - 200  # Desired width reduction from the right side
        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=3, y=55, width=self.main_frame_width, height=460)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=610,height=450)
        
        
        img_left = Image.open("./Images/hehe.jpg")
        img_left = img_left.resize((610, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl2 = Label(left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=610, height=90)
        
        # current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=80,width=595,height=100)
        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","CIVIL","Mechenical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
         # Course
        Course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="read only")
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
         # year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="read only")
        Year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         # Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="read only")
        Semester_combo["values"]=("Select Semester","semester-1","semester-2","semester-3")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
         # class student information
        Class_Student_frame = LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=10, y=180, width=595, height=243)
        # student id
        Studentid_label=Label(Class_Student_frame,text="Student id:",font=("times new roman",10,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=10,pady=1,sticky=W)
        
        Studentid_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_id,width=20, font=("times new roman", 12, "bold"))
        Studentid_entry.grid(row=0,column=1,padx=5,pady=1,sticky=W)
        
         # student name
        Student_name_label=Label(Class_Student_frame,text="Student name:",font=("times new roman",10,"bold"),bg="white")
        Student_name_label.grid(row=0,column=2,padx=10,pady=1,sticky=W)
        
        Student_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_name,width=20, font=("times new roman", 12, "bold"))
        Student_name_entry.grid(row=0,column=3,padx=5,pady=1,sticky=W)
        
         # Class division
        Class_div_label=Label(Class_Student_frame,text="Class division:",font=("times new roman",10,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=1,sticky=W)
        
        Class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20, font=("times new roman", 12, "bold"))
        Class_div_entry.grid(row=1,column=1,padx=5,pady=1,sticky=W)
        
         # Roll no
        Roll_No_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman",10,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=1,sticky=W)
        
        Roll_No_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20, font=("times new roman", 12, "bold"))
        Roll_No_entry.grid(row=1,column=3,padx=5,pady=1,sticky=W)
        
         # gender
        Gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",10,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=1,sticky=W)
        
        Gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20, font=("times new roman", 12, "bold"))
        Gender_entry.grid(row=2,column=1,padx=5,pady=1,sticky=W)
        
         # DOB
        dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=1,sticky=W)
        
        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=1,sticky=W)
         # EmailS
        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=1,sticky=W)
        
        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=1,sticky=W)
         # phone no
        phone_label=Label(Class_Student_frame,text="Phone no:",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=1,sticky=W)
        
        phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=1,sticky=W)
        
        
        # Adress
        Address_label=Label(Class_Student_frame,text="Address:",font=("times new roman",10,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=1,sticky=W)
        
        Address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20, font=("times new roman", 12, "bold"))
        Address_entry.grid(row=4,column=1,padx=5,pady=1,sticky=W)
        
        # teacher name
        teacher_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=1,sticky=W)
        
        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=5,pady=1,sticky=W)
        
        #radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radionbtn1.grid(row=5,column=0)
        
        self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio2,text="No photo sample",value="NO")
        radionbtn2.grid(row=5,column=1)
        
        # button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=165,width=590,height=40)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        Update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(btn_frame,text="Delete",width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(btn_frame,text="Reset",width=20,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=195,width=590,height=70)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=42,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        Update_Photo_btn=Button(btn_frame1,text="Update Photo Sample",width=42,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Update_Photo_btn.grid(row=0,column=1)
        
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=0,width=610,height=450)
        
        img_right = Image.open("./Images/yes.jpg")
        img_right = img_right.resize((610, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl2 = Label(right_frame, image=self.photoimg_right)
        f_lbl2.place(x=5, y=0, width=610, height=90)
        
        # =========search system==========
        
        Search_frame = LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=90, width=595, height=60)
        
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=1,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),state="read only")
        Search_combo["values"]=("Select","Roll No","Phone_no")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=13, font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0,column=2,padx=5,pady=1,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=3)
        
        ShowAll_btn=Button(Search_frame,text="ShowAll",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=3)
        # ============ table frame==================
        table_frame =Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5, y=154, width=599, height=270)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("id", "dep", "course", "year", "sem", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        # Configure columns
        self.student_table.column("id", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


    def fetch_data(self):
        conn=mysql.connector.connect(host='db',user='user',password='password',database='faceapp',port=3306)   
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        print("Hello here is data");
        print(data)
        
        if len(data) != 0:
            # Clear existing data in the table
            self.student_table.delete(*self.student_table.get_children())
        
            # Insert new data
            for row in data:
                print("hello")
                print (row)
                self.student_table.insert("", END, values=row)
                conn.commit()
        conn.close()    
        
        #========================function declaration===========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
           messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='db',user='user',password='password',database='faceapp',port=3306)   
                my_cursor=conn.cursor()
                query = """
                            INSERT INTO student (
                                    Student_Id, Dep , Course, Year, Semester, Name, Division, Roll, Gender, DOB, Email, Phone, Address, Teacher
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                values = (
                            self.var_id.get(),          # Should be Student_Id
                            self.var_dep.get(),         # Department
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get()
                        )        
                my_cursor.execute(query, values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            
        
            
            
        
        
# Main block to run the application
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
