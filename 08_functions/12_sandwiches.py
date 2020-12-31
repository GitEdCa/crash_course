def make_sandwich(*toppings):
    """
    Prints a sandwich with all the provided toppings
    """
    print("Your sandwich has: ")
    for topping in toppings:
        print(topping)

make_sandwich("ham", "catsup")
make_sandwich("ham", "catsup", "eggs")
make_sandwich("ham", "catsup", "eggs", "chilaquiles")
