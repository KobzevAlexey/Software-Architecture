import random
from HW2.AnyGenerator import AnyGenerator
from HW2.GemGenerator import GemGenerator
from HW2.GoldGenerator import GoldGenerator

if __name__ == '__main__':
    fabricList = [GoldGenerator(), GemGenerator(), AnyGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()