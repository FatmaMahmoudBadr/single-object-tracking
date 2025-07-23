import math

import cv2
from ultralytics import YOLO
from sort import sort
import numpy as np

detection_model = YOLO("yolov8n.pt")
tracker = sort.Sort()

video_path = "demo4.mp4"
video = cv2.VideoCapture(video_path)

width = int(video.get(3))
height = int(video.get(4))
fps = int(video.get(cv2.CAP_PROP_FPS))

ret, frame = video.read()
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output_tracking.mp4", fourcc, fps, (width, height))
if ret:
    selected_box = cv2.selectROI("Select Object", frame, False)
    cv2.destroyAllWindows()

    results = detection_model(frame)[0]
    detections = []

    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box.tolist()
        detections.append([x1, y1, x2, y2, conf])

    selected_x, selected_y, selected_width, selected_height = selected_box
    selected_center = np.array([selected_x + selected_width / 2, selected_y + selected_height / 2])

    min_distance = float("inf")
    target_bbox = None
    for det in detections:
        x1, y1, x2, y2, conf = det
        object_center = np.array([(x1 + x2) / 2, (y1 + y2) / 2])
        difference = object_center - selected_center
        distance = math.sqrt(difference[0]**2 + difference[1]**2)
        if distance < min_distance:
            min_distance = distance
            target_bbox = det

    if len(detections) == 0:
        print("no detected objects")
        exit()
    tracks = tracker.update(np.array([target_bbox]))
    target_id = int(tracks[0][4])

    while True:
        ret, frame = video.read()
        if not ret:
            break
        results = detection_model(frame)[0]
        detections = []
        for box in results.boxes.data:
            x1, y1, x2, y2, conf, cls = box.tolist()
            detections.append([x1, y1, x2, y2, conf])

        tracks = tracker.update(np.array(detections))

        for track in tracks:
            x1, y1, x2, y2, track_id = track
            if int(track_id) == target_id:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 3)
                cv2.putText(frame, f"ID: {int(track_id)}", (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

        cv2.imshow("Tracking", frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    out.release()
    cv2.destroyAllWindows()

