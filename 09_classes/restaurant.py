class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name.title() + " and has a " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("The restaurant is open!")
