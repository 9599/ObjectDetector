import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

videoPath = sys.argv[1]
cascPath = sys.argv[2]

video_object = cv2.VideoCapture(videoPath)
carCascade = cv2.CascadeClassifier(cascPath)

j = 1
success = True
while success:
    success,frame = video_object.read()
    if success:
        pathw = "/Users/Gale/Documents/ObjectDetector/return-face/tmpcadur.bmp"
        cv2.imwrite(pathw,frame)
        imagePath = pathw;
        
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cars = carCascade.detectMultiScale(
            gray,
            scaleFactor=1.24,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        print "Found {0} cars!".format(len(cars))
        
        for (x, y, w, h) in cars:
            imgcrop = image[y:(y+h), x:(x+w)]
            cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-car/found-cars/car" + str(j) + ".jpg", imgcrop)
            j = j + 1
            
print("Done!")
