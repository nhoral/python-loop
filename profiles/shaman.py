from macro import Macro
import predicates
import config

# Default attack
castDefaultAttack = Macro([], config.GAMEPAD_LEFT, debugName='default attack')

# Buffs
castFlametoungeIfOff = Macro([ predicates.have20Power, predicates.flametongueIsOff ], config.GAMEPAD_L_X, debugName='castFlametongueIfOff')
castFlametoungeOnOffhand = Macro([ predicates.have20Power, predicates.flametongueOffHandIsOff ], config.GAMEPAD_L_Y, debugName='castFlametoungeOnOffhand')
castRockbiterIfOff = Macro([ predicates.have20Power, predicates.rockbiterIsOff], config.GAMEPAD_RIGHT, debugName='castRockbiterIfOff')
castStoneskinTotemIfOff = Macro([ predicates.have20Power, predicates.targetHealthOver50, predicates.stoneSkinTotemIsOff, predicates.playerNotMoving, predicates.inMeleeRange ], config.GAMEPAD_Y, debugName='castStoneskinTotemIfOff')
castStrengthTotemIfOff = Macro([ predicates.have20Power, predicates.targetHealthOver50, predicates.strengthTotemIsOff, predicates.playerNotMoving, predicates.inMeleeRange ], config.GAMEPAD_L_A, debugName='castStrengthTotemIfOff')
castSearingTotemIfOff = Macro([ predicates.have20Power, predicates.targetHealthOver50, predicates.enemyRange20, predicates.searingTotemIsOff, predicates.playerNotMoving ], config.GAMEPAD_L_UP, debugName='castSearingTotemIfOff')
castLightningShieldIfOff = Macro([ predicates.have20Power, predicates.lightningShieldIsOff, predicates.have20Power ],config.GAMEPAD_L_DOWN, debugName="castLightningShieldIfOff")
castEarthbindTotemIfFleeing = Macro([ predicates.healthUnder50, predicates.playerIsMoving, predicates.targetIsMoving, predicates.earthbindTotemIsOff ], config.GAMEPAD_B, debugName="castEarthbindTotemIfFleeing")
castStoneclawTotemIfUnder20Health = Macro([ predicates.have10Power, predicates.healthUnder20, predicates.stoneclawTotemIsUsable ], config.GAMEPAD_L_LEFT, debugName="castStoneclawTotemIfUnder20Health")

# Healing
castHealingWaveIfHurt = Macro([ predicates.healthUnder50 ], config.GAMEPAD_DOWN, debugName='castHealingWaveIfHurt')
castHealingWaveOnParty1 = Macro([ predicates.party1Hurt ], config.GAMEPAD_R_RIGHT, debugName='castHealingWaveOnParty1')

# Ranged Attack
castLightningBoltIfOver20Power = Macro([ predicates.have20Power, predicates.playerNotMoving, predicates.notInMeleeRange ], config.GAMEPAD_UP, debugName='castLightningBoltIfOver20Power')

# Melee Attack
castLavaLashIfUsable = Macro([ predicates.have10Power, predicates.inMeleeRange, predicates.lavaLashIsUsable ], config.GAMEPAD_L_B, debugName='castMoltenBlastIfUsable') 
castFlameshockIfUsable = Macro([ predicates.have20Power, predicates.enemyRange20, predicates.flameShockIsUsable ], config.GAMEPAD_L_RIGHT, debugName='castFlameShockIfUable')
castMoltenBlastIfUsable = Macro([ predicates.have20Power, predicates.enemyRange20, predicates.moltenBlastIsUsable ], config.GAMEPAD_L_B, debugName='castMoltenBlastIfUsable') 
castEarthShockToSilenceIfUsable = Macro([ predicates.have20Power, predicates.enemyRange20, predicates.earthShockIsUsable, predicates.enemyCastingSpell ], config.GAMEPAD_X, debugName='castEarthShockToSilenceIfUable')

# macro order, first macro to be true picks the key to press
macros = [
    castStoneclawTotemIfUnder20Health,
    castEarthbindTotemIfFleeing,
    castHealingWaveIfHurt,
    castHealingWaveOnParty1,
    castLightningShieldIfOff,
    castFlametoungeIfOff,
    castFlametoungeOnOffhand,
    #castRockbiterIfOff,
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