# single-object-tracking
This project implements a real-time object tracking system using YOLOv8n for object detection and the SORT algorithm for tracking.
The system:
- Allows the user to select an object using a bounding box.
- Tracks the object across frames in real-time.
- Displays the tracking results on a live feed.


## Implementation Details

### Detection
I use [YOLOv8n](https://github.com/ultralytics/ultralytics).

### Tracking
[SORT (Simple Online and Realtime Tracking)](https://github.com/abewley/sort) is used for tracking the object across frames by associating detections over time.

### Video Input
Due to webcam limitations on the current device, a pre-recorded video was used. To use a webcam, simply change:

```python
cv2.VideoCapture("demo4.mp4") 
# to 
cv2.VideoCapture(0)
