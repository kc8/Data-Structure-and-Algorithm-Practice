import random 

class MSDie: 
    """"
    Multi-Sided die

        Instance variables:
            current_value
            num_sides
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll() 
    
    def get_num_sides(self):
        return self.num_sides
    
    def roll(self): 
        self.current_value = random.randrange(1, self.num_sides + 1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    def __eq__(self, otherdie):
        """
        See if the current die are equal to one another based on sides"""

        return True
        #if self.num_sides == otherdie.get_num_sides() 
        #    return True
        #else: return Falsae
    
    def __lt__(self, otherdie):
        """Tests to see if the number of sides on a die is less than another dice"""
        return False


my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)