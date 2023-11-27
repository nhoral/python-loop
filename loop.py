import pyautogui
import time
import keyboard
from gamepad import XboxController
import cv2
import platform
import util
import config

from profiles import rogue
macros = rogue.macros

ADJUST_FOR_RETINA =  True if platform.system() == "Darwin" else False

## Builds a map of all the unique states present in your macros
def getDefaultCombatState(macros):
    combatState = {}

    for macro in macros:
        for predicate in macro.predicates:
            combatState[predicate.stateName] = False

    return combatState

## Loads the images that will be evaluated into memory
def getIconImages(combatState):
    icons = {}

    for key in combatState:
        image = cv2.imread(config.IMAGES_FOLDER + '/' + key + '.png')

        if (ADJUST_FOR_RETINA):
            image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)

        icons[key] = image

    return icons

def pressKey(keyToPress):
    if config.DEBUG: print('Sending: ' + keyToPress)
    pyautogui.keyDown(keyToPress) 
    time.sleep(0.001)
    pyautogui.keyUp(keyToPress) 

# util.captureRegion will allow you to capture an image of your region to debug
region = config.REGION
util.captureRegion(config.REGION[0], config.REGION[1], config.REGION[2], config.REGION[3])
#util.captureScreen()

# Generate a set of unique conditions you are evaluating, based on your macros
combatState = getDefaultCombatState(macros)
iconImages = getIconImages(combatState)

## MAIN LOOP
print('Starting')

# If we are in controller mode, get a reference to it, otherwise switch to keyboard mode
if (config.IS_KEYBOARD_MODE == False):
    joy = XboxController()

while (True):
    buttonPressed = keyboard.is_pressed(config.DEFAULT_KEYBOARD_KEY) if config.IS_KEYBOARD_MODE else joy.LeftBumper
    stopButtonPressed = keyboard.is_pressed(config.STOP_KEY)

    if (stopButtonPressed):
        if config.DEBUG: print('Stop Pressed')
        break

    if (buttonPressed):
        if config.DEBUG: print('Button Pressed')
        screen = pyautogui.screenshot(region=region)
        for key, val in combatState.items():
            try:
                # Throws exception if image not found
                pyautogui.locate(iconImages[key], screen, confidence=0.95)
                combatState[key] = True
            except:
                if config.DEBUG: print(key + ' not found in image')
                combatState[key] = False

        for macro in macros:
            if (macro.predicatesMet(combatState)):
                pressKey(macro.keyToPress)
                break
        
    time.sleep(0.05)