# First we need a list
skills = ['Python', 'Javascript', 'NodeJS', 'Mean', 'Hawk Eye Debugging']

# lets print
for sk in skills:
    print " - " + sk.lower()

# can we create a number list?
for n in range(1,6):
    print n

print "--------"

# Can we have non-even fun? That last 2 adds to each item in the range
for n in range(1, 11, 2):
    print n

# What about lists
squares = []

for n in range (1, 11):
    squares.append(n**2)

print squares
