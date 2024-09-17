#calculate bill of rollercoaster according to thier height
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill=0
if height>= 120:
  print("you can ride the rollercoaster!")
  age=int(input("what is your age?"))
  if age<12:
    bill=5
    print("child tickets are $5")
  elif age<18:
    bill=7
    print("youth tickets are $7")
  else:
    bill=12
    print("adult tickets are $12")
  wants_photo=input("do you want your photo taken? Y or N?")
  if wants_photo=="Y":
    bill=bill+3
    print(f"your total bill is ${bill}")
else:
  print("sorry, you have to grow taller before you could ride the coaster") 