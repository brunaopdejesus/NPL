import cv2

image = cv2.imread('fiap.jpeg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

blurred_image = cv2.GaussianBlur(thresh_image, (3, 3), 0)

canny_edges = cv2.Canny(blurred_image, 100, 200)

cv2.imshow('Prepared Image', gray_image)
cv2.waitKey(0)
cv2.imshow('Prepared Image', thresh_image)
cv2.waitKey(0)
cv2.imshow('Prepared Image', blurred_image)
cv2.waitKey(0)
cv2.imshow('Canny Edge Detection', canny_edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite('processed_image.jpg', blurred_image)