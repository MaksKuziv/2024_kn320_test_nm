from .sword import Swords

class SwordBonus: 
    """Описує функціонал бонусів"""
    @staticmethod
    def poison(item):
        if isinstance(item, Swords):
            item.damage += 1
            return f"Застосовано бонус отрути до {item.name}"
        raise ValueError(f"Неможливо застосувати бонус до класу {type(item)}")

    @staticmethod
    def confusion(item):
        if isinstance(item, Swords):
            item.damage += 2
            return f"Застосовано бонус спантеличеність до {item.name}"
        raise ValueError(f"Неможливо застосувати бонус до класу {type(item)}")

    @staticmethod
    def strength(item):
        if isinstance(item, Swords):
            item.vitality += 1
            return f"Застосовано бонус сили. до {item.name}"
        raise ValueError(f"Неможливо застосувати бонус до класу {type(item)}")  