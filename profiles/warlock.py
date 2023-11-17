from macro import Macro, Predicate
from gamepad import BUTTON_X, BUTTON_L_X

immolationOff = Predicate('immolation', False)
castImmolationIfOff = Macro([immolationOff], BUTTON_X)

corruptionOff = Predicate('corruption', False)
castCorruptionIfOff = Macro([corruptionOff], BUTTON_L_X)


# macro order, first macro to be true picks the key to press
macros = [
    castImmolationIfOff,
    castCorruptionIfOff
]