#creating our own class 
#initialising class with constructor function i.e,__init__(self,etc)
#adding attributes
class User:
    def __init__(self,userid,username):
        self.id=userid
        self.name=username
        self.follower=0

    #adding methods
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("001","raksha")
user_2=User("002","katherine")

print(user_1.name)
print(user_2.name)

user_1.follow(user_2)



print(f"user one following {user_1.following}")
print(f"user one followers {user_1.followers}")
print(f"user two following {user_2.following}")
print(f"user two followers {user_2.followers}")