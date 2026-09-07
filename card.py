from enum import Enum,auto
class CardType(Enum):
    NUMBER=auto()
    FREEZE=auto()
    FLIP_THREE=auto()
    SECOND_CHANCE=auto()
class Card:
    def __init__(self,card_type,value=None):
        self.card_type=card_type
        self.value=value
    def is_number(self):
        return self.card_type==CardType.NUMBER
    def is_action(self):
        return self.card_type!=CardType.NUMBER
    def __str__(self):
        if self.is_number():
            return str(self.value)
        return self.card_type.name.replace("_","").title()
    