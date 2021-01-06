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

class Admin(User):

    def __init__(self, first_name, last_name, age, email, login_attempt = 0):
        super().__init__(first_name, last_name, age, email, login_attempt = 0)
        self.privileges = ('can add post', 'can delete post', 'can ban user',)

    def show_privileges(self):
        print("Current privileges: ")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Rolo", "Lothbrook", 30, "rolo@loth.com")
admin.describe_user()
admin.greet_user()
admin.show_privileges()
