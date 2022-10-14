class Character:
    def __init__(self, name='', hp=30, damage=1, defence=10):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence

    def attack(self, target):
        target.take_damage(self.damage)

    def take_defence(self, defence):
        self.hp = self.hp +abs(defence)

    def take_damage(self, damage, target):
        if self.defence >= self.damage:
            target.set_defence(self.defence)
        elif self.defence <= self.damage:
            if self.defence == 0:
                self.hp = (self.hp - abs(damage))
            else:
                self.hp = (self.hp - abs(damage))
                target.take_defence(self.defence)
                target.defence(self.defence)


    def stats(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.hp}\n' \
            f' Урон: {self.damage}\n' \
            f' Защита: {self.defence}\n'