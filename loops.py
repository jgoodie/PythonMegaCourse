#!/usr/local/bin/python3

# count = 0
# while count < 100:
#     print(count)
#     count = count + 1
 
# email = ["foo.bar@mail.com","fart.barf@vomit.com","asdf@asdf.net","peepee@poopoo.com", "john.goodman@gmail.com"]
#    
# for y in email:
#     y = y.split("@")
#     if 'gmail' in y[1]:
#         print(y[0] + " at " + y[1])
#     
# password = ''
# while password != 'python123':
#     password = input("Enter password: ")
#     if password == 'python123':
#         print("I got your password!!")
#     else:
#         print("I don't have your password...")
        
names = ['foo','bar','fart','barf']
email_domains=['gmail','hotmail','yahoo','outlook']        
        
for x,y in zip(names, email_domains):
    print(x+"@"+y+".com")        

    
  
    
    
    
    
    
    
    
