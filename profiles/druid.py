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

#player resources points
hasTwoComboPoints = Predicate('combo_2', True)
hasThreeComboPoints = Predicate('combo_3', True)
hasFourComboPoints = Predicate('combo_4', True)
hasFiveComboPoints = Predicate('combo_5', True)

#player buffs
stealthed = Predicate('stealth_buff', True)
outOfStealth = Predicate('stealth_buff', False)
rejuvenationOn = Predicate('rejuvenation', False)
doNotHaveThorns = Predicate('thorns', False)
doNotHaveMarkOfTheWild = Predicate('markofthewild', False)
inBearForm = Predicate('bearform', True)
enraged = Predicate('enrage', True)
inCatForm = Predicate('catform', True)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
isPoisoned = Predicate('poison_debuff', True)
isCursed = Predicate('cursed_debuff', True)
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)
isSlowed = Predicate('slow_debuff', True)

#player cooldowns
warstompOffCooldown = Predicate('warstomp_cooldown', False)

#player reactions
enemyCastingSpell = Predicate('enemy_casting', True)

#player actions
isNotCasting = Predicate('player_casting', False)

#friendly target buffs, debuffs and status
friendlyTargetDoesNotHaveMOTW = Predicate('friendly_MOTW', False) 
friendlyTargetIsPoisoned = Predicate('friendly_poison', True) 
friendlyTargetIsCursed = Predicate('friendly_curse', True)
friendlyTargetHealthUnder20 = Predicate('friendly_health_under_20', True) 
friendlyTargetHealthUnder50 = Predicate('friendly_health_under_50', True) 
friendlyTargetHealthUnder75 = Predicate('friendly_health_under_75', True)
friendlyTargetRejuvenationOff = Predicate('friendly_rejuvenation', False)

#target health
targetHealthUnder20 = Predicate ('target_health_under_20', True)
targetHealthOver20 = Predicate ('target_health_under_20', False)
targetHealthUnder50 = Predicate ('target_health_under_50', True)
targetHealthOver50 = Predicate ('target_health_under_50', False)
targetHealthUnder75 = Predicate ('target_health_under_75', True)
targetHealthOver75 = Predicate ('target_health_under_75', False)

#target Debuffs
moonFireOff = Predicate('moonfire', False)
entangledOff = Predicate('entangling_roots', False) 
demoralizingRoarOff = Predicate('demoralizing_roar', False) 
faerieFireOff = Predicate('fairie_fire', False)

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
castDefaultAttack = Macro([], "e")

##MACROS (keys to use 1,2,3,e,r,f,x,c,v,6,7,8,9,0, -, =, ;, ')
castMoonFireIfOff = Macro([ moonFireOff, have30Power ], '3')
castRejuvenationIfOff = Macro([ rejuvenationOn, have40Power, healthUnder75 ], 'e')
castWrath = Macro ([ have60Power, notInMeleeRange, isNotCasting], 'r')
interuptTargetCast = Macro([ warstompOffCooldown, enemyCastingSpell, inMeleeRange ], "2")
castMarkOfTheWildIfOff = Macro ([ doNotHaveMarkOfTheWild ], "9")
castThornsIfOff = Macro ([ doNotHaveThorns ], "0")

# macro order, first macro to be true picks the key to press
macros = [
    castMarkOfTheWildIfOff,
    castThornsIfOff,
    interuptTargetCast,
    castMoonFireIfOff,
    castWrath,
    castRejuvenationIfOff
]