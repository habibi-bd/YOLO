from ultralytics import YOLO
from datetime import datetime


# Load a model
model = YOLO("yolo11n-pose.pt")  # load an official model


# Predict with the model
# results = model("complex_pose.jpg")  # predict on an image
# results = model("marathon.mp4")  # predict on an video

results = model.track(
    "marathon.mp4",
    persist=True,
    save=True,
    show=True,
)
