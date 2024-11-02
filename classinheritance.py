"""class inheritence

a class can have methods and attributes defined in another class usimg class inheritance
"""

class Animal():
   def __init__(self):
    def numeyes(self):
         print("num of eyes: 2")

    def breathe(self):
                print("inhale,exhale")
                  
class Fish(Animal):
            def __init__(self):
                super().__init__()
            def swim(self):
                  print("moving in water")

            #can modify methods of super class in inherited class 
            def breathe(self):
                  super.breathe()
                  print("doing this underwater")
                  
                   

nemo=Fish()
nemo.swim()#method of Fish class
nemo.breathe()#method inherited from Animal class                
                
#class Fish is inherited methods and attributes from class Animal
