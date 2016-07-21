# Basic stats
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print (digits)

print ("Min: " + str(min(digits)))

print ("Max: " + str(max(digits)))

print ("Sum: " + str(sum(digits)))

# lists combined with loops...
squares = [value**2 for value in range(1,11)]

print (squares)

# What about reanges and ways to select inside the list?
pokemon = ['Charmander', 'Squirtle', 'Bulbasaur', 'Pikachu']
# pokemon? seriosly?

# okay, lets do some ranges

# Select the first one
print (pokemon[:1])

# Select the last two
print (pokemon[2:])

# Select the middle one
print (pokemon[1:2])

# Loop the first ones...
for p in pokemon[:3] :
    print (p)

# I want this pokemon set too...
commenter_pokemons = pokemon[:]

print ("My pokemons")
print (pokemon)
print ("Commenter pokemons")
commenter_pokemons.pop() # I dont like pikachu
print (commenter_pokemons)

# Can i create a list that doesnt change?
# Tuples!
dimensions = (200,500)
print (dimensions[0])

# I will get a nasty error if I try to change the value of [0]
# but I can assing a new value to the whole tuple

dimensions  = (500,100)
print (dimensions[0])

# Just because we can...
