from macro import Macro
import predicates
import config

minimumPowerForHealing = predicates.have70Power
# Default attack
castDefaultAttack = Macro([], config.GAMEPAD_LEFT, debugName='default attack')

# Buffs
castFlametoungeIfOff = Macro([ predicates.have50Power, predicates.flametongueIsOff ], config.GAMEPAD_L_X, debugName='castFlametongueIfOff')
castFlametoungeOnOffhand = Macro([ predicates.have50Power, predicates.flametongueOffHandIsOff ], config.GAMEPAD_L_Y, debugName='castFlametoungeOnOffhand')
castRockbiterIfOff = Macro([ predicates.have50Power, predicates.rockbiterIsOff], config.GAMEPAD_RIGHT, debugName='castRockbiterIfOff')
castRockbiterOnOffhand = Macro([ predicates.have50Power, predicates.flametongueOffHandIsOff], config.GAMEPAD_RIGHT, debugName='castRockbiterIfOff')
castStoneskinTotemIfOff = Macro([ predicates.have50Power, predicates.targetHealthOver50, predicates.stoneSkinTotemIsOff, predicates.playerNotMoving, predicates.inMeleeRange ], config.GAMEPAD_Y, debugName='castStoneskinTotemIfOff')
castStrengthTotemIfOff = Macro([ minimumPowerForHealing, predicates.targetHealthOver50, predicates.strengthTotemIsOff, predicates.playerNotMoving, predicates.inMeleeRange ], config.GAMEPAD_L_A, debugName='castStrengthTotemIfOff')
castSearingTotemIfOff = Macro([ minimumPowerForHealing, predicates.targetHealthOver50, predicates.enemyRange20, predicates.searingTotemIsOff, predicates.playerNotMoving ], config.GAMEPAD_L_UP, debugName='castSearingTotemIfOff')
castLightningShieldIfOff = Macro([ minimumPowerForHealing, predicates.lightningShieldIsOff ],config.GAMEPAD_L_DOWN, debugName="castLightningShieldIfOff")
castEarthbindTotemIfFleeing = Macro([ predicates.healthUnder50, predicates.playerIsMoving, predicates.targetIsMoving, predicates.earthbindTotemIsOff ], config.GAMEPAD_B, debugName="castEarthbindTotemIfFleeing")
castStoneclawTotemIfUnder20Health = Macro([ predicates.have10Power, predicates.healthUnder20, predicates.stoneclawTotemIsUsable ], config.GAMEPAD_L_LEFT, debugName="castStoneclawTotemIfUnder20Health")

# Healing
castHealingWaveIfHurt = Macro([ predicates.healthUnder50 ], config.GAMEPAD_DOWN, debugName='castHealingWaveIfHurt')
castHealingWaveOnParty1 = Macro([ predicates.party1Hurt ], config.ACTION_BAR_4_BUTTON_1, debugName='castHealingWaveOnParty1')
castHealingWaveOnParty2 = Macro([ predicates.party2Hurt ], config.ACTION_BAR_4_BUTTON_2, debugName='castHealingWaveOnParty2')
castHealingWaveOnParty3 = Macro([ predicates.party3Hurt ], config.ACTION_BAR_4_BUTTON_3, debugName='castHealingWaveOnParty3')
castHealingWaveOnParty4 = Macro([  predicates.party4Hurt ], config.ACTION_BAR_4_BUTTON_4, debugName='castHealingWaveOnParty4')
cancelHealingWaveIfHealthy = Macro([ predicates.playerIsHealing, predicates.healthOver50, predicates.party1NotHurt, predicates.party2NotHurt, predicates.party3NotHurt, predicates.party4NotHurt ], config.ACTION_BAR_4_BUTTON_5, debugName='cancelHealingWaveIfHealthy')

# Ranged Attack
castLightningBoltIfOver20Power = Macro([ minimumPowerForHealing, predicates.playerNotMoving, predicates.notInMeleeRange ], config.GAMEPAD_UP, debugName='castLightningBoltIfOver20Power')

# Melee Attack
castLavaLashIfUsable = Macro([ predicates.have40Power, predicates.inMeleeRange, predicates.lavaLashIsUsable ], config.GAMEPAD_L_B, debugName='castMoltenBlastIfUsable') 
castFlameshockIfUsable = Macro([ minimumPowerForHealing, predicates.enemyRange20, predicates.flameShockIsUsable ], config.GAMEPAD_L_RIGHT, debugName='castFlameShockIfUable')
castMoltenBlastIfUsable = Macro([ minimumPowerForHealing, predicates.enemyRange20, predicates.moltenBlastIsUsable ], config.GAMEPAD_L_B, debugName='castMoltenBlastIfUsable') 
castEarthShockToSilenceIfUsable = Macro([ predicates.have30Power, predicates.enemyRange20, predicates.earthShockIsUsable, predicates.enemyCastingSpell ], config.GAMEPAD_X, debugName='castEarthShockToSilenceIfUable')

# macro order, first macro to be true picks the key to press
macros = [
    castStoneclawTotemIfUnder20Health,
    #castEarthbindTotemIfFleeing,
    castHealingWaveIfHurt,
    castHealingWaveOnParty1,
    castHealingWaveOnParty2,
    castHealingWaveOnParty3,
    castHealingWaveOnParty4,
    cancelHealingWaveIfHealthy,
    castLightningShieldIfOff,
    #castFlametoungeIfOff,
    castRockbiterIfOff,
    castFlametoungeOnOffhand,
    #castRockbiterOnOffhand,
    castEarthShockToSilenceIfUsable,
    castFlameshockIfUsable,
    castLavaLashIfUsable,
    #castMoltenBlastIfUsable,
    castSearingTotemIfOff,
    castStoneskinTotemIfOff,
    # castStrengthTotemIfOff,
    castLightningBoltIfOver20Power,
    castDefaultAttack
]