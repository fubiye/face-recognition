import cv2
img = cv2.imread("dog.jpg") 
cv2.imshow("dog", img)
cv2.waitKey()
cv2.destroyAllWindows()
