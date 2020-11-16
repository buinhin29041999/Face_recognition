import os
import numpy as np
from cv2 import cv2
import PIL.Image
import sqlite3

# insert/update data to sqlite


def insertOrUpdate(Id, Name, IDStudent, BirthDay, Gender, Address):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID = "+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "UPDATE People SET Name='" + \
            str(Name)+"',MaSV='"+str(IDStudent)+"',Birthday='"+str(BirthDay) + \
            "',Gender='"+str(Gender)+"',Address='" + \
            str(Address)+"' WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO People(Id,Name,MaSV,Birthday,Gender,Address) Values(" + \
            str(Id)+",'"+str(Name)+"','"+str(IDStudent)+"','"+str(BirthDay)+"','"+str(Gender)+"','"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()


face_cascade = cv2.CascadeClassifier('lib/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
id = input('ID = ')
name = input('Điền tên: ')
masv = input('Mã sinh viên: ')
ns = input('Ngày sinh: ')
gt = input('Giới tính: ')
dc = input('Địa chỉ: ')
insertOrUpdate(id, name, masv, ns, gt, dc)

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
