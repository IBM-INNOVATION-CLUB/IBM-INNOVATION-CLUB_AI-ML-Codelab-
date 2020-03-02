import cv2

#imread allows you to read images
img = cv2.imread('ibm.jpg', 0)

print(img)

#Display image

cv2.imshow('image', img)
#run
#Display image for 5 seconds
cv2.waitKey(5000)
cv2.destroyAllWindows()

#save the image
cv2.imwrite('imb_copy.png', img)
