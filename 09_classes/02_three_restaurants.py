class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name.title() + " and has a " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("The restaurant is open!")

pfchangs = Restaurant("pfchangs", "Chinese")
macdonalds = Restaurant("Macdonalds", "Hamburgers")
pizza_hut = Restaurant("Pizza Hut", "Pizza")

pfchangs.describe_restaurant()
pfchangs.open_restaurant()

macdonalds.describe_restaurant()
macdonalds.open_restaurant()

pizza_hut.describe_restaurant()
pizza_hut.open_restaurant()
