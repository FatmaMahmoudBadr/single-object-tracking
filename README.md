# single-object-tracking
This project implements a real-time object tracking system using YOLOv8n for object detection and the SORT algorithm for tracking.

## Features
- Real-time object detection with **YOLOv8n**.
- User selects an object in the **first frame** (manual bounding box).
- Tracks the selected object using **SORT tracking algorithm**.
- Displays tracking results with bounding box and ID in real-time.
- Saves the output video with tracking annotations.

---

## Implementation Details

- **Detection**: [YOLOv8n](https://github.com/ultralytics/ultralytics) from Ultralytics is used for detecting objects in each frame.
- **Selection**: The user selects the target object in the first frame via a bounding box (`cv2.selectROI`).
- **Tracking**: [SORT (Simple Online and Realtime Tracking)](https://github.com/abewley/sort) is used for tracking the object across frames by associating detections over time.
- **Saving**: The output video with bounding boxes is saved using `cv2.VideoWriter`, saved as 'output_tracking.mp4'

## Webcam Note
Due to webcam limitations on the current device, a pre-recorded video was used. To use a webcam, simply change:

```python
cv2.VideoCapture("demo4.mp4") 
# to 
cv2.VideoCapture(0)
