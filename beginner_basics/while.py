#Biwott
#Flow control

number = 5
det = True

while det:
    guess= int(input('Give a guess :'))

    if guess == 5:
        print('You got it')
        det = False

    elif guess < 5:
        print('A little higher')

    else:
        print('A little lower')

else:
    print('Done')

