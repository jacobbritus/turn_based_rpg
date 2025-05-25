#learning how classes work by building a rpg character with health, attacking and taking damage
class Organism:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "Human"

    # INITIALIZING INSTANCE VARIABLES
    # differs depending on arguments passed in
    # init method which acts as a constructor
    # self key word is a reference to the instance of the class
    def __init__(self, name, gender, age):
        # assigning parameters to attributes
        # used to call later on created objects
        self.name = name
        self.gender = gender
        self.age = age


    # OPERATIONS / ACTIONS ----> METHOD (FUNCTION INSIDE OF CLASS)
    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} a year old {self.gender}.")

    @staticmethod
    def scream():
        print("AAAARGHHH")

# using the class (blueprint) to create a Character class (me)
# i pass in arguments which in the parameter spots which are assigned to the attributes
me = Organism("Jacob", "Male", 19)

# parenthesis to execute the method
me.introduce()
me.scream()
