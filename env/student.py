from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x720+0+0")
        self.root.title("Vigilance Pro")

        # **********************VARIABLES********************************************

        self.var_department = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_PhoneNo = StringVar()
        self.var_Address = StringVar()

        # main background
        img1 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\background.png")
        img1 = img1.resize((1366, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1366, height=720)

        # top label
        title_lbl = Label(f_lbl, text="Student / Employee Management System",
                          font=("Roboto", 35, "bold"), bg="#00022D", fg="whitesmoke")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # main section
        main_frame = Frame(f_lbl, bd=2, bg="whitesmoke")
        main_frame.place(x=30, y=65, width=1300, height=600)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="#628696", relief=RIDGE,
                                text="Student / Employee Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=630, height=580)

        # Current Course Details
        left_frame_dep = LabelFrame(left_frame, bd=2, bg="#628696", relief=RIDGE,
                                    text="Current Course Details", font=("times new roman", 12, "bold"))
        left_frame_dep.place(x=15, y=15, width=600, height=130)

        # Department
        dep_label = Label(left_frame_dep, bg="#628696", text="Department", font=(
            "times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=5, sticky=W)

        dep_combo = ttk.Combobox(left_frame_dep, textvariable=self.var_department, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo['values'] = ('Select Department', "CSE",
                               "IT", "ECE", "EE", "ME", "CE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        Course_label = Label(left_frame_dep, bg="#628696",
                             text="Course", font=("times new roman", 12, "bold"))
        Course_label.grid(row=0, column=2, padx=40, sticky=W)

        Course_combo = ttk.Combobox(left_frame_dep, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Course_combo['values'] = ('Select Course', "B.TECH", "M.TECH", "P.H.D")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # Year
        Year_label = Label(left_frame_dep, bg="#628696",
                           text="Year", font=("times new roman", 12, "bold"))
        Year_label.grid(row=1, column=0, padx=5, sticky=W)

        Year_combo = ttk.Combobox(left_frame_dep, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Year_combo['values'] = ('Select Year', "I", "II", "III", "IV")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_label = Label(left_frame_dep, bg="#628696", text="Semester", font=(
            "times new roman", 12, "bold"))
        Semester_label.grid(row=1, column=2, padx=40, sticky=W)

        Semester_combo = ttk.Combobox(left_frame_dep, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Semester_combo['values'] = (
            'Select Semester', "1", "2", "3", "4", "5", "6", "7", "8",)
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class sudent information
        left_frame_class_sudent = LabelFrame(
            left_frame, bg="#628696", bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        left_frame_class_sudent.place(x=15, y=170, width=600, height=370)

        # student id
        StudentID_label = Label(left_frame_class_sudent, bg="#628696",
                                text="StudentID", font=("times new roman", 12, "bold"))
        StudentID_label.grid(row=0, column=0, padx=5, sticky=W, pady=10)

        StudentID_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_id, width=18, font=(
            "times new roman", 12, "bold"))
        StudentID_entry.grid(row=0, column=1, padx=5, sticky=W, pady=10)

        # student name
        Studentname_label = Label(left_frame_class_sudent, bg="#628696",
                                  text="Student Name", font=("times new roman", 12, "bold"))
        Studentname_label.grid(row=0, column=2, padx=20, sticky=W, pady=10)

        Studentname_entry = ttk.Entry(
            left_frame_class_sudent, textvariable=self.var_name, width=18, font=("times new roman", 12, "bold"))
        Studentname_entry.grid(row=0, column=3, padx=5, sticky=W, pady=10)

        # Class Division
        classdiv_label = Label(left_frame_class_sudent, bg="#628696",
                               text="Class Division", font=("times new roman", 12, "bold"))
        classdiv_label.grid(row=1, column=0, padx=5, sticky=W, pady=10)

        classdiv_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_div, width=18, font=(
            "times new roman", 12, "bold"))
        classdiv_entry.grid(row=1, column=1, padx=5, sticky=W, pady=10)

        # Roll No
        Roll_label = Label(left_frame_class_sudent, bg="#628696",
                           text="Roll No", font=("times new roman", 12, "bold"))
        Roll_label.grid(row=1, column=2, padx=20, sticky=W, pady=10)

        Roll_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_roll, width=18, font=(
            "times new roman", 12, "bold"))
        Roll_entry.grid(row=1, column=3, padx=5, sticky=W, pady=10)

        # Gender
        Gender_label = Label(left_frame_class_sudent, bg="#628696",
                             text="Gender", font=("times new roman", 12, "bold"))
        Gender_label.grid(row=2, column=0, padx=20, sticky=W, pady=10)

        Gender_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_gender, width=18, font=(
            "times new roman", 12, "bold"))
        Gender_entry.grid(row=2, column=1, padx=5, sticky=W, pady=10)

        # DOB
        DOB_label = Label(left_frame_class_sudent, bg="#628696",
                          text="DOB", font=("times new roman", 12, "bold"))
        DOB_label.grid(row=2, column=2, padx=20, sticky=W, pady=10)

        DOB_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_DOB, width=18, font=(
            "times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=5, sticky=W, pady=10)

        # Email
        Email_label = Label(left_frame_class_sudent, bg="#628696",
                            text="Email", font=("times new roman", 12, "bold"))
        Email_label.grid(row=3, column=0, padx=20, sticky=W, pady=10)

        Email_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_Email, width=18, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=5, sticky=W, pady=10)

        # PhoneNo
        PhoneNo_label = Label(left_frame_class_sudent, bg="#628696",
                              text="PhoneNo", font=("times new roman", 12, "bold"))
        PhoneNo_label.grid(row=3, column=2, padx=20, sticky=W, pady=10)

        PhoneNo_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_PhoneNo, width=18, font=(
            "times new roman", 12, "bold"))
        PhoneNo_entry.grid(row=3, column=3, padx=5, sticky=W, pady=10)

        # Address
        Address_label = Label(left_frame_class_sudent, bg="#628696",
                              text="Address", font=("times new roman", 12, "bold"))
        Address_label.grid(row=4, column=0, padx=20, sticky=W, pady=10)

        Address_entry = ttk.Entry(left_frame_class_sudent, textvariable=self.var_Address, width=18, font=(
            "times new roman", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=5, sticky=W, pady=10)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(left_frame_class_sudent, variable=self.var_radio1,
                                    command=self.generate_dataset, text="Take a Photo Sample", value="YES")
        radiobtn1.grid(row=4, column=2, padx=20, sticky=W, pady=10)

        # radio buttons
        radiobtn2 = ttk.Radiobutton(
            left_frame_class_sudent, variable=self.var_radio1, text="No Photo Sample", value="NO")
        radiobtn2.grid(row=4, column=3, padx=5, sticky=W, pady=10)

        # button frame
        button_frame_class_sudent = LabelFrame(
            left_frame_class_sudent, bg="#628696", bd=2, relief=RIDGE)
        button_frame_class_sudent.place(x=15, y=230, width=560, height=100)

        # save button
        save_btn = Button(button_frame_class_sudent, command=self.add_data, text="Save", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=10)
        save_btn.grid(row=0, column=0, pady=10, padx=20)

        # update button
        update_btn = Button(button_frame_class_sudent, text="Update", command=self.update_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        update_btn.grid(row=0, column=1, pady=10, padx=20)

        # delete button
        delete_btn = Button(button_frame_class_sudent, text="Delete", command=self.delete_data, font=(
            "times new roman", 12, "bold"), bg="red", fg="white", width=10)
        delete_btn.grid(row=0, column=2, pady=10, padx=20)

        # Reset button
        Reset_btn = Button(button_frame_class_sudent, text="Reset", command=self.reset_data, font=(
            "times new roman", 12, "bold"), bg="yellow", fg="white", width=10)
        Reset_btn.grid(row=0, column=3, pady=10, padx=20)

        # #take photo sample
        # takephoto_btn=Button(button_frame_class_sudent,command=self.generate_dataset,text="Take a Photo",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        # takephoto_btn.grid(row=1,column=0,pady=5,padx=20)

        # #update photo sample
        # updatephoto_btn=Button(button_frame_class_sudent,text="Update Photo",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        # updatephoto_btn.grid(row=1,column=3,pady=5,padx=20)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="#628696", relief=RIDGE,
                                 text="Student / Employee Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=650, y=10, width=630, height=580)

        # search feature
        search_frame = LabelFrame(right_frame, bd=2, bg="#628696", relief=RIDGE,
                                  text="Search Student / Employee", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=10, width=610, height=70)

        search_label = Label(search_frame, bg="#628696", text="Search By", font=(
            "times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, sticky=W, pady=10)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        search_combo['values'] = ('Select', "Roll NO.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        searchre_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 12, "bold"))
        searchre_entry.grid(row=0, column=2, padx=5, sticky=W, pady=10)

        search_btn = Button(search_frame, text="Search", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=10)
        search_btn.grid(row=0, column=3, pady=5, padx=5)

        showall_btn = Button(search_frame, text="Show All", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        showall_btn.grid(row=0, column=4, pady=5, padx=5)

        # table frame
        table_frame = LabelFrame(right_frame, bd=2, bg="#628696", relief=RIDGE,
                                 text="Records", font=("times new roman", 12, "bold"))
        table_frame.place(x=5, y=100, width=610, height=440)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=('department', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll',
                                          'gender', 'DOB', 'Email', 'PhoneNo', 'Address', 'Image'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('department', text='Department')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('id', text='StudentID')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('div', text='Divison')
        self.student_table.heading('roll', text='RollNo')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('DOB', text='DOB')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('PhoneNo', text='PhoneNo')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Image', text='ImageSampleStatus')
        self.student_table['show'] = 'headings'

        self.student_table.column('department', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('year', width=100)
        self.student_table.column('sem', width=100)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('div', width=100)
        self.student_table.column('roll', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('PhoneNo', width=100)
        self.student_table.column('Address', width=100)
        self.student_table.column('Image', width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # **************************** function deceration ***************************************************

    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='9917', database='vigilancepro')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_Email.get(),
                    self.var_PhoneNo.get(),
                    self.var_Address.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Student Details Has been added Successfully', parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    'Error', f"Due To : {str(es)}", parent=self.root)

    # ************************* FETCH FUNCTION *****************************************************

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='9917', database='vigilancepro')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()

        conn.close()

    # ******************* UPDATE ******************************************

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_PhoneNo.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_radio1.set(data[13])

    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you really want to UPDATE the details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='9917', database='vigilancepro')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,sem=%s,name=%s,`div`=%s,roll=%s,gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Image=%s where id=%s", (
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_Email.get(),
                        self.var_PhoneNo.get(),
                        self.var_Address.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # **************** DELETE FUNC *******************************************

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Invalid student id", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "DELETE STUDENT ID", "Do you really want to delete student data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='9917', database='vigilancepro')
                    my_cursor = conn.cursor()
                    sql = 'DELETE FROM student where id=%s'
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                messagebox.showinfo(
                    "Success", "Student Data Successfully deleted", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # ************************** RESET ******************************
    def reset_data(self):
        self.var_department.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_DOB.set(""),
        self.var_Email.set(""),
        self.var_PhoneNo.set(""),
        self.var_Address.set(""),
        self.var_radio1.set("")

    # ************************* GENERATE DATA SET AND PHOTO SAMPLE **************************************************

    def generate_dataset(self):
        if self.var_department.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='9917', database='vigilancepro')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set department=%s,course=%s,year=%s,sem=%s,name=%s,`div`=%s,roll=%s,gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Image=%s where id=%s", (
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_Email.get(),
                    self.var_PhoneNo.get(),
                    self.var_Address.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()

                # **************************** LOAD PREDEFIEND DATA FROM OPEN CV *************************

                face_classifier = cv2.CascadeClassifier(
                    "C:\\Users\\vansh\\vansh\\ATTENDANCE\\env\\haarcascade_frontalface_default.xml")

                def face_crop(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
                    # scaling factor 1.3
                    # minimum neighbour 5

                    for (x, y, w, h) in faces:
                        face_crop = img[y:y+h, x:x+w]
                        return face_crop

                cap = cv2.VideoCapture(0)
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

                if not cap.isOpened():
                    print("Error: Could not open camera.")
                    messagebox.showerror("Error", "Could not open camera.")
                    return

                img_id = 0
                while True:
                    ret, frame_my = cap.read()
                    if not ret:
                        print("Error: Could not read frame.")
                        messagebox.showerror("Error", "Could not read frame.")
                        break

                    face = face_crop(frame_my)
                    if face is not None:
                        img_id += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:/Users/vansh/vansh/ATTENDANCE/env/imgdata/" + \
                            str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                # cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data Set completed Successfully")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
