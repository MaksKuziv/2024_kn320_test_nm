import unittest
from random import randint, choice
from axe import Axe
from swords_bonus import SwordBonus
from sword import Swords
from app import SWORD_NAMES, create_players

# клас для тестування повинен починатись з слова Test
class TestSwordBonus(unittest.TestCase):
    """Починаємо тестування Бонусів для меча"""
    # В даному класі реалізуються всі юніттести у вигляді методів
    # кожен юніттест (назва функції) повинен починатись з префікса імені "test_"
    # оскільки ми працюємо в класі, ми працюємо з методами, і маємо вказівник на обєкт self який містить 
    # весь функціонал батьківського класу TestCase, з якого ми будемо використовувати перевірки assert

    def setUp(self) -> None:
        print("Проводимо початкову ініціалізацію для тестів....")
        self.sw = Axe() # створений макет на який можемо накласти баф отрути
        self.sword = Swords(choice(SWORD_NAMES), "Legend", 1, 1, SwordBonus._nothing) # ми підмінили наш макет на реальний меч
        self.sb = SwordBonus() # імплементація бонусів
        self.d, self.v = self.sw.damag, self.sw.vitality  # Початкове значення характеристик витягуємо через подвійне присвоєння
        return super().setUp()
    
    def tearDown(self) -> None:
        print("Видаляємо обєкти після завершення тестування.")
        del self.sw
        del self.sb
        self.d, self.v = None, None
        return super().tearDown()

    def test_bonus_poison(self):
        """Тестуємо правильність накладення бафу отрути"""
        result = self.sb.bonus_poison(self.sw) # після накладення бонусі наша метод має повернути якись результат
        # нам відомий результат що повертається, тому ми просто перевіряємо результат на рівність
        self.assertEqual(result, f"Застосовано бонус отрути {self.sw.name}", f"Повернене значення {result} не відповідає очікуваному")
        # після накладення бафу отрути наш демедж має збільшитись, 
        # тому перевіряємо що поточно значення шкоди має бути більшим за початкове
        self.assertGreater(self.sw.damag, self.d, "Накладений бонус отрути не збільшив значення шкоди.")

    def test_bonus_strength(self):
        """Тестуємо накладання бафу міцності"""
        result = self.sb.bonus_strength(self.sw)
        self.assertEqual(result, f"Застосовано бонус сили до {self.sw.name}")
        self.assertGreater(self.sw.vitality, self.v, "Накладений бонус міцності не збільшив значення міцності.")
        # Якщо ми передали неправильний обєкт, до якого не можна накласти баф, то ам просто поварнеться значення None
        self.assertIsNone(self.sb.bonus_strength(1), "До цього обєкне не можна застосовувати накладення бафів, неправильний обєкт")
    
    def test_bonus_confusion(self):
        """Тестуємо накладання бафу конфузії"""
        ##### Цей підрозділ робить початкову ініціалізацію
        # Весь цей підрозділ ми можемо винести у спеціальний метод який називається setUp
        #sw = Axe() # створений макет на який можемо накласти баф отрути
        #sb = SwordBonus() # імплементація бонусів
        #d, v = sw.damag, sw.vitality  # Початкове значення характеристик витягуємо через подвійне присвоєння
        
        ##### Це новий підрозділ, де ми власне викликаємо методи який хочемо протестувати
        # передаємо в нього потрібно нам аргументи та записуємо результа
        result = self.sb.bonus_confusion(self.sw)
        
        ##### Це є останній розділів тесту, який власне тустує що ми отримали
        # тут тестуємо що повинна повертати наш метод накладення бафу
        self.assertTrue(isinstance(result, str), "Повернене значення не відповіє стрічковому типу даних")
        self.assertIn(self.sw.name, result, f"Отримана відповідь не вказує не містить {self.sw.name}")
        self.assertIn("бонус", result, "Повернене значення не містить слова бонус")
        
        # тут тестуємо зміни які були здійснені накладанням бафу
        self.assertGreaterEqual(self.sw.damag, self.d, "Баф мав залишити рівним або збільшити значення Нанесення шкоди.")
        self.assertGreaterEqual(self.sw.vitality, self.v, "Баф мав залишити рівним або збільшити значення Міцності.")
        # Якщо ми передали неправильний обєкт, до якого не можна накласти баф, то ам просто поварнеться значення None
        self.assertIsNone(self.sb.bonus_confusion(1), "До цього обєкне не можна застосовувати накладення бафів, неправильний обєкт")
        
    def test_bonus_berserk(self):
        """Тестуємо бонус Берсерка"""
        # Невелика перевірка чи ми дійсько працюємо з Мечем
        self.assertTrue(self.sw.__repr__() is Axe.__repr__(self.sw), f"{self.sw.__repr__()} Не відноситься до класу Меча {Swords.__repr__(self.sw)}")
        # початкова ініціалізація шкоди = 0, тому ставимо якесь значення яке ми хочемо протестувати
        min_damage = 5
        self.sw.damag = randint(min_damage, 10)
        # ініціалізуємо накладання бонусу на Меч
        result = self.sb.bonus_berserk(self.sw)

        # Ефект бурсерка подвоюює атаку, протестуємо це
        self.assertGreater(self.sw.damag, min_damage * 2 - 1) # шкода має бути збільшена
        # і збільшена у 2 рази
        self.assertTrue(self.sw.damag / min_damage >= 2, "Шкода від бафу берсеркера має бути більшою хочаб у 2 рази")
        # значення міцності не посинне бути зміненим і залишитись 0 як було ініціалізовано у класі Axe
        self.assertTrue(self.sw.vitality == 0)
        self.assertIsInstance(result, str, "Повернений результат повинен бути стрічкою.")

    def test_bonus_apply_on_legendary_rarity(self):
        """Тестуємо що для меча з Легендарною ріднісністю буде додано випадковий бонус"""
        # викиристаємо альтернативний конструктор та створимо Легендарний меч
        s = Swords.create_from_rarity(choice(SWORD_NAMES), "Legend")
        self.assertFalse(s.bonus == SwordBonus._nothing.__doc__, f"Легендарна рідкісність повинна мати бонус відмінний від {SwordBonus._nothing.__doc__}")
        # TODO: ЦЕ ТЕСТ НЕ ПРОХОДИТЬ, потрібно фіксити клас де накладаються бафи
        self.assertTrue(s.damag > (3 * Swords.rarity_map["Legend"]) or s.vitality > (5 * Swords.rarity_map["Legend"]), f"Накладений бонус {s.bonus} не збільшив атрибути шкоди {s.damag} або витривалості {s.vitality}")

