import cv2
import numpy as np


tracker = cv2.TrackerCSRT_create()
webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()

bounding_box = cv2.selectROI("Select Object then press ENTER", frame, False)
cv2.destroyWindow("Select Object then press ENTER")

tracker.init(frame, bounding_box)

x, y, w, h = [int(box) for box in bounding_box]

template = frame[y:y+h, x:x+w]
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  

while True:

    ret, frame = webcam.read()
    if not ret:
        break
    
    success, bounding_box = tracker.update(frame)

    if success:
        x, y, w, h = [int(box) for box in bounding_box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 255, 0), 2)
        cv2.putText(frame, "Tracking", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 255, 0), 2)
    else:
        cv2.putText(frame, "Searching for object", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      
        result = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:

            y_detect, x_detect = loc[0][0], loc[1][0]
            bounding_box = (x_detect, y_detect, w, h)

            tracker = cv2.TrackerCSRT_create()
            tracker.init(frame, bounding_box)

    cv2.imshow("Tracking", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()