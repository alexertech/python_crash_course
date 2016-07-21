# This one is fun

# The defnition of build_profile() expects a frst and last name,
# and then it allows the user to pass in as many name-value pairs
# as they want. The double asterisks before the parameter **user_info
# cause Python to create an empty dictionary called user_info and pack
# whatever name-value pairs it receives into this dictionary.

def build_profile(first, last, **user_info):

    # This comment is called a docstring, which describes what the function
    # does. Docstrings are enclosed in triple quotes, which Python looks for
    # when it generates documentation for the functions in your programs.
    """Build a dictionary containing everything we know about a user."""

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
