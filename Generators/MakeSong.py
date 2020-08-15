'''
make_song Write a function called make_song, which takes a count and a beverage,
and returns a generator that yields verses from a popular song about a the beverage.
The number of verses in the song is determined by the count. Each verse of the song should involve one fewer beverage,
until there are no beverages remaining. (Check the examples for details on the structure of the lyrics.)
The default count should be 99, and the default beverage should be soda.
'''
'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num=99, bevarage= "soda"):

    while True:
        if num<0 : raise StopIteration
        if num == 0: yield "No more {}!".format(bevarage)
        elif num == 1: yield "Only 1 bottle of {} left!".format(bevarage)
        else: yield "{} bottles of {} on the wall.".format(num,bevarage)
        num -= 1

# def make_song(verses=99, beverage="soda"):
#     for num in range(verses, -1, -1):
#         if num > 1:
#             yield "{} bottles of {} on the wall.".format(num, beverage)
#         elif num == 1:
#             yield "Only 1 bottle of {} left!".format(beverage)
#         else:
#             yield "No more {}!".format(beverage)

kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song))# 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration
