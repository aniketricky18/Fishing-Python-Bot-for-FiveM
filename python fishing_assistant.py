import cv2
import numpy as np
import pyautogui
import time
from mss import mss

# Screen + ROI setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
BOX_WIDTH, BOX_HEIGHT = 240, 100
BOX_X, BOX_Y = (SCREEN_WIDTH - BOX_WIDTH) // 2, (SCREEN_HEIGHT - BOX_HEIGHT) // 2

# HSV thresholds
RED_LOWER1 = np.array([0, 50, 50])
RED_UPPER1 = np.array([10, 255, 255])
RED_LOWER2 = np.array([160, 50, 50])
RED_UPPER2 = np.array([180, 255, 255])
WHITE_LOWER = np.array([0, 0, 180])
WHITE_UPPER = np.array([180, 60, 255])

# MSS screen capture region (only ROI for speed)
capture_region = {
    "top": BOX_Y,
    "left": BOX_X,
    "width": BOX_WIDTH,
    "height": BOX_HEIGHT
}

# Pre‑allocate kernel for dilation (if you want early trigger)
KERNEL = np.ones((3, 3), np.uint8)

def detect_and_press(frame):
    hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red mask
    red_mask1 = cv2.inRange(hsv_roi, RED_LOWER1, RED_UPPER1)
    red_mask2 = cv2.inRange(hsv_roi, RED_LOWER2, RED_UPPER2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # White mask
    white_mask = cv2.inRange(hsv_roi, WHITE_LOWER, WHITE_UPPER)

    # Overlap
    overlap = cv2.bitwise_and(red_mask, white_mask)
    overlap_pixels = np.count_nonzero(overlap)

    return overlap_pixels > 1  # slightly higher threshold to avoid noise

def main():
    sct = mss()
    print("🚀 Real-time detection started. Press ESC to stop.")

    last_press_time = 0
    cooldown = 0.25  # seconds between presses

    while True:
        frame = np.array(sct.grab(capture_region))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        current_time = time.time()
        if detect_and_press(frame) and (current_time - last_press_time > cooldown):
            print("✅ Red line on white detected → Pressing E")
            pyautogui.press("e")
            last_press_time = current_time

        # Debug view (optional, comment out for max speed)
        # cv2.rectangle(frame, (0, 0), (BOX_WIDTH, BOX_HEIGHT), (0, 255, 0), 2)
        # cv2.imshow("Debug ROI", frame)
        # if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        #     break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
