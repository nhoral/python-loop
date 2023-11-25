from macro import Macro, Predicate
from gamepad import BUTTON_B, BUTTON_L_B, BUTTON_Y, BUTTON_L_Y

## PREDICATES
arcaneIntellect = Predicate('arcane_intellect', True)
arcaneShot = Predicate('arcane_shot_cooldown', True)
battleStance = Predicate('battle_stance', True)
battleShout = Predicate('battleshout', True)
bearForm = Predicate('bearform', True)
catForm = Predicate('catform', True)
combat = Predicate('combat', True)
comboOne = Predicate('combo_1', True)
comboTwo = Predicate('combo_2', True)
comboThree = Predicate('combo_3', True)
comboFour = Predicate('combo_4', True)
comboFive = Predicate('combo_5', True)
corruption = Predicate ('corruption', True) 
curseOfAgony = Predicate ('curse_of_agony', True) 
curseOfWeakness = Predicate ('curse_of_weakness', True)   
cursedDebuff = Predicate('cursed_debuff', True)
demonSkin = Predicate('demon_skin', True)
demoralizingRoar = Predicate('demoralizing_roar', True)
enemiesOne = Predicate('enemies_1', True)
enemiesTwo = Predicate('enemies_2', True)
enemiesThree = Predicate('enemies_3', True)
enemiesFour = Predicate('enemies_4', True)
enemiesFive = Predicate('enemies_5', True)
enemyCasting = Predicate('enemy_casting', True)
meleeRange = Predicate('meleerange', True)
enrage = Predicate('enrage', True)
entanglingRoots = Predicate('entangling_roots', True) 
evasionCooldown = Predicate('evasion_cooldown', True)
faerieFire = Predicate('fairie_fire', True)
fearCharmSleepDebuff = Predicate('fear_charm_sleep_debuff', True)
fireBlast = Predicate('fire_blast', True) #WA needs spell ID
friendlyCurse = Predicate('friendly_curse', True)
friendlyHealthUnder20 = Predicate('friendly_health_under_20', True) 
friendlyHealthUnder50 = Predicate('friendly_health_under_50', True) 
friendlyHealthUnder75 = Predicate('friendly_health_under_75', True)
friendlyMOTW = Predicate('friendly_MOTW', True) 
friendlyPoison = Predicate('friendly_poison', True) 
friendlyRejuvenation = Predicate('friendly_rejuvenation', True)
frostArmor = Predicate('frost_armor', True)
frostNova = Predicate('frost_nova', True) #WA needs spell ID
gougeCooldown = Predicate('gouge_cooldown', True)
gougeDebuff = Predicate ('gouge_debuff', True)
hamstring = Predicate('hamstring', True)
healthUnder20 = Predicate ('health_under_20', True)
healthUnder50 = Predicate ('health_under_50', True)
healthUnder75 = Predicate ('health_under_75', True)
huntersMark = Predicate('hunters_mark', True)
immolation = Predicate ('immolation', True)
impPet = Predicate('imp_pet', True)
kickCooldown = Predicate('kick_cooldown', True)
markOfTheWild = Predicate('markofthewild', True)
meleeRange = Predicate('meleerange', True)
moonFire = Predicate('moonfire', True)
playerCasting = Predicate('player_casting', True)
poisonDebuff = Predicate('poison_debuff', True)
powerTen = Predicate('power_10', True) 
powerTwenty = Predicate('power_20', True) 
powerThirty = Predicate('power_30', True) 
powerFourty = Predicate('power_40', True)
powerFifty = Predicate('power_50', True)
powerSixty = Predicate('power_60', True)
powerSeventy = Predicate('power_70', True)
powerEighty = Predicate('power_80', True)
powerNinety = Predicate('power_90', True)
powerHundred = Predicate('power_100', True)
powerWordFortitude = Predicate('power_word_fortitude', True)
raptorStrikeCooldown = Predicate('raptor_strike_cooldown', True)
recentlyBandagedDebuff = Predicate('recently_bandaged_debuff', True)
rejuvenation = Predicate('rejuvenation', True)
rend = Predicate('rend', True)
serpentSting = Predicate('serpent_sting', True)
shieldBashOnCooldown = Predicate('shield_bash_on_cooldown', True)
sliceAndDice = Predicate('sliceanddice', True)
slowDebuff = Predicate('slow_debuff', True)
stealthBuff = Predicate('stealth_buff', True)
targetAggro = Predicate('target_aggro', True)
targetHealthUnder20 = Predicate ('target_health_under_20', True)
targetHealthUnder50 = Predicate ('target_health_under_50', True)
targetHealthUnder75 = Predicate ('target_health_under_75', True)
thorns = Predicate('thorns', True)
thunderClap = Predicate('thunderclap', True)
warstompCooldown = Predicate('warstomp_cooldown', True)
wotfCooldown = Predicate('wotf_cooldown', True)


