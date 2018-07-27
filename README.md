# CoinFlip
Flip a Coin or randomize some numbers
## How-To
Import these like you would any python library, uses base libraries (random). To use the Coin module, you would pass it a parameter for how many iterations you would like to do for flipping between heads or tails. Put in a secondary parameter of one to display the array if you would like to see the h and t. 
To use the RandNum, give it the amount of iterations and the number you would like to randomize. So, this basically says "Hey how many numbers are between 0 and n, okay lets then choose a random number x amount of times out of that set of numbers between 0 and n"
# Example Code
```
from CoinFlip.Coin import coin
from CoinFlip.RandNum import num

print(num.randomizer(5, 5))
print(coin.flip(5,1))
**********************************
OUTPUT:
[2, 3, 3, 1, 3]
['t', 'h', 't', 'h', 'h']
You have 3 heads, and 2 tails.

Process finished with exit code 0
```
