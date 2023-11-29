import pyautogui
from PIL import Image
import config
import dxcam

# Setup a dxcam camera if we are on Windows (slightly faster that ImageGrab)
if (config.ADJUST_FOR_RETINA): camera = None
else: camera = dxcam.create()

#Utilities for debugging
def captureScreen():
    screen = pyautogui.screenshot()
    screen.save('__debug__/screen.png')

def captureRegion(left, top, width, height):
    region = pyautogui.screenshot(region=(left, top, width, height))
    region.save('__debug__/region.png')

def captureIcon():
    region = pyautogui.screenshot(region=(0, 0, 28, 28))
    region.save('__debug__/icon.png')


def getCornerRegion(width, height):
    screen = pyautogui.screenshot();
    screenWidth, screenHeight = screen.size 
    
    # Check if we are on Windows or Mac
    if (config.ADJUST_FOR_RETINA):
        left = int(screenWidth / 2) - width
        top = int(screenHeight / 2) - height
    else:
        left = screenWidth - width
        top = screenHeight - height

    return (int(left), int(top), int(width), int(height))

def grabScreenRegion(region):
    # Check if we are on Windows or Mac
    if (config.ADJUST_FOR_RETINA):
        # If Mac, we don't have dxcam, so just use pyautogui
        return pyautogui.screenshot(region=region)
    else:
        # Convert from x, y, width, height to left, top, right, bottom
        dxregion = (region[0], region[1], region[0] + region[2], region[1] + region[3])
    
        # Keep grabbing a frame from the camera until we get one 
        frame = None
        while(frame is None):
            frame = camera.grab(region=dxregion)
    
        # Once we get a frame, convert to image (TODO: We should just find it by comparing two numpy arrays)
        return Image.fromarray(frame)
