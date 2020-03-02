import cv2

#use 0, -1 or 1 (These are device indexes for your camera) or you can pass the file name
cap = cv2.VideoCapture(0);

#Loop to capture the frame continuously
while(True):

    ret, frame = cap.read()
    #cap.read()-creates an instance of cap variable with a read() method
    #ret stores if the variable is true or false
    #frame captures or saves the frame
    #
    #
    #Show image in grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        #if q is pressed, break out of the Loop

cap.release()
cap.destroyAllWindows()
