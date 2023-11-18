from threading import Timer

## Macro defintion, containing the criteria to activate, and the key to press when predicates are true
# Example usage:
#     immolationPredicate = Predicate('immolation', True)
#     myMacro = Macro([immolationPredicate], "r")

class Predicate():
    def __init__(self, stateName, shouldBe):
        self.stateName = stateName
        self.shouldBe = shouldBe

class Macro():
    def __init__(self, predicates, keyToPress, debugName = 'Macro'):
        self.predicates = predicates
        self.keyToPress = keyToPress

        # Debug name for logging 
        self.debugName = debugName

    def predicatesMet(self, combatState, debug):
        # Check the predicates against the combat state
        for predicate in self.predicates:
            if (combatState[predicate.stateName] != predicate.shouldBe):
                if debug: print('predicates failed for ' + self.debugName + ', ' + predicate.stateName + ' was ' + str(combatState[predicate.stateName]) + ' shouldBe ' + str(predicate.shouldBe))
                return False

        # Predicates were met
        if debug: print('predicates met for ' + self.debugName)
        return True
    