from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime

class face_reco:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x720+0+0")
        self.root.title("Vigilance Pro")

 # main background
        img1=Image.open(r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\background.png")
        img1=img1.resize((1366,720))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1366,height=720)


        #top label
        title_lbl=Label(f_lbl,text="Face Recognition Module",font=("Roboto",35,"bold"),bg="#00022D",fg="whitesmoke")
        title_lbl.place(x=0,y=0,width=1366,height=50)

        # TFace Recognition BUTTON
        img3=Image.open(r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\powerbtn.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(f_lbl,image=self.photoimg3,cursor="hand2",command=self.reco)
        b2.place(x=540,y=200,width=220,height=220)
       
        b2_txt=Button(f_lbl,text="Detect Face",font=("Roboto",12,"bold"),bg="black",fg="whitesmoke",cursor="hand2",command=self.reco)
        b2_txt.place(x=540,y=410,width=220,height=30)

    # ************************ ATTENDANCE MARKED *************************************************

    def mark_attendance(self,i,j):
        with open(r"C:\Users\vansh\vansh\ATTENDANCE\env\vigilanceAttend.csv","r+",newline="\n") as f:
            mydatalist = f.readlines()
            name_list=[]
            for line in mydatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list)  and (j not in name_list)):
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtstring =  now.strftime("%H:%M:/%S")
                    f.writelines(f"\n{i},{j},{dtstring},{d1},Present")




    #********************* FACE RECO FUNC ***************************************************

    def reco(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, txt, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))

                try:
                    conn = mysql.connector.connect(host='localhost', username='root', password='9917', database='vigilancepro')
                    my_cursor = conn.cursor()

                    my_cursor.execute("select name from student where id=" + str(id))
                    i = my_cursor.fetchone()
                    if i is not None:
                        i = "+".join(i)
                    else:
                        i = ""  # or whatever default value you want

                    my_cursor.execute("select roll from student where id=" + str(id))
                    j = my_cursor.fetchone()
                    if j is not None:
                        j = "+".join(j)
                    else:
                        j = ""  # or whatever default value you want

                    my_cursor.execute("select department from student where id=" + str(id))
                    k = my_cursor.fetchone()
                    if k is not None:
                        k = "+".join(k)
                    else:
                        k = ""  # or whatever default value you want
                    
                    my_cursor.execute("select department from student where id=" + str(id))
                    l = my_cursor.fetchone()
                    if l is not None:
                        l = "+".join(l)
                    else:
                        l = ""  # or whatever default value you want

                    # Repeat this error handling for other queries as well

                except mysql.connector.Error as error:
                    print("Error fetching data from MySQL:", error)
                finally:
                    if conn.is_connected():
                        my_cursor.close()
                        conn.close()

                if confidence > 75:
                    cv2.putText(img, f"Roll No :{j}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name :{i}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0 , 255, 0), 2)
                    self.mark_attendance(j,i)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def reconise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Users\vansh\vansh\ATTENDANCE\env\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\vansh\vansh\ATTENDANCE\classifier.xml")

        video_cap=cv2.VideoCapture(0)
        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()  # Add this line to check the value of ret
            if ret:  # Check if ret is True, indicating a successful frame read
                img=reconise(img,clf,faceCascade)
                cv2.imshow("Vigilance Pro",img)

                if cv2.waitKey(1)==13:
                    break
            else:
                print("Failed to read frame")
                break  # Add this line to indicate when frame reading fails

if __name__ == "__main__":
    root=Tk()
    obj=face_reco(root)
    root.mainloop()