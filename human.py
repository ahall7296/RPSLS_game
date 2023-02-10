from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.gesture_list= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]

    def choose_gesture(self, player_one_choice):
        while player_one_choice in human_options:
            human_options = ["0", "1","2","3","4"]
        input("Choose 0 for Rock, 1 for Paper, 2 for Scissor, 3 for Lizard, 4 for Spock ")      
        print(f'You chose option {player_one_choice} which is {self.choice [int(player_one_choice)]}')
        if player_one_choice==0:
            player_one_choice= "Rock"
        elif player_one_choice ==1:
            player_one_choice= "Paper"
        elif player_one_choice == 2:
            player_one_choice= "Scissors"
        elif player_one_choice==3:
            player_one_choice="Lizard"
        elif player_one_choice==4:
            player_one_choice= "Spock"
        else:                     
            print("Please choose another name.")
                
        return player_one_choice
        