from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_L_Y, BUTTON_L_X, BUTTON_Y, BUTTON_R_B

have10Rage = Predicate('rage_10', True)
have20Rage = Predicate('rage_20', True)
have30Rage = Predicate('rage_30', True)

targetIsNotUndeadOrMechanical = Predicate('undead_or_mechanical', False)
targetIsCasting = Predicate('enemy_casting', True)

shieldBashOffCooldown = Predicate('shield_bash_on_cooldown', False)
shieldBashIfEnemyCasting = Macro([targetIsCasting, have10Rage, shieldBashOffCooldown], BUTTON_R_B, debugName='Shield Bash')

battleShoutOff = Predicate('battleshout', False)
castBattleShoutIfOff = Macro([have10Rage, battleShoutOff], BUTTON_B)

rendOff = Predicate('rend', False)
castRendIfOff = Macro([ have10Rage, rendOff ], BUTTON_L_B)

thunderclapOff = Predicate('thunderclap', False)
castThunderclapIfOff = Macro([ have20Rage, thunderclapOff ], BUTTON_L_Y)

hamstringOff = Predicate('hamstring', False)
castHamstringIfOff = Macro([ have20Rage, hamstringOff ], BUTTON_L_X)

castDefaultAttack = Macro([], BUTTON_Y)

# macro order, first macro to be true picks the key to press
macros = [
    shieldBashIfEnemyCasting,
    castBattleShoutIfOff,
    castThunderclapIfOff,
    castRendIfOff,
    castHamstringIfOff,
    castDefaultAttack
]