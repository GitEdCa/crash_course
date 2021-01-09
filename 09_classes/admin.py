from user_m import User

class Privileges():

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Current privileges: ")
        for privilege in self.privileges:
            print(privilege)
   

class Admin(User):

    def __init__(self, first_name, last_name, age, email, login_attempt = 0):
        super().__init__(first_name, last_name, age, email, login_attempt = 0)
        print("Adding privileges to " + first_name)
        self.privileges = Privileges('can add post', 'can delete post', 'can ban user',)
