import cv2
import os

# Create a folder to save your images
save_path = "competition_data"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)
img_id = 0

print("Point camera at your object. Press 'S' to save, 'Q' to quit.")

while True:
    ret, frame = cap.read()
    cv2.imshow("Data Collector", frame)
    
    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = os.path.join(save_path, f"image_{img_id}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Captured {filename}")
        img_id += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()