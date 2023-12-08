from macro import Predicate

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
healthOver50 = Predicate ('health_under_50', False)
healthUnder75 = Predicate ('health_under_75', True)

# Party Health
party1Hurt = Predicate("party1_hurt", True)
party1NotHurt = Predicate("party1_hurt", False)
party2Hurt = Predicate("party2_hurt", True)
party2NotHurt = Predicate("party2_hurt", False)
party3Hurt = Predicate("party3_hurt", True)
party3NotHurt = Predicate("party3_hurt", False)
party4Hurt = Predicate("party4_hurt", True)
party4NotHurt = Predicate("party4_hurt", False)

# Moving
playerIsMoving = Predicate('player_moving', True)
playerNotMoving = Predicate('player_moving', False)
targetIsMoving = Predicate('target_moving', True)
playerIsHealing = Predicate('player_healing', True)

#player buffs
flametongueIsOff = Predicate('flametongue', False)
flametongueOffHandIsOff = Predicate('flametongue_offhand', False)
rockbiterIsOff = Predicate('rockbiter', False)
lightningShieldIsOff = Predicate('lightning_shield', False)
earthbindTotemIsOff = Predicate('earthbind_totem', False)
stoneSkinTotemIsOff = Predicate('stoneskin_totem', False)
strengthTotemIsOff = Predicate('strength_totem', False)
searingTotemIsOff = Predicate('searing_totem', False)
stoneclawTotemIsUsable = Predicate('stoneclaw_usable', True)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
isPoisoned = Predicate('poison_debuff', True)
isCursed = Predicate('cursed_debuff', True)
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)
isSlowed = Predicate('slow_debuff', True)

# Cooldowns
lavaLashIsUsable = Predicate('lava_lash', True)
flameShockIsUsable = Predicate('flame_shock', True)
moltenBlastIsUsable = Predicate('molten_blast', True) 
earthShockIsUsable = Predicate('earth_shock', True)

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

#target aggro
targetIsAggro = Predicate('target_aggro', True)
targetIsNotAggro = Predicate('target_aggro', False)

#target range
inMeleeRange = Predicate('enemy_in_melee_range', True)
notInMeleeRange = Predicate('enemy_in_melee_range', False)
enemyRange20 = Predicate('enemy_range_20', True)

#enemy proximity - note can't find images
oneEnemyInMeleeRange = Predicate('enemies_1', True)
twoEnemyInMeleeRange = Predicate('enemies_2', True)
threeEnemyInMeleeRange = Predicate('enemies_3', True)
fourEnemyInMeleeRange = Predicate('enemies_4', True)