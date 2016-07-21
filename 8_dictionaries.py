# What about something that can has a name and a value,
# for example for a tank game...

tank_0 = {'color': 'green', 'power': 5}
print (tank_0['color'])
print (tank_0['power'])

# So we have a key and a value
# What about adding more values

tank_0['x_pos'] = 0
tank_0['y_pos'] = 25

print (tank_0)

# lets create a empty tank_0
tank_1 = {}

# add a color and power
tank_1['color'] = "yellow"
tank_1['power'] = "10"

# to much
del tank_1['power']

print (tank_1)

# Can we loop?
for key, value in tank_0.items():
    print (key + " = " + str(value))

# Sorted please?
for key, value in sorted(tank_0.items()):
    print (key + " = " + str(value))

# I want the tanks nested in a battlefield
battlefield = [tank_0, tank_1]
print (battlefield)

# Pizza sample...
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
                "with the following toppings:")
print (pizza['toppings'])
