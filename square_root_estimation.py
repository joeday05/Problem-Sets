x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        print "guess: " + str(guess) + " x: " + str(x) + " epsilon: " + str(epsilon)
        guess += step
    else:
        break



if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
