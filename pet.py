class pet:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self,name):
        self.name = name
        self.hunger = 0
        self.energy = 0
        self.happiness = 0
        self.tricks= []
    def eat(self):
        #  reduces hunger by 3 points (but not below 0), and increases happiness by 1.
        if self.happiness <= 10:
            self.happiness += 1
        else: 
            pass
        if self.hunger >= 3:
            self.hunger -=3
        elif self.hunger == 2:
            self.hunger -=2
        elif self.hunger == 1:
            self.hunger -=1
        else:
            pass
    def sleep(self):
        if self.energy <= 5:
            self.energy += 5 
        else :
            value = 10 - self.energy 
            self.energy += value
        
    def play(self):
        #  decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        if self.energy > 0 :
            if self.energy >= 2:
                self.energy -= 2
                if self.happiness <= 10:
                    self.happiness +=2
                else:
                    pass
                if self.hunger <= 10:
                    self.hunger += 1
                else:
                    pass
            elif self.energy == 1 : 
                self.energy -= 1 
                if self.happiness <= 10:
                    self.happiness += 1
                else:
                    pass
                if self.hunger <= 10:
                    self.hunger += 0.5
                else:
                    pass
            else:
                self.energy = 0
            pass
        else:
                print("you cannot play while you are hungry")
    def get_status(self):
        print("name : ",self.name)
        print("energy : ",self.energy)
        print("happiness", self.happiness)
        print("hunger", self.hunger)
        print("tricks", self.tricks)

    def train(self, trick):
        #Teaches the pet a new trick and stores it in the tricks list
        if self.energy > 0 :
            if trick not in self.tricks:
                self.tricks.append(trick)
                print(f"{self.name} learned a new trick: {trick}!")
            else:
                print(f"{self.name} already knows the trick: {trick}.")
        else:
            print("you cannot play while you are hungry")

    def show_tricks(self):
        #Prints all the tricks that the pet has learned.
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
    def play_trick(self):
        trick = input("Enter the trick you want to play: ")
        if trick in self.tricks:
            self.play()
            print(f"{self.name} is performing the trick: {trick}!")

        else:
            print(f"{self.name} doesn't know the trick: {trick}.")
            print("Would you like to train your pet to learn this trick? (yes/no)")
            response = input()
            if response.lower() == "yes":
                self.train(trick)
            else:
                print("Okay, maybe later!")