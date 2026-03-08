# Single Object Tracking 

## Overview

This project implements a **real-time object tracking system** using a webcam feed.
The user selects an object in the first frame using a bounding box, and the system tracks the object as it moves in the video.

The system is built using **OpenCV's CSRT tracker** and includes an **automatic recovery mechanism** that attempts to find the object again if tracking fails.

---

## Features

* Real-time object tracking using webcam
* Manual object selection using bounding box
* Automatic recovery when tracking fails

---

## Technologies Used

* Python
* OpenCV
* NumPy

---

## Implementation Details

### Object Selection

The user selects the object to track in the first frame using OpenCV's ROI selection tool.

### Object Tracking

The tracking is performed using the **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) tracker**, which is one of the most accurate classical trackers available in OpenCV.

### Automatic Object Recovery

If the tracker loses the object, the system attempts to recover it automatically using **template matching**:

1. The selected object region is stored as a template.
2. When tracking fails, the system searches for the template across the frame using normalized cross-correlation.
3. If the object is detected again, the tracker is reinitialized.

This allows the tracker to recover the object if it temporarily leaves the frame or tracking fails.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/FatmaMahmoudBadr/single-object-tracking.git
cd single-object-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python single_object_tracker.py
```

Steps:

1. The webcam starts.
2. Select the object with the mouse.
3. Press **ENTER** to start tracking.
4. The system tracks the object in real time.
5. Press **Q** to quit.

---

## Future Improvements

* Integrate deep learning detectors (e.g., YOLO) for stronger object re-detection
* Improve robustness to scale and rotation changes
