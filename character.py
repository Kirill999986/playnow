from haracter import Character
from items import Item
from enum import Enum, auto

class CharacterStats(Enum):
    HP = auto()
    DAMAGE = auto()
    DEFENCE = auto()

class CharacterWithItems(Character):
    def __init__(self, name='', hp=30, damage=1, defence=10):
        Character.__init__(self, name, hp, damage, defence)
        self.defence = defence
        self.weapon = None
        self.armor = None

    def set_weapon(self, item: Item):
        self.weapon = item

    def set_defence(self, damage):
        self.defence = self.defence - abs(damage)

    def defence(self, dafence):
        self.defence = self.defence - abs(dafence)

    def set_armor(self, item: Item):
        self.armor = item

    def attack(self, target):
        try:
            additional_damage = self.weapon.use()[CharacterStats.DAMAGE]
        except Exception:
            additional_damage = 0
        target.take_damage(self.damage + additional_damage)