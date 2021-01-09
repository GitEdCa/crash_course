filename = 'guest.txt'
name = input("What is your name?")
with open(filename, 'w') as guest_file:
    guest_file.write(name + "\n")
