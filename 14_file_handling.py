# Yeah, lets open that file...
with open('pi_digits.txt') as file_object:
    # Each line will be set inisde as contents as a list
    contents = file_object.read()
    print(contents.rstrip())

pi_string = ''
# We can iterate between lines
for line in contents:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# --------

# Lets write

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