##MACROS (keys to use 1,2,3,e,r,f,x,c,v,6,7,8,9,0, -, =, ;, ')
testArcaneIntellect = Macro([ arcaneIntellect ], "1")
testArcaneShot = Macro([ arcaneShot ], "1")
testBattleStance = Macro([ battleStance ], "1")
testBattleShout = Macro([ battleShout ], "1")
testBearForm = Macro([ bearForm ], "1")
testCatForm = Macro([ catForm ], "1")
testCombat = Macro([ combat ], "1")
testComboOne = Macro([ comboOne ], "1") #can't test from /wa
testCorruption = Macro([ corruption ], "1")
testCurseOfAgony = Macro([ curseOfAgony ], "1")
testCurseOfWeakness = Macro([ curseOfWeakness ], "1")
testCursedDebuff = Macro([ cursedDebuff ], "1")
testDemonSkin = Macro([ demonSkin ], "1")
testDemoralizingRoar = Macro([ demoralizingRoar ], "1")
testEnemiesOne = Macro([ enemiesOne ], "1")
testEnemyCasting = Macro([ enemyCasting ], "1")
testMeleeRange = Macro([ meleeRange ], "1")
testEnrage = Macro([ enrage ], "1")
testEntanglingRoots = Macro([ entanglingRoots ], "1")
testEvasionCooldown = Macro([ evasionCooldown ], "1")
testFaerieFire = Macro([ faerieFire ], "1")
testFearCharmSleepDebuff = Macro([ fearCharmSleepDebuff ], "1")
testFireBlast = Macro([ fireBlast ], "1")
testFriendlyCurse = Macro([ friendlyCurse ], "1")
testFriendlyHealthUnder20 = Macro([ friendlyHealthUnder20 ], "1") 
testFriendlyHealthUnder50 = Macro([ friendlyHealthUnder50 ], "1")
testFriendlyHealthUnder75 = Macro([ friendlyHealthUnder75 ], "1")
testFriendlyMOTW = Macro([ friendlyMOTW ], "1") 
testFriendlyPoison = Macro([ friendlyPoison ], "1")
testFriendlyRejuvenation = Macro([ friendlyRejuvenation ], "1")
testFrostArmor = Macro([ frostArmor ], "1")
testFrostNova = Macro([ frostNova ], "1")
testGougeCooldown = Macro([ gougeCooldown ], "1")
testGougeDebuff = Macro([ gougeDebuff ], "1")
testHamstring = Macro([ hamstring ], "1")
testHealthUnder20 = Macro([ healthUnder20 ], "1")
testHealthUnder50 = Macro([ healthUnder50 ], "1")
testHealthUnder75 = Macro([ healthUnder75 ], "1")
testHuntersMark = Macro([ huntersMark ], "1")
testImmolation = Macro([ immolation ], "1")
testImpPet = Macro([ impPet ], "1")
testKickCooldown = Macro([ kickCooldown ], "1")
testMarkOfTheWild = Macro([ markOfTheWild ], "1")
testMeleeRange = Macro([ meleeRange ], "1")
testMoonFire = Macro([ moonFire ], "1")
testPlayerCasting = Macro([ playerCasting ], "1")
testPoisonDebuff = Macro([ poisonDebuff ], "1")
testPowerTen = Macro([ powerTen ], "1")
testPowerTwenty = Macro([ powerTwenty ], "1")
testPowerThirty = Macro([ powerThirty ], "1")
testPowerFourty = Macro([ powerFourty ], "1")
testPowerFifty = Macro([ powerFifty ], "1")
testPowerSixty = Macro([ powerSixty ], "1")
testPowerSeventy = Macro([ powerSeventy ], "1")
testPowerEighty = Macro([ powerEighty ], "1")
testPowerNinety = Macro([ powerNinety ], "1")
testPowerHundred = Macro([ powerHundred ], "1")
testPowerWordFortitude = Macro([ powerWordFortitude ], "1")
testRaptorStrikeCooldown = Macro([ raptorStrikeCooldown ], "1")
testRecentlyBandagedDebuff = Macro([ recentlyBandagedDebuff ], "1")
testRejuvenation = Macro([ rejuvenation ], "1")
testRend = Macro([ rend ], "1")
testSerpentSting = Macro([ serpentSting ], "1")
testShieldBashOnCooldown = Macro([ shieldBashOnCooldown ], "1")
testSliceAndDice = Macro([ sliceAndDice ], "1")
testSlowDebuff = Macro([ slowDebuff ], "1")
testStealthBuff = Macro([ stealthBuff ], "1")
testTargetAggro = Macro([ targetAggro ], "1")
testTargetHealthUnder20 = Macro([ targetHealthUnder20 ], "1")
testTargetHealthUnder50 = Macro([ targetHealthUnder50 ], "1")
testTargetHealthUnder75 = Macro([ targetHealthUnder75 ], "1")
testThorns = Macro([ thorns ], "1")
testThunderClap = Macro([ thunderClap ], "1")
testWarstompCooldown = Macro([ warstompCooldown ], "1")
testWotfCooldown = Macro([ wotfCooldown ], "1")

