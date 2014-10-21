x = float(raw_input("Enter a decimal number between 0 and 1: "))

# find p such that 2^p * x is a whole number
p = 0
while ((2**p) * x) % 1 != 0:
    print("Remainder = " + str((2**p) * x - int((2**p) * x)))
    p += 1
    
# multiply this by 2^p
num = int(x * (2**p))

#convert integer into binary form
result = ""
if num == 0:
    result = "0"

while num > 0:
    result = str(num % 2) + result
    num = num / 2

# put the correct number of zeros in front of binary
for i in range(p - len(result)):
    result = "0" + result
    
result = result[0: -p] + "." + result[-p:]
print "The binary representation of the decimal " + str(x) + " is " + str(result)
