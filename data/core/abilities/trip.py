VERSION = 1

NAME = "Trip"

DESCRIPTION = "Knocks down an enemy."

ABILITY_TYPE = ACTION

COST = 5

TARGET_TYPE = HOSTILE

RANGE = Cross(1, 1)

AOE = Single()

EFFECTS = [Status(Status.TRIPPED,duration=3)]
