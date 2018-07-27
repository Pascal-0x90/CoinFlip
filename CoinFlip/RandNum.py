import random

class num(object):

    #    This module is to iterate a certain range
    #    of numbers, a certain amount of times. So,
    #    for a number 5 with an iteration of 3, this
    #    would supply 3 numbers randomly chosen between
    #    1 and 5

    def randomizer(iter, numb):
        iterate = int(iter)
        numb = int(numb)
        result = []
        for x in range(0, iterate):
            I = random.randint(1, numb)
            assert isinstance(I, int)
            result.append(I)
        return result