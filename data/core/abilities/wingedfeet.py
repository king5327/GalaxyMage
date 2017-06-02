VERSION = 1

NAME = "Winged Feet"

DESCRIPTION = "Increases the movement rate of a unit."

ABILITY_TYPE = ACTION

COST = 10

TARGET_TYPE = FRIENDLY

RANGE = Diamond(0, 5, 16)

AOE = Single()

EFFECTS = [Status(Status.PLUS_MOVE, power=1.0, hit=0.5, duration=5)]

