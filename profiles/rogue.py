from macro import Macro, Predicate

## PREDICATES
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

#player resource points
hasOneComboPoint = Predicate('combo_1', True)
hasTwoComboPoints = Predicate('combo_2', True)
hasThreeComboPoints = Predicate('combo_3', True)
hasFourComboPoints = Predicate('combo_4', True)
hasFiveComboPoints = Predicate('combo_5', True)

#player buffs
sliceAndDiceDown = Predicate('sliceanddice', False)
stealthed = Predicate('stealth_buff', True)
outOfStealth = Predicate('stealth_buff', False)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
fearedCharmedSlept = Predicate('fear_charm_sleep_debuff', True)
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)

#player cooldowns
kickOffCooldown = Predicate('kick_cooldown', False)
evasionOffCooldown = Predicate('evasion_cooldown', False)
gougeOffCooldown = Predicate('gouge_cooldown', False)
gougeOnCooldown = Predicate('gouge_cooldown', True)
wotfOffCooldown = Predicate('wotf_cooldown', False)
#feintOffCooldown = Predicate('feint_cooldown', False)
#vanishOffCooldown = Predicate('vanish_cooldown', False)

#player reactions
enemyCastingSpell = Predicate('enemy_casting', True)

#target health
targetHealthUnder20 = Predicate ('target_health_under_20', True)
targetHealthOver20 = Predicate ('target_health_under_20', False)
targetHealthUnder50 = Predicate ('target_health_under_50', True)
targetHealthOver50 = Predicate ('target_health_under_50', False)
targetHealthUnder75 = Predicate ('target_health_under_75', True)
targetHealthOver75 = Predicate ('target_health_under_75', False)

#target Debuffs
gougeDebuffOn = Predicate ('gouge_debuff', True)
gougeDebuffOff = Predicate ('gouge_debuff', False)

#target aggro
targetIsAggro = Predicate('target_aggro', True)
targetIsNotAggro = Predicate('target_aggro', False)

#target range
inMeleeRange = Predicate('meleerange', True)
notInMeleeRange = Predicate('meleerange', False)

#enemy proximity - note can't find images
oneEnemyInMeleeRange = Predicate('enemies_1', True)
twoEnemyInMeleeRange = Predicate('enemies_2', True)
threeEnemyInMeleeRange = Predicate('enemies_3', True)
fourEnemyInMeleeRange = Predicate('enemies_4', True)

#default attack
castDefaultAttack = Macro([], "'")

##MACROS (keys to use 1,2,3,e,r,f,x,c,v,6,7,8,9,0, -, =, ;, ')
interuptTargetCast = Macro([ kickOffCooldown, enemyCastingSpell ], "2")

evasionAt50Health = Macro( [ evasionOffCooldown, healthUnder50 ], "3")
willOfTheForsaken = Macro([ fearedCharmedSlept, wotfOffCooldown], "0")
castGougeAt20Health = Macro ([ inCombat, inMeleeRange, healthUnder20, gougeOffCooldown, gougeDebuffOff ], "v")
bandageWhenGouged = Macro ([ gougeDebuffOn, bandageOffCooldown ], "7")
#castVanishAt20Health = Macro([ inCombat, healthUnder20, vanishOffCooldown ], ";")

castGarrote = Macro([ stealthed, have50Power ], "x")

#castFeintWhenAggro([ inCombat, targetIsAggro, feintOffCooldown, have20Power ], "=")

sliceandiceAtTwoComboPoints = Macro([ hasTwoComboPoints, sliceAndDiceDown, targetHealthOver50 ], "r")

eviscerateAtThreeComboPoints = Macro([ hasThreeComboPoints, targetHealthUnder20 ], "9")
eviscerateAtFourComboPoints = Macro([ hasFourComboPoints, targetHealthUnder50 ], "9")
eviscerateAtFiveComboPoints = Macro([ hasFiveComboPoints ], "9")

#ruptureAtXComboPoints
#KidneyShotAtXComboPoints

sinisterStrike = Macro([ have40Power], "e")

# macro order, first macro to be true picks the key to press restarts on success
macros = [
    
    castGougeAt20Health,
    bandageWhenGouged,
    willOfTheForsaken,
    interuptTargetCast,
    evasionAt50Health,
    castGarrote,
    sliceandiceAtTwoComboPoints,
    eviscerateAtThreeComboPoints,
    eviscerateAtFourComboPoints,
    eviscerateAtFiveComboPoints,
    sinisterStrike,
    castDefaultAttack
    
]







