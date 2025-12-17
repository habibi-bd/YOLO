from ultralytics import YOLO

# Load YOLOv11 nano model
model = YOLO("yolo11n.pt")

# Run inference on image
# results = model(
#     "image.png",
#     save=True,
#     show=True,
# )
# print(model.names)

marathon = model.track(
    "marathon.mp4",
    persist=True,
    save=True,
    show=True,
 
)
