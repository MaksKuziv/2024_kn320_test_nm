from game.sword import SwordBonus, Swords

# Створення екземпляра меча
sword = Swords.create_random_rarity("Меч долі")

# Перевірка методів бонусів
for method in SwordBonus.list_bonus_methods():
    print(getattr(SwordBonus, method)(sword))

# Перевірка інформації про меч
print(sword.info)

# Перевірка атаки
print(sword.attack(Swords.create_random_rarity("Зламана зброя")))

# Перевірка парирування
print(sword.parry(10))

# Перевірка старіння
sword.aging()
print(sword.info)

# Перевірка ремонту
print(sword.repair())
print(sword.info)

# Перевірка бафів
sword.get_baff_damage(5)
print(sword.info)
sword.expired_buff()
print(sword.info)

# Перевірка нового бонусу
sword = Swords.create_random_rarity("Могутній меч")
print(SwordBonus.bonus_power(sword))
print(sword.info)