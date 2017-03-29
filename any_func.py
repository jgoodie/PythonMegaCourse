#!/usr/local/bin/python3

# hosts_path="foo_hosts"
# redirect = "127.0.0.1"
# website_list = ["www.facebook.com", "facebook.com", "www.instagram.com","instagram.com"]
# 
# 
# file=open(hosts_path,'r+')
# content = file.readlines()
# 
# for line in content:
#     if any(website in line for website in website_list):
#         pass
#     else:
#         print(line)


# with open(hosts_path,'r+') as file:
#     content=file.readlines()
#     for line in content:

# print("any(l == 't' for l in 'python') # Returns True. Same as: 't' in 'python'")
# print(any(l == 't' for l in 'python'))
# print("all(l == 't' for l in 'python') # Returns False. Not all of the letters are 't'.")
# print(all(l == 't' for l in 'python'))
#         
# g = (l == 't' for l in 'python')
# print(g)
# print(g.__next__()) # False. 'p' is not equal to 't'
# print(g.__next__()) # False. 'y' is not equal to 't'
# print(g.__next__()) # True. 't' is equal to 't'
# for value in g:
#     print(value)
#     
# print(any(g))

def t():
    print('In True!\n')
    return True

def f():
    print('In False!\n')
    return False

# Store functions to be called in a list
funcs = [t, f, f, f, t]

def test_any():
    # Pass a generator expression with function calls to any
    print(any(func() for func in funcs))

def test_all():
    # Pass a generator expression with function calls to all
    print(all(func() for func in funcs))

test_any() # Calls t() once and stops.
test_all() # Calls t(), then f(), then stops