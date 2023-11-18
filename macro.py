## Macro defintion, containing the criteria to activate, and the key to press when predicates are true
# Example usage:
#     immolationPredicate = Predicate('immolation', True)
#     myMacro = Macro([immolationPredicate], "r")

class Predicate():
    def __init__(self, stateName, shouldBe):
        self.stateName = stateName
        self.shouldBe = shouldBe

class Macro():
    def __init__(self, predicates, keyToPress):
        self.predicates = predicates
        self.keyToPress = keyToPress

    def predicatesMet(self, combatState, debug):
        for predicate in self.predicates:
            # if debug: print(predicate.stateName + ' in combatState is ' + str(combatState[predicate.stateName]))
            if (combatState[predicate.stateName] != predicate.shouldBe):
                # if debug: print(predicate.stateName + ' was not ' + str(predicate.shouldBe))
                return False
        
        return True
    