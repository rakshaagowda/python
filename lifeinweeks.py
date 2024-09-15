#Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.



#It will take your current age as the input and output a message with our time left 
def life_in_weeks(age_now):
    age_left=90-age_now
    weeks_left=age_left*52
    print(f"You have {weeks_left} weeks left.")


age=input(f"Enter your age now: ")
life_in_weeks(age)

    