class TestApplyBuffs(unittest.TestCase):
    """Клас призначений для тестування накладання бафів на меч"""
    def setUp(self) -> None:
        self.s = Swords.create_random_rarity("Тренувальний Меч")
        return super().setUp()
    
    def tearDown(self) -> None:
        del self.s
        return super().tearDown()
    
    def test_get_correct_damage_buff(self):
        """Тестуємо правильність накладання бафу нанесення шкоди"""
        self.assertEqual(self.s.hit, self.s.damag, f"Значення damage {self.s.damag} не рівне значенню hit {self.s.hit}")
        self.s.get_buff_damag(4)
        self.assertGreater(self.s.hit, self.s.damag, "Накладений баф нанесення шкоди НЕ підвищив атрибут нанесення шкоди.")
        self.assertIn(self.s.__hash__, Swords.who_has_buff, f"Неправильно відстежуються накладені бафи в глобальній змінній who_has_buff {Swords.who_has_buff}")


class TestSwordsCreation(unittest.TestCase):
    """В цьому класі ми тестуємо Клас Меча"""
    # давайте не будемо робити в цьому класі початкової ініціалізації для Меча
    # а натомість, в кожному тесті ми просто будемо тестувати інший спосіб створення Меча
    
    def test_create_sword_from_constructor(self):
        """Тестуємо створення меча через основний конструктор класу Swords"""
        d = {'name': 'Тренувальний Меч', 
             'rarity': 'Epic', 
             'damag': 5, 
             'vitality': 10, 
             'bonus': SwordBonus._nothing.__doc__, 
             'buff_damage': 0, 
             'buff_vitality': 0, 
             'debuff': []}
        s = Swords(d["name"], d["rarity"], d["damag"], d["vitality"], SwordBonus._nothing)
        self.assertIsInstance(s, Swords, f"Щось пішло не так і меч не є класу {Swords.__repr__}")
        self.assertDictEqual(d, s.__dict__, f"У стореному Мечі немає базових атрибутів доступних через __dict__ {s.__dict__}")
    
    def test_create_sword_with_correct_rarity(self):
        """Тестуємо правильність сторення меча із задоною характеристикою рідкісності"""
        s = Swords.create_from_rarity("Тренувальний Меч", "Epic")
        self.assertEqual(s.damag, 3*Swords.rarity_map["Epic"], "Неправильно вирахувано величину нанесення шкоди.")
        # наступна перевірка. викличе помилку в ініціалізації Меча, але ми так і хочемо, тому ми виловлюємо цю помилку
        with self.assertRaises(AttributeError):
            Swords.create_from_rarity("Тренувальний Меч", "NonExist")
        # навіть після виникнення помилки, ми продовжуємо тестування
        # тут тестуємо, відповідність присвоєного бонусу відповідно до заданої рідкісності
        self.assertFalse(s.bonus == SwordBonus._nothing.__doc__, "Меч з рідкісністю Epic повинен мати бонус")
        s = Swords.create_from_rarity("Тренувальний Меч", "Green")
        self.assertTrue(s.bonus == SwordBonus._nothing.__doc__, "Меч з рідкісністю Green НЕ повинен мати бонус")

    def test_create_sword_from_random_rarity(self):
        """Тестуємо створення меча з випідковою характеристикою рідкісності"""
        name = 'Тренувальний Меч'
        s = Swords.create_random_rarity(name)
        self.assertIn(s.rarity, Swords.rarity_map.keys(), f"Рідкісність меча не відповідає заданим в {Swords.rarity_map.keys()}.")
        self.assertTrue(s.name == name, "Меч з випадковою рідкіснісю має неправильне Імя.")

    def test_player_creation(monkeypatch):
        """Тестуємо правильність ініціалізаціцї гравців та їх Мечів"""
        # даний тест буде розпізнаватись лише бібліотекою PyTest, unittest його не побачить

        # створюємо гравця
        monkeypatch.setattr('builtins.input', lambda _: "Богдан")
        p = create_players()
        #assert False # Даний тест впаде, ми просто хочемо протестувати чи це буде працювати
        assert isinstance(p, Swords)
        assert p.player == "Богдан"
        assert p.name in SWORD_NAMES




# Ця конструкція if не дозволить запустити цей код якщо ми його імпортнемо в інший файл
if __name__ == '__main__':
    unittest.main(verbosity=2)