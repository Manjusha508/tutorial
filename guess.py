import random
def guesnum():
    guess=random.randint(1,100)
    attempts=0
    while True:
        try:
            trails=int(input('enter ur choice:'))
            attempts+=1
            if trails<guess:
                print('expected num is low')
            elif trails>guess:
                print('expected num is higer')
            else:
                print('congrats guessed num',trails)
                break
        except:
            print('enter valid num ')

print(guesnum())
