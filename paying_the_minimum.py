# Paying the minimum - problem set 2
'''
calculate the monthly payment and interest for a credit card over the 
course of a year by month.

total the amount paid and the remaining balance on the credit card
'''

# Problem Set 2
#previous_balance = 5000
#annual_interest_rate = 0.18
#monthly_payment_rate = 0.02

# Test Case
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total_principal_paid = 0

def unpaid_balance(previous_balance, monthly_payment_rate):
    minimum_monthly_payment = previous_balance * monthly_payment_rate
    previous_balance = previous_balance - minimum_monthly_payment
    return [minimum_monthly_payment, previous_balance]
    
def calc_interest(remaining_balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12
    monthly_interest_payment = remaining_balance * monthly_interest_rate
    return monthly_interest_payment
    
for month in range(1, 13):
    print "Month: ", month
    ub = unpaid_balance(balance, monthlyPaymentRate)
    minimum_monthly_payment = ub[0]
    balance = ub[1]

    interest = calc_interest(balance, annualInterestRate)
    balance = balance + interest
    total_principal_paid += minimum_monthly_payment
    
    print "Minimum monthly payment: ", round(minimum_monthly_payment, 2)
    print "Remaining balance: ", round(balance, 2)
    

print "Total paid: ", round(total_principal_paid, 2)
print "Remaining balance: ", round(balance, 2)