import cv2
import numpy as np
import sys
import os

WINDOW = "Image Processing"
MIN_CUBE_AREA = 5000
MAX_CUBE_AREA = 12000
MIN_BOX_AREA = 12000
MAX_BOX_AREA = 50000

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

colors = {
    "Red": [np.array([0, 120, 70]), np.array([10, 255, 255])],
    "Blue": [np.array([94, 80, 2]), np.array([126, 255, 255])],
    "Green": [np.array([25, 52, 72]), np.array([102, 255, 255])],
    "Yellow": [np.array([20, 100, 100]), np.array([30, 255, 255])],
    "Purple": [np.array([120, 100, 100]), np.array([140, 255, 255])],
    "Pink": [np.array([140, 100, 100]), np.array([160, 255, 255])],
    "Brown": [np.array([10, 100, 20]), np.array([20, 255, 200])],
    "Black": [np.array([0, 0, 0]), np.array([180, 255, 30])]
}

def get_center(contour):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY
    return 0, 0

def main():
    print("Press Q to exit")
    print("Camera opening", end="")
    
    # Proper warmup
    for i in range(10): 
        success, _ = cap.read()
        print("." if success else "x", end="", flush=True)
    print("\nStarting stream...")

    # Set up the window once before the loop
    cv2.namedWindow(WINDOW, cv2.WINDOW_AUTOSIZE)

    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to grab frame.")
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 1. Process all colors and draw them on the frame
        for color_name, (lower, upper) in colors.items():
            mask = cv2.inRange(hsv, lower, upper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
            
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours:
                area = cv2.contourArea(cnt)
                
                if MIN_CUBE_AREA < area < MAX_CUBE_AREA:
                    shape_type = "CUBE (Pick)"
                    cX, cY = get_center(cnt)
                    cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
                    cv2.putText(frame, f"{color_name} {shape_type}", (cX - 20, cY - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)

                elif MIN_BOX_AREA < area < MAX_BOX_AREA:
                    shape_type = "BOX (Place)"
                    cX, cY = get_center(cnt)
                    cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 3)
                    cv2.putText(frame, f"{color_name} {shape_type}", (cX - 20, cY - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        # 2. Show the FINAL frame once per loop
        cv2.imshow(WINDOW, frame)
        
        # 3. Check for exit key once per loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nClosing...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted, exiting...")
    except Exception as e:
        print("\nException:", e)
    finally:
        cap.release()
        cv2.destroyAllWindows()
