import pyautogui
import time
import keyboard
from gamepad import XboxController
import cv2
import util
import config
from timeit import default_timer as timer

from profiles import warrior
macros = warrior.macros

## Builds a map of all the unique states present in your macros
def getDefaultCombatState(macros):
    combatState = {}

    for macro in macros:
        for predicate in macro.predicates:
            combatState[predicate.stateName] = False

    return combatState

## Loads the images that will be evaluated into memory
def getIconImagesAndPositions(combatState):
    icons = {}
    iconPositions = {}

    for key in combatState:
        image = cv2.imread(config.IMAGES_FOLDER + '/' + key + '.png')

        if (config.ADJUST_FOR_RETINA):
            image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)

        icons[key] = image

        # Initialize the positions to false until we start finding them
        iconPositions[key] = False

    return (icons, iconPositions)

def pressKey(keyToPress):
    if config.DEBUG: print('Sending: ' + keyToPress)
    pyautogui.typewrite(keyToPress)

# Get the corner region to use
region = util.getCornerRegion(config.REGION_WIDTH, config.REGION_HEIGHT)

# Generate a set of unique conditions you are evaluating, based on your macros
combatState = getDefaultCombatState(macros)
iconImages, iconPositions = getIconImagesAndPositions(combatState)

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
        # Debug and benchmarking
        if config.DEBUG: print('Button Pressed')
        if config.BENCHMARKING: start = timer()
        
        screen = util.grabScreenRegion(region)

        for key, val in combatState.items():
            try:
                if (iconPositions[key]):
                    positionSaved = iconPositions[key]
                    pyautogui.locate(iconImages[key], screen.crop(positionSaved), confidence=config.CONFIDENCE)
                    if config.DEBUG: print("Found " + key + " in saved positions")
                else:
                    positionFound = pyautogui.locate(iconImages[key], screen, confidence=config.CONFIDENCE)
                    iconPositions[key] = (
                        positionFound.left,
                        positionFound.top,
                        positionFound.left + positionFound.width,
                        positionFound.top + positionFound.height
                    )
                    if config.DEBUG: print("Saved " + key + " into saved positions")

                combatState[key] = True
            except:
                if config.DEBUG: print(key + ' not found in image')
                combatState[key] = False

        for macro in macros:
            if (macro.predicatesMet(combatState)):
                pressKey(macro.keyToPress)
                break

        if config.BENCHMARKING: 
            print('Loop took ' + str(timer() - start))
    
    time.sleep(0.01)