import json
username = input("What is your name? ")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

# on other file
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
