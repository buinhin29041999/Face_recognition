import os
import numpy as np
from cv2 import cv2
import PIL.Image
import sqlite3

# insert/update data to sqlite


def insertOrUpdate(Id, Name, IDStudent, Gender):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID = "+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "UPDATE People SET Name='" + \
            str(Name)+"',MaSV='"+str(IDStudent)+"',Gender='"+str(Gender)+"' WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO People(Id,Name,MaSV,Gender) Values(" + \
            str(Id)+",'"+str(Name)+"','"+str(IDStudent)+"','"+str(Gender)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()


face_cascade = cv2.CascadeClassifier('lib/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
id = input('ID = ')
name = input('Điền tên: ')
masv = input('Mã sinh viên: ')
gt = input('Giới tính: ')

insertOrUpdate(id, name, masv, gt)

sampleN = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleN = sampleN+1
        cv2.imwrite("facesData/User." + str(id) + "." +
                    str(sampleN) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.waitKey(150)
    cv2.imshow('Face', img)
    cv2.waitKey(1)
    if sampleN >= 100:
        break
cap.release()
cv2.destroyAllWindows()
