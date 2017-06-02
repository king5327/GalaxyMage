VERSION = 1

NAME = "Poison"

DESCRIPTION = "Poison your enemy, causing him to lose HP every turn."

ABILITY_TYPE = ACTION

COST = 5

TARGET_TYPE = HOSTILE

RANGE = Diamond(1, 5, 16)

AOE = Single()

EFFECTS = [Status(Status.POISON, power=0.03, duration=5)]

