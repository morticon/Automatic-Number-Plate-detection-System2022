import cv2
import imutils
import pytesseract

image = cv2.imread('C:\Users\abc\Documents\car_parking_system_MAJOR\Car-Number-Plates-Detection-main\plates')
image = imutils.resize(image,width=300)
cv2.imshow("original image",image)
cv2.waitkey(0)


