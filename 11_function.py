def greet_user():
    hi = "Hi from your robot overlords!"
    print (hi)

def user_name(un):
    username = "The NSA thanks for your cooperation "+un
    print (username)

def twitter_follow(tw):
    twitter = "Following the account @" + tw
    return twitter

greet_user()
user_name(input("Please enter your username: "))
twmsg = twitter_follow(input("Please enter your twitter uname @"))
print(twmsg)
