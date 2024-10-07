#creating our own class 
#initialising class with constructor function i.e,__init__(self,etc)

class User:
    def __init__(self,userid,username):
        self.id=userid
        self.name=username
        self.follower=0

user_1=User("001","raksha")
user_2=User("002","katherine")

print(user_1.name)
print(user_2.name)