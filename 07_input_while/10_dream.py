dreams = {}

while True:
    name = input("What's your name? \n(Insert 'quit' to exit) ")
    if name == 'quit':
        break
    dream = input("If you could visit one place in the world, where would you go? ")
    dreams[name] = dream

for name, dream in dreams.items():
    print(name + " would like to go to " + dream)

