import cv2
from ultralytics import YOLO

# 1. Load the model (Automatically uses your M3 GPU if available)
model = YOLO('runs/detect/train/weights/best.pt')

# 2. Open MacBook Camera
cap = cv2.VideoCapture(0)

# Set resolution for a balance of speed and detail
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("AI Vision Active. Press 'q' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # 3. Run the AI Tracking
    # device='mps' tells it to use the M3 GPU cores
    results = model.predict(frame, device='mps', conf=0.3, stream=True)

    for r in results:
        # Get detected objects
        boxes = r.boxes
        for box in boxes:
            # Get coordinates for the arm
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            cX, cY = int((x1 + x2) / 2), int((y1 + y2) / 2)
            
            # Get the name of what the AI sees
            cls = int(box.cls[0])
            label = model.names[cls]

            # Logic: If it sees a 'box' or 'cup' (placeholders for your cubes)
            color = (0, 255, 0) if "box" in label.lower() else (255, 0, 0)
            
            # Draw visual feedback
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, f"{label} (Center: {cX},{cY})", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

    cv2.imshow("Hell off a robotic arm AI image Rec.", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
