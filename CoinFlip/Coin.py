import random

class coin(object):

    #     This module is to flip a coin to land heads or tails.
    #     First there must be a number passed which will say
    #     how many times to flip the coin. Allow an extra param
    #     of 1 with a given input and the out put will also include
    #     the array in the output
     def flip(iter=1):
        iterate = int(iter)
        result = []
        heads = 0
        tails = 0
        x=0
        for x in range(0, iterate):
            I = random.randint(1, 2)
            if I is 1:
                result.append('h')
                heads = heads + 1
            else:
                result.append('t')
                tails = tails + 1
        return 'You have ' + str(heads) + ' heads, and ' + str(tails) + ' tails.'