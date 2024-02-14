from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class traindata:
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
        title_lbl = Label(f_lbl, text="Tain Data Module", font=(
            "Roboto", 35, "bold"), bg="#00022D", fg="whitesmoke")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # TRAIN DATA BUTTON
        img3 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\powerbtn.jpg")
        img3 = img3.resize((220, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(f_lbl, image=self.photoimg3, cursor="hand2",
                    command=self.train_classifier)
        b2.place(x=540, y=200, width=220, height=220)

        b2_txt = Button(f_lbl, text="Train data", font=("Roboto", 12, "bold"),
                        bg="black", fg="whitesmoke", cursor="hand2", command=self.train_classifier)
        b2_txt.place(x=540, y=410, width=220, height=30)

    def train_classifier(self):
        data_dir = (r"C:\Users\vansh\vansh\ATTENDANCE\env\imgdata")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            imagenp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow('Training', imagenp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ***************** TRAIN THE CLASSIFIER *****************************************

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Train Datasets Completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = traindata(root)
    root.mainloop()
