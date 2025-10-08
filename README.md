# 🎣 FiveM Fishing Assistant (Python + OpenCV)

An intelligent **fishing automation script for FiveM** built with **Python** and **OpenCV**, designed to detect the in-game fishing minigame in real time and automatically press the interaction key when a successful catch is detected.  

This script leverages **real-time screen capture, HSV color analysis, and AI-optimized logic** to provide fast and accurate responses during the fishing sequence.  

---

## 🚀 Features

✅ **Real-time Screen Detection** – Uses `mss` and `OpenCV` for ultra-fast region-based screen capture.  
✅ **Color-based Logic** – Detects when the red bar overlaps the white zone using HSV color masks.  
✅ **Optimized Performance** – Focuses only on a small Region of Interest (ROI) for better FPS.  
✅ **Automatic Key Press** – Simulates an “E” key press when the target is detected.  
✅ **AI-Optimized** – Fine-tuned with help from AI tools to improve detection speed and reliability.  
✅ **Lightweight & Safe** – No game memory injection, only reads pixels from your screen.  

---

## 🧠 How It Works

1. The script constantly captures a small **region of your screen (ROI)** — centered on your monitor.  
2. It converts the image to the **HSV color space**, which is better for distinguishing colors.  
3. Two color masks are applied:
   - **Red Mask:** Detects the red fishing bar.
   - **White Mask:** Detects the target catch zone.
4. When there’s sufficient overlap between red and white pixels, the script automatically triggers a **key press ("E")**.  
5. The detection runs at a high frame rate, providing near-instant response times.  

---

## 🖥️ Requirements

Before running the script, ensure you have **Python 3.8+** installed.

### Install all dependencies:
```bash
pip install -r requirements.txt
```

### requirements.txt
```
opencv-python
numpy
pyautogui
mss
```

(Optional — pin exact versions for consistency:)
```
opencv-python==4.10.0.84
numpy==1.26.4
pyautogui==0.9.54
mss==9.0.1
```

---

## ⚙️ Configuration

The script automatically adapts to **1366x768 resolution**, but you can modify the ROI for your setup:

```python
SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
BOX_WIDTH, BOX_HEIGHT = 240, 100
BOX_X, BOX_Y = (SCREEN_WIDTH - BOX_WIDTH) // 2, (SCREEN_HEIGHT - BOX_HEIGHT) // 2
```

If you play in a different resolution, adjust these values to center the detection area over your fishing minigame.

---

## 🕹️ Usage

1. **Start the game** and open the fishing minigame.  
2. **Run the script**:
   ```bash
   python fishing_assistant.py
   ```
3. The console will show:
   ```
   🚀 Real-time detection started. Press ESC to stop.
   ```
4. Once the red bar overlaps the white zone, the script will automatically:
   ```
   ✅ Red line on white detected → Pressing E
   ```
5. To stop, simply press **ESC** (if debug mode is active) or close the terminal window.  

---

## 📸 Screenshots

*(Attach screenshots showing your fishing minigame and the ROI region.)*  
These help demonstrate the color areas the script detects.

---

## ⚡ Performance Tips

- Comment out the `cv2.imshow()` debug window for maximum speed.  
- Adjust the **cooldown** parameter for different reaction times:
  ```python
  cooldown = 0.25  # seconds between key presses
  ```
- Fine-tune the HSV values if your game uses different lighting:
  ```python
  RED_LOWER1 = np.array([0, 50, 50])
  RED_UPPER1 = np.array([10, 255, 255])
  RED_LOWER2 = np.array([160, 50, 50])
  RED_UPPER2 = np.array([180, 255, 255])
  WHITE_LOWER = np.array([0, 0, 180])
  WHITE_UPPER = np.array([180, 60, 255])
  ```

---

## 🧩 Code Structure

```
fivem-fishing-assistant/
├── fishing_assistant.py      # Main script
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── screenshots/              # Game screenshots for reference
```

---

## 🤖 AI Assistance

This project was partially optimized using **AI-based performance tuning** — improving detection accuracy, reducing false positives, and making color thresholding more efficient.

---

## ⚠️ Disclaimer

- This script does **not** interact directly with game memory or data.  
- It works entirely through **pixel recognition** and **keyboard automation**, similar to accessibility tools.  
- Use responsibly on servers where such utilities are allowed.  

---

## 💡 Future Plans

- Add configurable GUI for HSV threshold adjustment.  
- Dynamic ROI detection based on mouse clicks.  
- Multi-game mode (for different fishing systems).  
- Integration with sound or vibration triggers.

---

## ❤️ Credits

Created by **Aniket Biswas**  
Special thanks to AI tools and the open-source Python community for inspiration and optimization support.
