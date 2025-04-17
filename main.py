from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from db import create_student_table_if_not_exists


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        create_student_table_if_not_exists()
         
        # Load and display first image
        img = Image.open("./Images/neew.jpg")
        img = img.resize((430, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=430, height=130)
        
        # Load and display second image
        img1 = Image.open("./Images/3faces.jpeg")
        img1 = img1.resize((430, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=430, y=0, width=430, height=130)

        # Load and display third image
        img2 = Image.open("./Images/recognition.jpg")
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
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",33,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        
        #student button
        img4 = Image.open("./Images/bg.png")
        img4 = img4.resize((150, 150), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=250,width=150,height=25)
        
        #Detect face button
        img5 = Image.open("./Images/detect face.jpg")
        img5 = img5.resize((150, 150), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=400,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=150,height=25)
        
         #attendance button
        img6 = Image.open("./Images/OIP.jpeg")
        img6 = img6.resize((150, 150), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=650,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="attendance",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=250,width=150,height=25)
        
        #help button
        img7 = Image.open("./Images/helpdesk.png")
        img7 = img7.resize((150, 150), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=900,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Help",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=250,width=150,height=25)
        
        
        #train button
        img8 = Image.open("./Images/trainFace-khom.png")
        img8 = img8.resize((150, 150), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=150,y=330,width=150,height=150)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=473,width=150,height=25)
        
         #photos button
        img9 = Image.open("./Images/photos.jpg")
        img9 = img9.resize((150, 150), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=400,y=330,width=150,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=473,width=150,height=25)
        
        
         #Developer button
        img10 = Image.open("./Images/developer.jpg")
        img10 = img10.resize((150, 150), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=650,y=330,width=150,height=150)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=473,width=150,height=25)
        
         #Exit button
        img11 = Image.open("./Images/exit-sign-neon-style_77399-144.jpg")
        img11 = img11.resize((150, 150), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=900,y=330,width=150,height=150)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2" ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=473,width=150,height=25)
        
         # ===========function===========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
        
        
        
        
# Main block to run the application
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()

