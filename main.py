# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from animal import Animal
from dog import Dog
from bird import Bird
from factory import Fact
from singleton import Single
from person import Person

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    s = Single()
    ss = Single()
    p = Person()

"""
    r = Fact(3)
    x=r.getObject()
    r.getObject().drink()

  


    a=Dog(10)
    a.sleep(3)
    a.run()
    a.dogmakesound()
    a.makesound('dana')
    b=Bird(8)
    b.fly()
    b.birdmakesound()
    b.makesound('dana')
    a.move()
    b.move()
"""


