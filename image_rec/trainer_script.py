from ultralytics import YOLO

# 1. Start with the base Nano model
model = YOLO('yolov8n.pt') 

# 2. Train the AI using your M3 GPU (mps)
# data='data.yaml' is the file you got from Roboflow
model.train(data='data.yaml', epochs=50, imgsz=640, device='mps')

print("Training complete! Your new brain is in 'runs/detect/train/weights/best.pt'")