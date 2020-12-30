class User():

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("User[ " + self.first_name + ", " + 
                self.last_name + ", " + str(self.age) +
                ", " + self.email + "]")

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name)

rolo = User("Rolo", "Lothbrook", 28, "Rolo.Lothbrook@vikings.com")
mario = User("Mario", "Bros", 24, "Mario.Bros@pipes.com")
geralt = User("Geralt", "Rivia", 25, "Geralt.Rivia@witchers.com")

rolo.greet_user()
mario.greet_user()
geralt.greet_user()
