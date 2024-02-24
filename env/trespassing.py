import cv2
import winsound
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')     
body_cascade = cv2.CascadeClassifier(r"C:\Users\vansh\vansh\ATTENDANCE\env\haarcascade_fullbody.xml")  # Replace "path_to_full_body_cascade.xml" with the path to your full-body cascade XML file

class Trespassing:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x720+0+0")
        self.root.title("Trespassing Detector")

        # main background
        img1 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\background.png")
        img1 = img1.resize((1366, 720))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1366, height=720)

        # top label
        title_lbl = Label(f_lbl, text="Trespassing Module", font=(
            "Roboto", 35, "bold"), bg="#00022D", fg="whitesmoke")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        # Trespassing BUTTON
        img3 = Image.open(
            r"C:\Users\vansh\vansh\ATTENDANCE\env\appimages\powerbtn.jpg")
        img3 = img3.resize((220, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(f_lbl, image=self.photoimg3, cursor="hand2", command=self.detect_movement_window)
        b2.place(x=540, y=200, width=220, height=220)

        b2_txt = Button(f_lbl, text="Detect Movement", font=("Roboto", 12, "bold"),
                        bg="black", fg="whitesmoke", cursor="hand2", command=self.detect_movement_window)
        b2_txt.place(x=540, y=410, width=220, height=30)

    # Function to detect human movement
    def detect_movement(self, frame, roi, face_detected, body_detected):
        # If neither face nor body is detected, return immediately
        if not (face_detected or body_detected):
            return frame

        # Convert frames to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Compute absolute difference between current frame and ROI
        frame_diff = cv2.absdiff(gray_roi, gray_frame)

        # Apply threshold to filter out insignificant movements
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours are detected
        for contour in contours:
            # Compute area of contour
            area = cv2.contourArea(contour)
            
            # Set minimum area threshold for movement detection
            min_area_threshold = 1000
            
            # If contour area exceeds threshold, consider it as movement
            if area > min_area_threshold:
                # Draw bounding box around detected contours
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Display alarm message on screen
                cv2.putText(frame, "Movement Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Play alarm sound
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

        return frame

    # Function to detect faces
    def detect_faces(self, frame):
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

        # Draw bounding box around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Return True if faces are detected, False otherwise
        return len(faces) > 0

    # Function to detect full bodies
    def detect_bodies(self, frame):
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect full bodies
        bodies = body_cascade.detectMultiScale(gray_frame, 1.1, 4)

        # Draw bounding box around detected bodies
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Body', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Return True if bodies are detected, False otherwise
        return len(bodies) > 0
    
    def detect_movement_window(self):
        # Read video stream
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use 0 for webcam, or provide path to video file

        # Capture initial frame for reference
        _, roi = cap.read()

        while True:
            # Read frame from video stream
            ret, frame = cap.read()

            # If frame is not read properly, break the loop
            if not ret:
                break

            # Detect faces and bodies
            face_detected = self.detect_faces(frame)
            body_detected = self.detect_bodies(frame)

            # Detect human movement only if a face or body is detected
            frame = self.detect_movement(frame, roi, face_detected, body_detected)

            # Display resulting frame
            cv2.imshow("Human Movement Detection", frame)

            # Check for key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):  # Press 'q' to exit
                break


if __name__ == "__main__":
    root = Tk()
    obj = Trespassing(root)
    root.mainloop()
