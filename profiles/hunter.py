from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_Y, BUTTON_L_Y

isEnemyInMeleeRange = Predicate('enemy_in_melee_range', True)

raptorStrikeNotOnCooldown = Predicate('raptor_strike_on_cooldown', False)
raptorStrikeIfInMelee = Macro([ raptorStrikeNotOnCooldown, isEnemyInMeleeRange ], BUTTON_L_Y)

huntersMarkOff = Predicate('hunters_mark', False)
casthuntersMarkIfOff = Macro([huntersMarkOff], BUTTON_B, debugName='Hunters Mark')

serpentStringOff = Predicate('serpent_sting', False)
castserpentStringIfOff = Macro([serpentStringOff], BUTTON_L_B, debugName='Serpent String')
 
castDefaultAttack = Macro([], BUTTON_Y)


# macro order, first macro to be true picks the key to press
macros = [
    raptorStrikeIfInMelee,
    casthuntersMarkIfOff,
    castserpentStringIfOff,
    castDefaultAttack
]