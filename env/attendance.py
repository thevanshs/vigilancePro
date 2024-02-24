from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x720+0+0")
        self.root.title("Vigilance Pro")
 # **********************VARIABLES********************************************

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_roll = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # main background
        img1 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\background.png")
        img1 = img1.resize((1366, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1366, height=720)

        # top label
        title_lbl = Label(f_lbl, text="Attendance Management System", font=(
            "Roboto", 35, "bold"), bg="#00022D", fg="whitesmoke")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # main section
        main_frame = Frame(f_lbl, bd=2, bg="whitesmoke")
        main_frame.place(x=30, y=65, width=1300, height=600)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="#628696", relief=RIDGE,
                                text="Student / Employee Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=630, height=580)

        # Student/Employee Information
        left_frame_class_sudent = LabelFrame(
            left_frame, bg="#628696", bd=2, relief=RIDGE, font=("times new roman", 12, "bold"))
        left_frame_class_sudent.place(x=15, y=10, width=600, height=370)

        # student id
        StudentID_label = Label(left_frame_class_sudent, bg="#628696",
                                text="StudentID", font=("times new roman", 12, "bold"))
        StudentID_label.grid(row=0, column=0, padx=5, sticky=W, pady=10)

        StudentID_entry = ttk.Entry(left_frame_class_sudent, width=18, font=(
            "times new roman", 12, "bold"), textvariable=self.var_id)
        StudentID_entry.grid(row=0, column=1, padx=5, sticky=W, pady=10)

        # student name
        Studentname_label = Label(left_frame_class_sudent, bg="#628696",
                                  text="Student Name", font=("times new roman", 12, "bold"))
        Studentname_label.grid(row=0, column=2, padx=20, sticky=W, pady=10)

        Studentname_entry = ttk.Entry(
            left_frame_class_sudent, width=18, font=("times new roman", 12, "bold"), textvariable=self.var_name)
        Studentname_entry.grid(row=0, column=3, padx=5, sticky=W, pady=10)

        # Department
        classdep_label = Label(left_frame_class_sudent, bg="#628696",
                               text="Department", font=("times new roman", 12, "bold"))
        classdep_label.grid(row=1, column=0, padx=5, sticky=W, pady=10)

        classdep_entry = ttk.Entry(left_frame_class_sudent, width=18, font=(
            "times new roman", 12, "bold"), textvariable=self.var_department)
        classdep_entry.grid(row=1, column=1, padx=5, sticky=W, pady=10)

        # Roll No
        Roll_label = Label(left_frame_class_sudent, bg="#628696",
                           text="Roll No", font=("times new roman", 12, "bold"))
        Roll_label.grid(row=1, column=2, padx=20, sticky=W, pady=10)

        Roll_entry = ttk.Entry(left_frame_class_sudent, width=18, font=(
            "times new roman", 12, "bold"), textvariable=self.var_roll)
        Roll_entry.grid(row=1, column=3, padx=5, sticky=W, pady=10)

        # Time
        Time_label = Label(left_frame_class_sudent, bg="#628696",
                           text="Time", font=("times new roman", 12, "bold"))
        Time_label.grid(row=2, column=0, padx=20, sticky=W, pady=10)

        Time_entry = ttk.Entry(left_frame_class_sudent, width=18, font=(
            "times new roman", 12, "bold"), textvariable=self.var_time)
        Time_entry.grid(row=2, column=1, padx=5, sticky=W, pady=10)

        # Date
        Date_label = Label(left_frame_class_sudent, bg="#628696",
                           text="Date", font=("times new roman", 12, "bold"))
        Date_label.grid(row=2, column=2, padx=20, sticky=W, pady=10)

        Date_entry = ttk.Entry(left_frame_class_sudent, width=18, font=(
            "times new roman", 12, "bold"), textvariable=self.var_date)
        Date_entry.grid(row=2, column=3, padx=5, sticky=W, pady=10)

        # Attendance Status
        Attendance_label = Label(left_frame_class_sudent, bg="#628696", text="Attendance Status", font=(
            "times new roman", 12, "bold"))
        Attendance_label.grid(row=3, column=0, padx=5, sticky=W, pady=10)

        Attendance_combo = ttk.Combobox(left_frame_class_sudent, textvariable=self.var_attendance, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Attendance_combo['values'] = (
            'Select Status', "Present", "Absent")
        Attendance_combo.current(0)
        Attendance_combo.grid(row=3, column=1, padx=5, sticky=W, pady=10)

        # button frame
        button_frame_class_sudent = LabelFrame(
            left_frame, bg="#628696", bd=2, relief=RIDGE)
        button_frame_class_sudent.place(x=30, y=400, width=560, height=65)

        # import_csv_btn
        import_csv_btn = Button(button_frame_class_sudent, text="Import CSV", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=10, command=self.import_csv)
        import_csv_btn.grid(row=0, column=0, pady=10, padx=20)

        # export_csv_btn
        export_csv_btn = Button(button_frame_class_sudent, text="Export CSV", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=10, command=self.export_csv)
        export_csv_btn.grid(row=0, column=1, pady=10, padx=20)

        # update button
        update_btn = Button(button_frame_class_sudent, text="Update", font=(
            "times new roman", 12, "bold"), bg="green", fg="white", width=10)
        update_btn.grid(row=0, column=2, pady=10, padx=20)

        # Reset button
        Reset_btn = Button(button_frame_class_sudent, text="Reset", font=(
            "times new roman", 12, "bold"), bg="tomato", fg="white", width=10, command=self.reset_data)
        Reset_btn.grid(row=0, column=3, pady=10, padx=20)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="#628696", relief=RIDGE,
                                 text="Student / Employee Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=650, y=10, width=630, height=580)

        # table frame
        table_frame = LabelFrame(right_frame, bd=2, bg="#628696", relief=RIDGE,
                                 text="Records", font=("times new roman", 12, "bold"))
        table_frame.place(x=5, y=10, width=610, height=540)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_report_table = ttk.Treeview(table_frame, columns=(
            "id", "name", "department", "roll", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.heading("id", text="Attendance ID")
        self.attendance_report_table.heading("name", text="Name")
        self.attendance_report_table.heading("department", text="Department")
        self.attendance_report_table.heading("roll", text="Roll No")
        self.attendance_report_table.heading("time", text="Time")
        self.attendance_report_table.heading("date", text="Date")
        self.attendance_report_table.heading(
            "attendance", text="Attendance Status")

        self.attendance_report_table["show"] = "headings"
        self.attendance_report_table.column("id", width=100)
        self.attendance_report_table.column("name", width=100)
        self.attendance_report_table.column("department", width=100)
        self.attendance_report_table.column("roll", width=100)
        self.attendance_report_table.column("time", width=100)
        self.attendance_report_table.column("date", width=100)
        self.attendance_report_table.column("attendance", width=120)
        self.attendance_report_table.pack(fill=BOTH, expand=1)

        self.attendance_report_table.bind("<ButtonRelease>", self.get_cursor)

    # ***************************** FETCH DATA ********************************************************

    def face_data(self, rows):
        self.attendance_report_table.delete(
            *self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("", END, values=i)

    def import_csv(self):
        global mydata
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.face_data(mydata)

    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "ERROR", "No data found to be exported", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "SUCCESS", "Data succesfully exported to"+os.path.basename(fln))

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.attendance_report_table.focus()
        content = self.attendance_report_table.item(cursor_focus)
        data = content['values']

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_department.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attendance.set(data[6])

    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_department.set(""),
        self.var_roll.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attendance.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
