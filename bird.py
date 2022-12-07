from animal import Animal

class Bird(Animal):

    def __init__(self, km):
        super().__init__()
        self.km = km

    def fly(self):
        print("bird is flying km: ", self.km)

    def birdmakesound(self):
        super().makesound('wik wik')

    def move(self):
        print('bird move')