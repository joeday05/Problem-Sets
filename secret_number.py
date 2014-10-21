# secret number - bisection search example

high = 100
low = 0
hlc = ""

print "Please think of a number between 0 and 100!"

while hlc != "c":
    guess = int((high - low) / 2 + low)
    print "Is this your secret number? " + str(guess)

    hlc = raw_input("Enter 'h' to indicate the guess is too high.\
    Enter 'l' to indicate the guess is too low.\
    Enter 'c' to indicate I guessed correctly. ")
    
    if hlc == "h":
        high = guess
    elif hlc == "l":
        low = guess
    elif hlc == "c":
        print "Game Over. Your secret number was: " + str(guess)
        break
    else:
        print "Sorry, I did not understand your input."
