import cv2
import numpy as numpy

image = cv2.imread('carro.jpg', 0)

ret, thresholded = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)

blurred_image = cv2.GaussianBlur(thresholded, (3, 3), 0)

x = 130
y = 250
w = 190
h = 100

roi = blurred_image[y:y+h, x:x+w]

cv2.imshow('Região de Interessante', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.rectangle(image, (x,y), (x + w, y + h), (255, 0, 255), 5)

cv2.imshow('Imagem Original com ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()