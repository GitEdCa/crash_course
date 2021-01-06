class User():

    def __init__(self, first_name, last_name, age, email, login_attempt = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempt = login_attempt

    def describe_user(self):
        print("User[ " + self.first_name + ", " + 
                self.last_name + ", " + str(self.age) +
                ", " + self.email + "]")

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + " " + str(self.login_attempt))

    def increment_login_attempts(self):
        """Increment logins attempt to one"""
        self.login_attempt = self.login_attempt + 1

    def reset_login_attempts(self):
        """Reset logins attempt to zero"""
        self.login_attempt = 0

rolo = User("Rolo", "Lothbrook", 28, "Rolo.Lothbrook@vikings.com")
mario = User("Mario", "Bros", 24, "Mario.Bros@pipes.com")
geralt = User("Geralt", "Rivia", 25, "Geralt.Rivia@witchers.com")

rolo.greet_user()
mario.greet_user()
geralt.greet_user()

rolo.increment_login_attempts()
rolo.increment_login_attempts()
rolo.increment_login_attempts()
rolo.greet_user()
rolo.reset_login_attempts()
rolo.greet_user()
