x = float(input("Enter your number: "))
if x < 256:
    print(bin(x))
else:
    print("Your value is too high")

y = float(input("Enter your number: "))
y = float(y)
if y < 256:
    print(bin(x))
else:
    print("Your value is too high")
print("your answer is", x + y, "the binary is", bin(x + y))