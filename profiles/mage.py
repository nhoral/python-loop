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


#player buffs
doNotHaveFrostArmor = Predicate('frost_armor', False)
doNotHaveArcaneIntellect = Predicate('arcane_intellect', False)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)
fearedCharmedSlept = Predicate('fear_charm_sleep_debuff', True)

#player cooldowns
wotfOffCooldown = Predicate('wotf_cooldown', False)
fireBlastOffCooldown = Predicate('fire_blast', False) #WA needs spell ID
frostNovaOffCooldown = Predicate('frost_nova', False) #WA needs spell ID

#player reactions
enemyCastingSpell = Predicate('enemy_casting', True)

#player actions
isNotCasting = Predicate('player_casting', False)

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
castDefaultAttack = Macro([], "1")

##MACROS (keys to use 1,2,3,e,r,f,x,c,v,6,7,8,9,0, -, =, ;, ')
willOfTheForsaken = Macro([ fearedCharmedSlept, wotfOffCooldown ], "0")
castFireBall = Macro ([ isNotCasting ], "e")
castFrostBolt = Macro ([ isNotCasting ], "f")
castArcaneMissiles = Macro([ isNotCasting ], "x")
castArcaneIntellectIfOff = Macro ([ doNotHaveArcaneIntellect, notInCombat ], "9")
castFrostArmorIfOff = Macro ([ doNotHaveFrostArmor, notInCombat ], "8")
castFireBlast = Macro([ fireBlastOffCooldown ], "v")

castFrostNovaWithThreeEnemies = Macro([ frostNovaOffCooldown, threeEnemyInMeleeRange, inCombat ], "7")
castFrostNovaWithFourEnemies = Macro([ frostNovaOffCooldown, fourEnemyInMeleeRange, inCombat ], "7")
castFrostNovaAtLowHealth = Macro([ frostNovaOffCooldown, healthOver20, inCombat ], "7")


# macro order, first macro to be true picks the key to press
macros = [
    
    castFrostArmorIfOff,
    castArcaneIntellectIfOff,
    willOfTheForsaken,
    castFireBall,
    castDefaultAttack
    
]