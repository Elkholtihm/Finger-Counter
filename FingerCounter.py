import HandTrackingModule as hm
import cv2
import os






def main():
    # initialize previous time and currnent time variables to draw the frame rate
    pTime = 0
    cTime = 0

    # capturing videos via the webcam (used to open a video file or webcam)
    cap = cv2.VideoCapture(0)

    # define an instance of the class
    detector = hm.HandDetector()

    # get images names
    images_names = os.listdir(r'fingers_images')
    listPath = []

    # get images path
    for name in images_names:
        listPath.append(os.path.join(r'fingers_images', name))
    print(listPath)

    # get images representation
    npImage = []
    for path in listPath:
        image = cv2.imread(path)
        resized = cv2.resize(image, (100, 100))
        npImage.append(resized)
    
    # needed landmarks ids
    IdList = [8, 12, 16, 20]
    
    while True:
        # success to whether the frame is successfully read, img capture image 
        success, img = cap.read()

        # use the track methode of the class 
        img, lmlist = detector.Track(img)
        
        # get number of fingers is raised
        if lmlist:
            fingers_num = 0
            for i in IdList:
                if lmlist[i][2] < lmlist[i-1][2]:
                    fingers_num+=1
            if (lmlist[4][1] > lmlist[3][1]) & (lmlist[20][2] < lmlist[19][2]):
                fingers_num+=1

            #  diplay number of fingers raised and 
            print(fingers_num)
            img[0:100, 0:100] = npImage[fingers_num]

        # diplay frame
        cv2.imshow('Image', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

