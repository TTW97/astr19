"""Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical 
parameters of the animal: length of the arms (float), 
length of the legs (float), number of eyes (int), does it have a tail? (bool), 
is it furry? (bool). Write an initialization function that sets the values 
of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe 
the data members representing the physical characteristics of the animal.
"""

class Crocodile:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length      # in centimeters
        self.leg_length = leg_length      # in centimeters
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Crocodile Physical Characteristics:")
        print(f"- Arm Length: {self.arm_length} cm")
        print(f"- Leg Length: {self.leg_length} cm")
        print(f"- Number of Eyes: {self.num_eyes}")
        print(f"- Has a Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"- Is Furry: {'Yes' if self.is_furry else 'No'}")

# Example usage:
my_favorite_animal = Crocodile(arm_length=50, leg_length=75, num_eyes=2, has_tail=True, is_furry=False)
my_favorite_animal.describe()
