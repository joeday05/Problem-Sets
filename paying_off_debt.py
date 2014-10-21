# Paying off debt in a year - problem set 2
'''
using estimation to figure out the fixed payment necessary to pay of debt in
12 months with monthly compounding interest
'''

#balance = 3926
#annualInterestRate = 0.2

fixed_payment = 0
new_balance = balance 

while new_balance > 0:
    new_balance = balance
    fixed_payment += 10
        
    for month in range(1, 13):
        new_balance = new_balance - fixed_payment
        new_balance = new_balance + (new_balance * (annualInterestRate / 12))

print "Lowest Payment: ", fixed_payment
