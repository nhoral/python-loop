from macro import Macro, Predicate

hasTwoComboPoints = Predicate('combo_2', True)
eviscerateAtTwoComboPoints = Macro([ hasTwoComboPoints ], "r")
# checkTwoThings = Macro([ hasTwoComboPoints, hasEightyEnergy ], "q")

# macro order, first macro to be true picks the key to press
macros = [
    eviscerateAtTwoComboPoints
]