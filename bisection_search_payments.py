# Bisection Search to speed program - problem set 2
"""
calcluate the fixed payment, to the penny, required to pay off a loan in a year
accounting for monthly interest accrual
"""

#balance = 999999
#annualInterestRate = 0.18
#lowest payment is 90325.03

low = balance / 12
high = (balance * ((1 + annualInterestRate/12.0)**12)) /12.0
tolerance = .01

fixed_payment = (high + low) / 2.0
new_balance = balance 

def guess(low, fixed, high, bal, tol):
    if abs(bal) <= tol: return [low, fixed, high]
    if bal > 0:
        low = fixed
        fixed = (high + fixed) / 2.0    
        high = high
        return [low, fixed, high]
    else:
        high = fixed
        fixed = (fixed + low) / 2.0
        low = low
        return [low, fixed, high]
 
while abs(new_balance) >= tolerance:
    new_balance = balance
        
    for month in range(1, 13):
        new_balance = new_balance - fixed_payment
        new_balance = new_balance + (new_balance * (annualInterestRate / 12))
    
    hilo = guess(low, fixed_payment, high, new_balance, tolerance)
    low = hilo[0]
    fixed_payment = hilo[1]
    high = hilo[2]

print "Lowest Payment: ", round(fixed_payment, 2)

