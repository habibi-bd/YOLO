# YOLO Custom Dataset Training

This repository contains code, configuration, and resources for training YOLO (You Only Look Once) object detection models on custom datasets.

---

## Project Overview

- Fine-tune and train YOLOv8 models on custom datasets
- Annotate images using tools like [CVAT.ai](https://cvat.ai/)
- Organize dataset with a clear folder structure
- Track training experiments and save best weights
- Predict and visualize detections on test images

---

## Folder Structure

```
data 
   images
       train 
          img1.jpg
          img2.jpg
          ....
        val/
          img1.jpg
          img2.jgp
          ......
   labels
      train
         img1.txt
         img2.txt
         .....
        val
           img1.txt
           img2.txt
           ......
```



---

## Dataset Annotation

- Use [CVAT](https://cvat.ai/) or similar tools to label your images
- Export annotations in YOLO format (`.txt` files with class and bounding box info)
- Make sure your `config.yaml` reflects the dataset structure and class names

---

## Quick Start

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```
## Train YOLO model:
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load pre-trained model
model.train(data='data/config.yaml', epochs=100, imgsz=640)

## Predict on new images:
results = model.predict(source='path/to/image.jpg', conf=0.25, save=True)


Notes & Tips

Use Git LFS to track large model files (e.g., .pt weights) to avoid GitHub size limits

Keep runs/ folder in .gitignore to avoid pushing training logs and checkpoints

Experiment with YOLOv8 models (yolov8n.pt, yolov8s.pt, etc.) for better accuracy or speed trade-offs

## References

[Ultralytics YOLO Documentation](https://docs.ultralytics.com/)

[CVAT Annotation Tool](https://www.cvat.ai/)

[Git Large File Storage (LFS)](https://git-lfs.com/)

Contact

Created by Habib | [GitHub](https://github.com/habibi-bd)

