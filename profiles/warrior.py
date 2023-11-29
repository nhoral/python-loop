from macro import Macro, Predicate
import config


## PREDICATES
#power meters
have5Power = Predicate('power_5', True)
have10Power = Predicate('power_10', True)
have15Power = Predicate('power_15', True)
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
battleShoutOff = Predicate('battle_shout', False)
inBattleStance = Predicate('battle_stance', True)
notInBattleStance = Predicate('battle_stance', False)
inDefensiveStance = Predicate('defensive_stance', True)
notInDefensiveStance = Predicate('defensive_stance', False)
#inBeserkerStance = Predicate('beserker_stance', True)
inCombat = Predicate('combat', True)
notInCombat = Predicate('combat', False)

#player debuffs
bandageOffCooldown = Predicate('recently_bandaged_debuff', False)

#player cooldowns
shieldBashOffCooldown = Predicate('shield_bash_on_cooldown', False)
tauntOffCooldown = Predicate('taunt_on_cooldown', False)
tauntOnCooldown = Predicate('taunt_on_cooldown', True) 

#player reactions
enemyCastingSpell = Predicate('enemy_casting', True)
revengeIsUsable = Predicate('revenge_usable', True)
overpowerIsUsable = Predicate('overpower_usable', True)
overpowerIsNotUsable = Predicate('overpower_usable', False)

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
demoralizingShoutOff = Predicate('demoralizing_shout', False)
sunderArmorStacksRemain = Predicate('sunder_armor', False)

#target aggro
targetIsAggro = Predicate('target_aggro', True)
targetIsNotAggro = Predicate('target_aggro', False)

#target range
inMeleeRange = Predicate('enemy_in_melee_range', True)
notInMeleeRange = Predicate('enemy_in_melee_range', False)

#enemy proximity - note can't find images
oneEnemyInMeleeRange = Predicate('enemies_1', True)
twoEnemyInMeleeRange = Predicate('enemies_2', True)
threeEnemyInMeleeRange = Predicate('enemies_3', True)
fourEnemyInMeleeRange = Predicate('enemies_4', True)

if (config.IS_KEYBOARD_MODE):
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
    castDemoralzingRoar = Macro([ demoralizingShoutOff, inMeleeRange], "0")
else:
    castDefaultAttack = Macro([], config.GAMEPAD_LEFT, debugName="Default Attack") 

    # Stance independant
    castBattleShoutIfOff = Macro([ have10Power, battleShoutOff ], config.GAMEPAD_UP, debugName="Battle Shout")
    castRendIfOff = Macro([ have10Power, rendOff, inMeleeRange ], config.GAMEPAD_RIGHT, debugName="Rend")
    castRendIfNoAggro = Macro([ notInDefensiveStance, targetIsNotAggro, rendOff, inMeleeRange ], config.GAMEPAD_RIGHT, debugName="Rend No Aggro")
    shieldBashIfEnemyCasting = Macro([ enemyCastingSpell, have10Power, shieldBashOffCooldown ], config.GAMEPAD_DOWN, debugName="Shield Bash")
    castHeroicStrike = Macro([ have60Power, inMeleeRange ], config.GAMEPAD_B, debugName="Heroic Strike")
    castSunderArmorIfNotFiveStacks = Macro([ have15Power, sunderArmorStacksRemain, inMeleeRange ], config.GAMEPAD_L_LEFT, debugName="Sunder Armor")
    castDemoralzingRoarIfOff = Macro([ have10Power, demoralizingShoutOff, inMeleeRange], config.GAMEPAD_R_LEFT, debugName="Demoralizing Shout")
    usePotionIfUnder25 = Macro([ inCombat, healthUnder20 ], config.GAMEPAD_L_X, debugName="Potion")
    
    # Battle Stance
    castThunderclapIfOff = Macro([ have20Power, thunderclapOff, inMeleeRange ], config.GAMEPAD_X, debugName="Thunder Clap")
    castHamstringIfOff = Macro([ have20Power, hamstringOff, inMeleeRange ], config.GAMEPAD_Y, debugName="Hamstring")

    # Switch Into Battle Stance
    castBattleStanceIfOutOfCombat = Macro([ notInBattleStance, notInCombat ], config.GAMEPAD_L_RIGHT, debugName="Battle Stance OOC")

    castBattleStanceIfMockingBlow = Macro([ notInBattleStance, targetIsNotAggro, tauntOnCooldown, inMeleeRange ], config.GAMEPAD_L_RIGHT, debugName="Battle Stance of Mocking Blow")
    castMockingBlowIfTauntDown = Macro([ inBattleStance, have10Power, targetIsNotAggro, tauntOnCooldown, inMeleeRange ], config.GAMEPAD_L_B, debugName="Mocking Blow")

    castBattleStanceIfOverpower = Macro([ notInBattleStance, overpowerIsUsable ], config.GAMEPAD_L_RIGHT, debugName="Battle Stance for Overpower")
    castOverpowerIfUsable = Macro([ inBattleStance, have5Power, inMeleeRange, overpowerIsUsable ], config.GAMEPAD_R_UP, debugName="Overpower")

    # Defensive Stance
    

    # Switch Into Defensive Stance
    castDefensiveStanceForRevenge = Macro([ notInDefensiveStance, overpowerIsNotUsable, revengeIsUsable ], config.GAMEPAD_L_DOWN, debugName='Defense Stance for Revenge')
    castRevengeIfUsable = Macro([ inDefensiveStance, have5Power, inMeleeRange, revengeIsUsable ], config.GAMEPAD_R_DOWN, debugName="Revenge")

    castDefensiveStanceIfLostAggro = Macro([ notInDefensiveStance, targetIsNotAggro, inMeleeRange, tauntOffCooldown ], config.GAMEPAD_L_DOWN, debugName='Defense Stance for Taunt')
    castTauntIfLostAggro = Macro([ inDefensiveStance, targetIsNotAggro, inMeleeRange, tauntOffCooldown ], config.GAMEPAD_L_UP, debugName="Taunt")
    

    #castDemoralzingRoar = Macro([ demoralizingRoarOff, inMeleeRange], "0")

# macro order, first macro to be true picks the key to press
macros = [
    # OOC
    castBattleStanceIfOutOfCombat,

    # Emergency
    usePotionIfUnder25,

    # Silence
    shieldBashIfEnemyCasting,

    # Fight Buff
    castBattleShoutIfOff,
    castDemoralzingRoarIfOff,

    # Taunt and Rend to avoid pre-aggro stance switch
    castRendIfNoAggro,
    castDefensiveStanceIfLostAggro,
    castTauntIfLostAggro,

    # Use Mocking Blow if taunt not ready
    castBattleStanceIfMockingBlow,
    castMockingBlowIfTauntDown,

    # Use Overpower if we can
    castBattleStanceIfOverpower,
    castOverpowerIfUsable,

    # Use Revenge if we can
    castDefensiveStanceForRevenge,
    castRevengeIfUsable,

    # Main loop
    castRendIfOff,
    castSunderArmorIfNotFiveStacks,
    # castThunderclapIfOff, <- Get 3 enemy check?
    castHamstringIfOff,
    castHeroicStrike,
    castDefaultAttack   
]