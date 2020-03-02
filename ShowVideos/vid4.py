import cv2

cap = cv2.VideoCapture(0);
#get fourcc code using a class
#XVID is for XVID MPEG-4
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#VideoWriter() takes four arguments. Name of output file. and fourcc code(specifies video codec), Frame rate per sec, Sizeof the video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):

    ret, frame = cap.read()

    #ret is boolean and if it's true, save the file
    if ret == True:

        #cap.get() alllows us to get various properties of the video
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        #write frame to a file using an instance of the out variable
        out.write(frame)


        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cap.destroyAllWindows()
