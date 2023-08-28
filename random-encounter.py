## Random Encounter Simulator

import random

class Player():
    def __init__(self):
        self.hp = 100
        self.mp = 100

    def inputName(self):
        print("What is your name? ")
        self.name = input("> ")

    def chooseMapAction(self):
        print(f'Player: {user.name}')
        print(f'User HP: {user.hp}')
        print(f'User MP:{user.mp}')
        print("--------------------------")

        print("Where do you want to go?")
        self.choice = ["Forward","Back","Right","Left"]
        for x in self.choice:
            print(x)

        self.choice = input("> ").upper()
        print(f"You walked {self.choice}.")

        status = self.rollEvent()

        if status == "stop":
            return
        if status == "proceed":
            self.chooseMapAction()

    def rollEvent(self):
        event = random.randint(0,100)
        if event >= 60:
            print(f"{user.name} encountered a monster!")
            return 'stop'
        else:
            print(f'{user.name} walked without issue.')
            return "proceed"
        

user = Player()

user.inputName()
user.chooseMapAction()