#Test all macro
testAll = Macro([
    
    arcaneIntellect,
    arcaneShot,
    recentlyBandagedDebuff,
    battleStance,
    battleShout,
    bearForm,
    catForm,
    combat,
    comboOne,
    corruption,
    curseOfAgony,
    curseOfWeakness,
    cursedDebuff,
    demonSkin,
    demoralizingRoar,
    enemiesOne,
    enemyCasting,
    meleeRange,
    enrage,
    entanglingRoots,
    evasionCooldown,
    faerieFire,
    fearCharmSleepDebuff,
    fireBlast,
    friendlyCurse,
    friendlyHealthUnder20, 
    friendlyHealthUnder50,
    friendlyHealthUnder75,
    friendlyMOTW,
    friendlyPoison,
    friendlyRejuvenation,
    frostArmor,
    frostNova,
    gougeCooldown,
    gougeDebuff,
    hamstring,
    healthUnder20,
    healthUnder50,
    healthUnder75,
    huntersMark,
    immolation,
    impPet,
    kickCooldown,
    markOfTheWild,
    meleeRange,
    moonFire,
    playerCasting,
    poisonDebuff,
    powerTen,
    powerTwenty,
    powerThirty,
    powerFourty,
    powerFifty,
    powerSixty,
    powerSeventy,
    powerEighty,
    powerNinety,
    powerHundred,
    powerWordFortitude,
    raptorStrikeCooldown,
    recentlyBandagedDebuff,
    rejuvenation,
    rend,
    serpentSting,
    shieldBashOnCooldown,
    sliceAndDice,
    slowDebuff,
    stealthBuff,
    targetAggro,
    targetHealthUnder20,
    targetHealthUnder50,
    targetHealthUnder75,
    thorns,
    thunderClap,
    warstompCooldown,
    wotfCooldown,
    
    ], "1")


##MACROS
macros = [
    
    testAll
    
]