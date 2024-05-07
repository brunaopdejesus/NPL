import cv2

image = cv2.imread('fiap.jpeg')

cv2.imshow('Image Title', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('imagem_salva.jpg', image)
