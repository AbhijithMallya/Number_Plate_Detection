    import cv2
import numpy as np
#import easyocr

f_width,f_heigth = 700 , 700
plateCascade = cv2.CascadeClassifier(r"D:\Num_2\haarcascade_model.xml")
minArea = 500
cap =cv2.VideoCapture(0)
cap.set(3,f_width)
cap.set(4,f_heigth)
cap.set(10,150)
count = 0
while True:
    success , img  = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            region_of_interest = img[y:y+h,x:x+w]
            cv2.imshow("ROI",region_of_interest)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        cv2.ex
    if cv2.waitKey(1) == 27:
        break  

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Image{}.jpg".format(count),region_of_interest)
        """
        reader = easyocr.Reader(['en'])
        numberplate_text = reader.readtext("Image{}.jpg".format(count),paragraph="False")
        print(numberplate_text)
        """
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
cv2.destroyAllWindows()
