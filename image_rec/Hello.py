import cv2
import numpy as np
# from picamera2 import Picamera2
# import when finalized

# Initialize the camera (0 is usually the USB webcam or PiCamera)
cap = cv2.VideoCapture(0)

# Set camera resolution (Lower resolution is faster on Raspberry Pi)
# 4608x2592@14 FPS  2304x1296@56 FPS  1536x864@120FPS
# Probably 2304x1296 for final code
cap.set(3, 1920)
cap.set(4, 1080)

# Define color ranges in HSV
# format: Color Name: [Lower HSV, Upper HSV]
colors = {
    "Red": [np.array([0, 120, 70]), np.array([10, 255, 255])],
    "Blue": [np.array([94, 80, 2]), np.array([126, 255, 255])],
    "Green": [np.array([25, 52, 72]), np.array([102, 255, 255])]
}

# Define size thresholds to distinguish Cube vs Box
MIN_CUBE_AREA = 500
MAX_CUBE_AREA = 5000
MIN_BOX_AREA = 5000
MAX_BOX_AREA = 50000

def get_center(contour):
    """Calculates the center (x, y) of a contour."""
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY
    return 0, 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert BGR image to HSV for better color processing
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop through each color we want to track
    for color_name, (lower, upper) in colors.items():
        
        # 1. Create a mask for the color
        mask = cv2.inRange(hsv, lower, upper)
        
        # 2. Remove noise (Erosion + Dilation)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # 3. Find Contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            
            # shape_type will identify if it's the item or the container
            shape_type = ""
            
            # Logic: Differentiate Box vs Cube by Size
            if MIN_CUBE_AREA < area < MAX_CUBE_AREA:
                shape_type = "CUBE (Pick)"
                # This (cX, cY) is where the robot arm goes to PICK
                cX, cY = get_center(cnt)
                
                # Visuals
                cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
                cv2.putText(frame, f"{color_name} {shape_type}", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

            elif MIN_BOX_AREA < area < MAX_BOX_AREA:
                shape_type = "BOX (Place)"
                # This (cX, cY) is where the robot arm goes to PLACE
                cX, cY = get_center(cnt)
                
                # Visuals
                cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 3) # Thicker line for box
                cv2.putText(frame, f"{color_name} {shape_type}", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Show the result
    cv2.imshow("Raspberry Pi Tracking", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted, exiting...")
        sys.exit()
    except Exception as e:
        print("Exception:", e)

