while True:
    age = input("What's your age? ")
    age = int(age)

    if age > 12:
        print("Your ticket's cost is $15")
    elif age >= 3 and age < 12:
        print("Your ticket's cost is $10")
    else:
        print("Your ticket is free")
