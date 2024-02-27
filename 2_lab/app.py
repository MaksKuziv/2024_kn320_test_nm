# спочатку йдуть імпорти бібліотек
from game.sword import Swords
from random import randint 
# опис функціоналу програми у вигляді функцій 

# виконання всієї програми
if __name__ == "__main__":
    print("Start game")
    player1 = input("Enter the name of the first player:")
    c = Swords.create_random_rarity("Катана")
    print(f"Гравець {player1} отримує Меч:", c.info)
    player2 = input("Enter the name of the second player:")
    d = Swords.create_random_rarity("Шпага")
    print(f"Гравець {player2} отримує Меч:", d.info)

    # Дозволимо гравцю впливати на те як ми будемо змагатись на отриманих мечах
    player1_buff = input(f"{player1} ведіть 1 для бафу шкоди, 2 для бафу міцності: ")
    if player1_buff in ["1", "2"]:
        print("Застосовано баф на нанесення шкоди" if player1_buff == "1" else "Застосовано баф на міцність")
    
    # емулюємо як ми користуємось нашим мечем, накладаємо баф, меч старіє/зношується від
    # використання та ми проводимо бої де його міцність зменшується
    c.get_baff_vitality(2)
    print(f"Наклали баф: {c.info}")
    c.aging()
    print(f"Меч почав старіти:: {c.info}")
    d.attack(c)
    print(f"Нас атакували {d.name} з атакою {d.damage}: {c.info}")
    c.expired_buff()
    print(f"Закінчилась дія бафу: {c.info}")
    c.repair(2)
    print(f"Справляємо Меч: {c.info}")
    c.attack(d)
    print(f"Атакували у відповідь: {d.info}")

    if c.vitality > 0 and c.vitality >= d.vitality:
        print(f"Гравець {player1} переміг над {player2}")
    else:
        print(f"Гравець {player2} переміг над {player1}")

    print("End game")
