from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# actually I want to train the model with the COCO Dataset from 2017 and especially on all kitchen appliences
# results = model.train(data="coco.yaml", epochs=10, imgsz=640)
# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("Datensatz/test2.jpeg")
