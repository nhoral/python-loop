import pyautogui

#Utilities for debugging
def captureScreen():
    screen = pyautogui.screenshot()
    print(screen.size)
    screen.save('__debug__/screen.png')

def captureRegion(left, top, width, height):
    region = pyautogui.screenshot(region=(left, top, width, height))
    region.save('__debug__/region.png')

def captureMatchedRegion(stateName):
    try:
        screen = pyautogui.screenshot() 
        box = pyautogui.locate('images/' + stateName + '.PNG', screen, confidence=0.95)

        region = pyautogui.screenshot(region=(int(box.left), int(box.top), int(box.width), int(box.height)))
        region.save('__debug__/' + stateName + '_region.png')
    except:
        print(stateName + ' not found')

def getCornerRegion(width, height):
    screen = pyautogui.screenshot();
    screenWidth, screenHeight = screen.size 
    
    left = screenWidth - width
    top = screenHeight - height

    return (int(left), int(top), int(width), int(height))
