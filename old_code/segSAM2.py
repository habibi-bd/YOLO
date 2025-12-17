from ultralytics import SAM
from ultralytics.data.annotator import auto_annotate


# auto_annotate(data="data/video.mp4", det_model="yolo11x.pt", sam_model="sam2_b.pt")
# auto_annotate(data ='dataset/alpaca', det_model = "yolo11x.pt", sam_model = "sam2_b.pt")

model = SAM("sam2_b.pt")
print(model.name)