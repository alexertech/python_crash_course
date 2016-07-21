# Conditionals of course
cars = ['audi','porshe','tesla','ferrari','mazda']

for c in cars:
    if c == "tesla":
        print ("tesla FTW!")
    else:
        print (c)

# Classic comparators
for n in range(5,25):
    if n < 18:
        print (str(n) + "= nope!")
    if n == 18:
            print (str(n) + "= yes!")
    if n > 18:
        print (str(n) + "= meh!")

# better comparations
for k in range(100,500, 50):
    if k < 200:
        print ("Too cheap")
    elif k == 300:
        print ("Good prize")
    elif k > 300:
        print ("what?")

# Lists and choises

pizza_tops = ['mushrooms', 'extra cheese']

if 'mushrooms' in pizza_tops:
    print("Adding mushrooms.")
if 'pepperoni' in pizza_tops:
    print("Adding pepperoni.")
if 'extra cheese' in pizza_tops:
    print("Adding extra cheese.")

# Your pizza is ready sir!
