# a list is a collection of items, in some order
catz = ['piano cat', 'long cat', 'maru cat', 'simon cat', 'pusheen cat']

print catz

# your favorite one?
print catz[2]
# Just remember, the index starts in 0...

# Moar fun
print "The best compositor is the " + catz[0].title() + ", just because"

# I don't like that simon cat...
catz[3] = 'Grumphy cat'

# We need more cats!
catz.append('Executive cat')
catz.append('Commander cat')

# Can we add at the begining vitage cat?
catz.insert(0, 'Vintage cat')

# lets see the list again
print catz

# too many cats!
catz.remove('long cat')
del catz[6]
lastcat = catz.pop()

print "current list"
print catz
print "last deleted: " + lastcat

# lets organize our cats
catz.sort()
# in reverse please
catz.reverse()
