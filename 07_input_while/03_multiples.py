number = input("Number? ")
number = int(number)

if number % 10 == 0:
    print("Your number: " + str(number) + " is multiple of 10")
else:
    print("Your number: " + str(number) + " is not multiple of 10")
