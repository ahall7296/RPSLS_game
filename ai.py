from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = "Player 2"

    def choose_gesture(self):
        bot_selects = random.choice(self.choice)
        return BOT_SELECTS