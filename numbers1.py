num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
sum = int(num1+num2)
diff = int(num1-num2)
product = int(num1*num2)
quotient = float(num1/num2)

print("We will now do some math!")

print("{} + {} equals {}".format(num1, num2, (sum)))
print("{} - {} equals {}".format(num1, num2, (diff)))
print("{} * {} equals {}".format(num1, num2, (product)))
print("{} / {} equals {}".format(num1, num2, (quotient)))
