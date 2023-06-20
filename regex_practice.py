import re

# 1. Write a function to match a string of any length that contains only lowercase letters, uppercase letters, numbers, and underscores.    
def match_string(string):   
    if re.match(r'^[a-zA-Z0-9_]+$', string):
        print("Match!")
    else:
        print("No match!")  

# 2. Write a function that matches a string that has an a followed by zero or more b's.
def match_string2(string):
    if re.search(r'ab*', string):
        print("Match!")
    else:
        print("No match!")

# 3. Write a function that matches a string that has an a followed by one or more b's.
def match_string3(string): 
    if re.search(r'ab+', string):
        print("Match!")
    else:
        print("No match!") 

# 4. Write a function that matches a string that has an a followed by zero or one 'b'.
def match_string4(string):
    if re.search(r'ab?', string):
        print("Match!")
    else:
        print("No match!")


match_string("hello_world")
match_string2("atbbbbb")
match_string3("aqbbbbb")
match_string4("c")