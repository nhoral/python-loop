from macro import Macro, Predicate

#power meters
have10Power = Predicate('power_10', True)
have20Power = Predicate('power_20', True)
have30Power = Predicate('power_30', True)
have40Power = Predicate('power_40', True)
have50Power = Predicate('power_50', True)
have60Power = Predicate('power_60', True)
have70Power = Predicate('power_70', True)
have80Power = Predicate('power_80', True)
have90Power = Predicate('power_90', True)
have100Power = Predicate('power_100', True)

#health meters
healthUnder20 = Predicate ('health_under_20', True)
healthOver20 = Predicate ('health_under_20', False)
healthUnder50 = Predicate ('health_under_50', True)
healthUnder75 = Predicate ('health_under_75', True)

#enemy proximity - note can't find images
oneEnemyInMeleeRange = Predicate('enemies_1', True)
twoEnemyInMeleeRange = Predicate('enemies_2', True)
threeEnemyInMeleeRange = Predicate('enemies_3', True)
fourEnemyInMeleeRange = Predicate('enemies_4', True)

#target health
targetHealthUnder20 = Predicate ('target_health_under_20', True)
targetHealthOver20 = Predicate ('target_health_under_20', False)
targetHealthUnder50 = Predicate ('target_health_under_50', True)
targetHealthOver50 = Predicate ('target_health_under_50', False)
targetHealthUnder75 = Predicate ('target_health_under_75', True)
targetHealthOver75 = Predicate ('target_health_under_75', False)

#combo points
hasTwoComboPoints = Predicate('combo_2', True)
hasThreeComboPoints = Predicate('combo_3', True)
hasFourComboPoints = Predicate('combo_4', True)
hasFiveComboPoints = Predicate('combo_5', True)

#player buffs
sliceAndDiceDown = Predicate('sliceanddice', False)
stealthed = Predicate('stealth_buff', True)
outOfStealth = Predicate('stealth_buff', False)

#player debuffs
fearedCharmedSlept = Predicate('fear_charm_sleep_debuff', True)

#cooldowns
kickOffCooldown = Predicate('kick_cooldown', False)
evasionOffCooldown = Predicate('evasion_cooldown', False)
gougeOffCooldown = Predicate('gouge_cooldown', False)
gougeOnCooldown = Predicate('gouge_cooldown', True)
bandageOffCooldown = Predicate('bandage_cooldown', False)

#reactions
enemyCastingSpell = Predicate('enemy_casting', True)

#macros
#checkTwoThings = Macro([ hasTwoComboPoints, hasEightyEnergy ], "q")
sliceandiceAtTwoComboPoints = Macro([ hasTwoComboPoints, sliceAndDiceDown, have30Power ], "r")
eviscerateAtThreeComboPoints = Macro([ hasThreeComboPoints, targetHealthUnder20 ], "9")
eviscerateAtFourComboPoints = Macro([ hasFourComboPoints, targetHealthUnder50 ], "9")
eviscerateAtFiveComboPoints = Macro([ hasFiveComboPoints ], "9")
interuptTargetCast = Macro([ kickOffCooldown, enemyCastingSpell, have30Power ], "2")
evasionAt50Health = Macro( [ evasionOffCooldown, healthUnder50 ], "3")
sinisterStrike = Macro([ have40Power], "e")

#default attack
castDefaultAttack = Macro([], "e")

#macros for testing
whisperAtOneEnemy = Macro([ oneEnemyInMeleeRange ], "f")
whisperAtUnder75Health = Macro([ healthUnder75 ], "x")
whisperAtEnemyCastingSpell = Macro([ enemyCastingSpell ],"c") 

# macro order, first macro to be true picks the key to press restarts on success
macros = [
    interuptTargetCast,
    evasionAt50Health,
    sliceandiceAtTwoComboPoints,
    eviscerateAtThreeComboPoints,
    eviscerateAtFourComboPoints,
    eviscerateAtFiveComboPoints,
    sinisterStrike
]