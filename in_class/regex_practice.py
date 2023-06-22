import re

# 1. Write a function to match a string of any length that contains only lowercase letters, uppercase letters, numbers, and underscores.    
def match_string(string):   
    if re.match(r'^[a-zA-Z0-9_]+$', string):
        print("Match!")
    else:
        print("No match!")  

# 2. Write a function that matches a string that starts with "The" and ends with "Spain".
def match_string2(string):
    if re.search(r'^The.*Spain$', string):
        print("Match!")
    else:
        print("No match!")

# 3. Write a function that starts with "he", followed by 1 or more  (any) characters, and an "o":
def match_string3(string): 
    if re.search(r'he.+o', string):
        print("Match!")
    else:
        print("No match!") 

# 4. Write a function that matches a string that starts with "he", followed by two (any) characters, and an "o":'.
def match_string4(string):
    if re.search(r'he..o', string):
        print("Match!")
    else:
        print("No match!")


# Test Cases. Predict the output of each test case before running the program.
match_string("hello_world")
match_string("hello_world%")
match_string2("The trip from Spain")
match_string2("The trip from Spainn")
match_string3("helllo")
match_string4("helllo")

#In Class Exercises

# 1.) Write a function  that matches a string that starts with "se", followed by two (any) characters, and an "r".

# 2.) Write a function that starts with "ap", followed by 1 or more  (any) characters, and an "l".

