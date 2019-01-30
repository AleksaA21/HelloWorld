
class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something(self):
        "pass"
        print("Hi from " + str(self))

    def __str__(self):
        return self._name + ", " + self._email



users = [ User("Testuser", "tmail@mail.com"), User("User2", "mail2@mail.com") ] 

for user in users:
    user.do_something()

"""
print("Hello, from python! ")
a = 3 
b = 5
c = a + b
print(c)
"""
