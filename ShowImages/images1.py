import cv2

#imread allows you to read images
img = cv2.imread('ibm.jpg', 0)
#Display image

cv2.imshow('image', img)
#run
#Display image for 5 seconds = (5000)
#for 64-bit use the bit key - &0xFF
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()

    #ord() listens for the key passed as argument
elif k == ord('s'):
    #save the image
    cv2.imwrite('imb_copy.png', img)
