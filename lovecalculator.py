#1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

#2. Then check for the number of times the letters in the word LOVE occurs.   

#3. Then combine these numbers to make a 2 digit number and print it out. 

def calculate_love_score(name1,name2):
    combined_names=name1+name2
    lowered=combined_names.lower()
    
   
    t=lowered.count("t")
    r=lowered.count("r")
    u=lowered.count("u")
    e=lowered.count("e")
      
    first=t+r+u+e
    l=lowered.count("l")  
    o=lowered.count("o")
    v=lowered.count("v")
    e=lowered.count("e")
    second=l+o+v+e
    
    score=int(str(first)+str(second))
    print(f"Your love score is {score}.")
    
    
nameone=input("enter first person name: ")
nametwo=input("enter second person name: ")   
        
calculate_love_score(nameone,nametwo)            
