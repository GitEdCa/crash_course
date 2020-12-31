import user
from user import create_user
from user import create_user as cu
import user as u
from user import *

user1 = user.create_user('Name', 'Last', 10)
user2 = create_user('Name', 'Last', 10)
user3 = cu('Name', 'Last', 10)
user4 = u.create_user('Name', 'Last', 10)
print(user1)
print(user2)
print(user3)
print(user4)
