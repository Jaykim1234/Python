"""
Fill in the class definition below such that it initializes a Car object with 
four attributes that take string values (or, in some cases, None): 
'color', 'speed', 'brand', and 'worth'.

Color and speed should be passed to Car during initialization. Brand 
and worth, on the other hand, are derived attributes.

If color is 'yellow' and speed is 'slow', then the brand attribute
should be 'Renault'. Otherwise, the brand attribute should be left as None.

If the brand is 'Renault', then worth should be 'cheap'. If the brand is 
not 'Renault', then worth should be 'expensive'.

Correct the code below so that the class definition works as expected.

For example:
If we create an object from your class as:
my_car = Car("blue", "super slow")
then: 
my_car.color should be equal to 'blue'
my_car.speed should be equal to 'super slow'
my_car.brand should be equal to  None
my_car.worth should be equal to 'expensive'
"""
# 2nd solution
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

        if self.color == 'yellow' and self.speed == 'slow':
            self.brand = 'Renault'
            self.worth = 'cheap'
        else:
            self.brand =  None
            self.worth = 'expensive'



# 1st solution
# class Car:
#     def __init__(self, color, speed):

#         self.color = color
#         self.speed = speed

#         if (self.color == 'yellow') and (self.speed == 'slow'):
#             self.brand = 'Renault'
#             self.worth = 'cheap'
#         else:
#             self.brand = None
#             self.worth = 'expensive'

        
# my_car = Car("blue", "super slow")
# my_car.color
# my_car.speed 
# my_car.brand 
# my_car.worth