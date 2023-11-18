from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_L_Y, BUTTON_L_X

have10Rage = Predicate('rage_10', True)
have20Rage = Predicate('rage_20', True)
have30Rage = Predicate('rage_30', True)

battleShoutOff = Predicate('battleshout', False)
castBattleShoutIfOff = Macro([have10Rage, battleShoutOff], BUTTON_B)

rendOff = Predicate('rend', False)
castRendIfOff = Macro([ have10Rage, rendOff ], BUTTON_L_B)

thunderclapOff = Predicate('thunderclap', False)
castThunderclapIfOff = Macro([ have20Rage, thunderclapOff ], BUTTON_L_Y)

hamstringOff = Predicate('hamstring', False)
castHamstringIfOff = Macro([ have10Rage, hamstringOff ], BUTTON_L_X)


# macro order, first macro to be true picks the key to press
macros = [
    castBattleShoutIfOff,
    castThunderclapIfOff,
    castRendIfOff,
    castHamstringIfOff,
]