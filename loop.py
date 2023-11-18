import pyautogui
import time
import keyboard
from gamepad import XboxController
import cv2
import platform
import util

# The macro set you want to run
from profiles import warlock
macros = warlock.macros

ADJUST_FOR_RETINA =  True if platform.system() == "Darwin" else False

DEFAULT_KEY = "e"               # Default key to be pressed if no macros are true
STOP_KEY = "n"                  # Key to stop the python process
DEBUG = True                    # Displays extra logs to help with debugging keys

DEFAULT_KEYBOARD_KEY = 'm'      # Default keyboard key you will press to engage the macros
IS_KEYBOARD_MODE = False        # Whether to listen for keyboard key or controller input

## You can change this function to set the rectangle on the screen you want to check against
def getDefaultRegion(width, height):
    screen = pyautogui.screenshot();
    screenWidth, screenHeight = screen.size 
    
    left = screenWidth - width
    top = screenHeight - height

    return (int(left), int(top), int(width), int(height))

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
        image = cv2.imread('images/' + key + '.PNG')

        if (ADJUST_FOR_RETINA):
            image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)

        icons[key] = image

    return icons

# util.captureRegion will allow you to capture an image of your region to debug
region = getDefaultRegion(500, 500)

# Generate a set of unique conditions you are evaluating, based on your macros
combatState = getDefaultCombatState(macros)
iconImages = getIconImages(combatState)

## MAIN LOOP
print('Starting')

# If we are in controller mode, get a reference to it, otherwise switch to keyboard mode
if (IS_KEYBOARD_MODE == False):
    joy = XboxController()

while (True):
    buttonPressed = keyboard.is_pressed(DEFAULT_KEYBOARD_KEY) if IS_KEYBOARD_MODE else joy.X
    stopButtonPressed = keyboard.is_pressed(STOP_KEY)

    if (stopButtonPressed):
        if DEBUG: print('Stop Pressed')
        break

    if (buttonPressed):
        if DEBUG: print('Button Pressed')
        screen = pyautogui.screenshot(region=region)
        for key, val in combatState.items():
            try:
                # Throws exception if image not found
                pyautogui.locate(iconImages[key], screen, confidence=0.95)
                combatState[key] = True
            except:
                if DEBUG: print(key + ' not found in image')
                combatState[key] = False

        keyToPress = DEFAULT_KEY
        for macro in macros:
            if (macro.predicatesMet(combatState, DEBUG)):
                keyToPress = macro.keyToPress
                break

        if DEBUG: print('Sending: ' + keyToPress)
        pyautogui.keyDown(keyToPress) 
        time.sleep(0.001)
        pyautogui.keyUp(keyToPress) 
        
    time.sleep(0.05)