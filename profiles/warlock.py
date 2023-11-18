from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_Y

isNotCasting = Predicate('casting', False)

immolationOff = Predicate('immolation', False)
castImmolationIfOff = Macro([isNotCasting, immolationOff], BUTTON_B, debugName='Immolation')

corruptionOff = Predicate('corruption', False)
castCorruptionIfOff = Macro([isNotCasting, corruptionOff], BUTTON_L_B, debugName='Corruption')

castShadowBolt = Macro([isNotCasting], BUTTON_Y, debugName='Shadowbolt')

# macro order, first macro to be true picks the key to press
macros = [
    castImmolationIfOff,
    castCorruptionIfOff,
    castShadowBolt
]