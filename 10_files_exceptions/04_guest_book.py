filename = "guest_name.txt"

with open(filename, "w") as file:
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        name = input("Please type a name: ")
        file.write(name.title() + "\n")
        answer = input("Would you like to type another (y=Yes, anything else to exit)?: ")
