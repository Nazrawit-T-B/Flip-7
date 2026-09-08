class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.frozen=False
        self.second_chance=False
        self.skipped=False
    def addCard(self,card):
        self.hand.append(card)
        if card.is_number():
            self.score+=card.value
    def hasDuplicate(self,card):
        if not card.is_number():
            return False
        return any(c.is_number() and c.value == card.value for c in self.hand)
    def reset(self):
        self.hand.clear()
        self.score=0