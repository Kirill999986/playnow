from items import Item
from character import CharacterWithItems
from character import CharacterStats as stats
Weapon = Item
a = 5
c = a
b = 10
d = b
dem1 = 3
dem2 = 2
player1 = CharacterWithItems(name='Vasya')
player2 = CharacterWithItems(name='Petya')

sword1 = Weapon('Меч Васи', stats={stats.DAMAGE: (a / c) * dem1}, durability=a)
sword2 = Weapon('Меч Пети', stats={stats.DAMAGE: (b / d) * dem2}, durability=b)
player1.set_weapon(sword1)
player2.set_weapon(sword2)

print(player1.stats())
print(player2.stats())
while player1.hp > 0 and player2.hp > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1.stats())
    print(player2.stats())
    a = a - 1
    b = b - 1
    sword1 = Weapon('Меч Васи', stats={stats.DAMAGE: (a / c) * dem1}, durability=a)
    sword2 = Weapon('Меч Пети', stats={stats.DAMAGE: (b / d) * dem2}, durability=b)
    player1.set_weapon(sword1)
    player2.set_weapon(sword2)