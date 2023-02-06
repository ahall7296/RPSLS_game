from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name

    def choose_gesture(self):
        self.selected_choice = self.gesture_list