#!/usr/local/bin/python3
value = int(input("Enter an int: "))
if value < 10:
    print("Less than 10")
    if value > 5:
        print("but it's greater than 5")
elif value == 42:
    print("This is the answer to life, the universe and everything.")
else:
    print("value does not lie between 5 and 10")
    if(value >= 10):
        print("value is greater or equal to 10")
    if(value <= 5):
        print("value is less than or equal to 5")
        
   
#### In-line conditionals
print("Positive" if value > 0 else "Negative")     
    
        
        
         
        
    