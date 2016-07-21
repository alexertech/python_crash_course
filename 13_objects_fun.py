# The classic animal sample
class Cat():
    """A simple attempt to be an amazing a cat."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + ", \"seriosly? I'm a cat!\".")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + ", rolled in position to scratch!")


my_cat = Cat('maru', 6) # name and age
print("My cat name is " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")

print("Hey cat! SIT!")
my_cat.sit();

print("Hey cat! Do a roll over!")
my_cat.roll_over();
