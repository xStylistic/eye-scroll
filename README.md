# EyeScroll

Hands free scrolling controlled with your eyes. Sit back and relax and have fun reading! Once running, it works on any webpage or application that has scrolling.

## How to Use

1. Make sure you have a working webcam.
2. Make sure you have a working Python IDE 
3. Clone the repo and run in Main.py. 

## Usage

```python
class EyeTracker:
    """
    up_threshold -> increase for smaller eyes
    down_threshold -> decrease for smaller eyes
    """
    def __init__(self, up_threshold=0.42, down_threshold=0.56):
```
Run the program and in the terminal, it will show your eye ratio when it detects scroll up, down, and neutral. Adjust based on the ratios detected.

Squint eyes to scroll down faster, open eyes wider to scroll up faster. 

## Future Improvements

I want to add a calibration feature when you can change scroll settings without manually changing the numbers. That way it will automatically adjust to the user.

## Libraries Used

- OpenCV
- Mediapipe
- PyQt5
- PyAutoGUI
