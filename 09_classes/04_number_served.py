class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served 

    def describe_restaurant(self):
        print("This restaurant is " + self.restaurant_name.title() + " and has a " + self.cuisine_type.title() + " cuisine. Serving " + str(self.number_served) + " persons.")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("Number served: " + str(number_served))

restaurant = Restaurant("pfchangs", "Chinese")
restaurant.describe_restaurant()
restaurant = Restaurant("pfchangs", "Chinese", 20)
restaurant.describe_restaurant()
restaurant.set_number_served(50)
restaurant.describe_restaurant()
