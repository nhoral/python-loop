from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_L_Y, BUTTON_L_X, BUTTON_Y, BUTTON_R_B


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

#player buffs
battleShoutOff = Predicate('battleshout', False)
inBattleStance = Predicate('battle_stance', True)
#inDefensiveStance = Predicate('defensive_stance', True)
#inBeserkerStance = Predicate('beserker_stance', True)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)

#player cooldowns
shieldBashOffCooldown = Predicate('shield_bash_on_cooldown', False)

#player reactions
enemyCastingSpell = Predicate('enemy_casting', True)

#player actions

#friendly target buffs, debuffs and status
friendlyTargetHealthUnder20 = Predicate('friendly_health_under_20', True) 
friendlyTargetHealthUnder50 = Predicate('friendly_health_under_50', True) 
friendlyTargetHealthUnder75 = Predicate('friendly_health_under_75', True)

#target health
targetHealthUnder20 = Predicate ('target_health_under_20', True)
targetHealthOver20 = Predicate ('target_health_under_20', False)
targetHealthUnder50 = Predicate ('target_health_under_50', True)
targetHealthOver50 = Predicate ('target_health_under_50', False)
targetHealthUnder75 = Predicate ('target_health_under_75', True)
targetHealthOver75 = Predicate ('target_health_under_75', False)

#target Debuffs
rendOff = Predicate('rend', False)
thunderclapOff = Predicate('thunderclap', False)
hamstringOff = Predicate('hamstring', False)
demoralizingRoarOff = Predicate('demoralizing_roar', False)

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
castDefaultAttack = Macro([], "1") #/startattack

##MACROS (keys to use 1,2,3,e,r,f,x,c,v,6,7,8,9,0, -, =, ;, ')
shieldBashIfEnemyCasting = Macro([ enemyCastingSpell, have10Power, shieldBashOffCooldown ], "2")
castBattleShoutIfOff = Macro([ have10Power, battleShoutOff ], "9")
castRendIfOff = Macro([ have10Power, rendOff, inMeleeRange ], "3")
castThunderclapIfOff = Macro([ have20Power, thunderclapOff, inMeleeRange ], "r")
castHamstringIfOff = Macro([ have20Power, hamstringOff, inMeleeRange ], "f")
castHeroicStrike = Macro([ have60Power, inMeleeRange ], "e")
castCharge = Macro([ notInMeleeRange ], "v")
castDemoralzingRoar = Macro([ demoralizingRoarOff, inMeleeRange], "0")

# macro order, first macro to be true picks the key to press
macros = [
    
    #shieldBashIfEnemyCasting,
    castBattleShoutIfOff,
    castRendIfOff,
    castThunderclapIfOff,
    castHamstringIfOff,
    castHeroicStrike,
    castCharge,
    castDefaultAttack
    
]