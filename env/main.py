from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import traindata
from face_recognition import face_reco
import os


class Face_recoginition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x720+0+0")
        self.root.title("Vigilance Pro")

        # main background
        img1 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\background.png")
        img1 = img1.resize((1366, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1366, height=720)

        # top label
        title_lbl = Label(f_lbl, text="VIGILANCE PRO", font=(
            "Roboto", 35, "bold"), bg="#00022D", fg="whitesmoke")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # student button
        img2 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\user.png")
        img2 = img2.resize((220, 220))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(f_lbl, image=self.photoimg2,
                    command=self.studetails, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b1_txt = Button(f_lbl, text="Student/Employee Details", command=self.studetails,
                        font=("Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b1_txt.place(x=100, y=310, width=220, height=30)

        # 3 button
        img3 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\face-detection.jpg")
        img3 = img3.resize((220, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(f_lbl, image=self.photoimg3, cursor="hand2",
                    command=self.face_recognition)
        b2.place(x=400, y=100, width=220, height=220)

        b2_txt = Button(f_lbl, text="Face Recognition", font=("Roboto", 12, "bold"),
                        bg="black", fg="whitesmoke", cursor="hand2", command=self.face_recognition)
        b2_txt.place(x=400, y=310, width=220, height=30)

        # Attendance button
        img4 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\attendance.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(f_lbl, image=self.photoimg4, cursor="hand2")
        b3.place(x=700, y=100, width=220, height=220)

        b3_txt = Button(f_lbl, text="Attendance", font=(
            "Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b3_txt.place(x=700, y=310, width=220, height=30)

        # Train data button
        img5 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\train data.png")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(f_lbl, image=self.photoimg5, cursor="hand2",
                    command=self.traindatasample)
        b4.place(x=1000, y=100, width=220, height=220)

        b4_txt = Button(f_lbl, text="Train Data", font=("Roboto", 12, "bold"),
                        bg="black", fg="whitesmoke", cursor="hand2", command=self.traindatasample)
        b4_txt.place(x=1000, y=310, width=220, height=30)

        # Number Plate button
        img6 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\numberplate.png")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(f_lbl, image=self.photoimg6, cursor="hand2")
        b5.place(x=100, y=400, width=220, height=220)

        b5_txt = Button(f_lbl, text="Number Plate Recognition", font=(
            "Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b5_txt.place(x=100, y=610, width=220, height=30)

        # Number Plate button
        img7 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\train data.png")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(f_lbl, image=self.photoimg7, cursor="hand2")
        b6.place(x=400, y=400, width=220, height=220)

        b6_txt = Button(f_lbl, text="Number Plate Recognition", font=(
            "Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b6_txt.place(x=400, y=610, width=220, height=30)

        # Number Plate button
        img8 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\train data.png")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b7 = Button(f_lbl, image=self.photoimg8, cursor="hand2")
        b7.place(x=700, y=400, width=220, height=220)

        b7_txt = Button(f_lbl, text="Number Plate Recognition", font=(
            "Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b7_txt.place(x=700, y=610, width=220, height=30)

        # Number Plate button
        img9 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\train data.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b8 = Button(f_lbl, image=self.photoimg9, cursor="hand2")
        b8.place(x=700, y=400, width=220, height=220)

        b8_txt = Button(f_lbl, text="Number Plate Recognition", font=(
            "Roboto", 12, "bold"), bg="black", fg="whitesmoke", cursor="hand2")
        b8_txt.place(x=700, y=610, width=220, height=30)

        # Number Plate button
        img10 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\train data.png")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b9 = Button(f_lbl, image=self.photoimg10,
                    cursor="hand2", command=self.open_img)
        b9.place(x=1000, y=400, width=220, height=220)

        b9_txt = Button(f_lbl, text="Collected Data Sample", font=(
            "Roboto", 12, "bold"), command=self.open_img, bg="black", fg="whitesmoke", cursor="hand2")
        b9_txt.place(x=1000, y=610, width=220, height=30)

    def open_img(self):
        os.startfile(r"C:\Users\vansh\vansh\ATTENDANCE\env\imgdata")


# ************************************** FUNCTION BUTTONS ********************************************************************************

# student details func


    def studetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


# Train data func


    def traindatasample(self):
        self.new_window = Toplevel(self.root)
        self.app = traindata(self.new_window)

# face reco func

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = face_reco(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recoginition_system(root)
    root.mainloop()
