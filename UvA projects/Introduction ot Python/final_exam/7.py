"""

                                   Question 7                                   
--------------------------------------------------------------------------------

Modify the code below to create a class called 'TunnelPass' that has three 
attributes: 'weight', 'tunnel', and 'fare'. An object of this class represents
a ticket that a lorry driver must have to pass through a specific tunnel.

'weight' (the vehicle's weight in tons) and 'tunnel' (the name of the tunnel) 
should be passed to the class during object construction (in this order).

'fare' (the ticket price) is a calculated attribute.

'weight' and 'fare' are integers. 'tunnel' is a string.

The fare calculation rules are the following:
- Vehicles weighing less than 13 tons driving through Stationstunnel 
have to pay 10 euros. 
- Vehicles weighing less than 13 tons driving through Noordtunnel 
have to pay 2 euros. 
- Vehicles weighing at least 13 tons driving through Stationstunnel
or Noordtunnel have to pay 12 euros.
- Vehicles driving through any other tunnel have to pay 0 euros.

Hints:
1. The code below is already a valid class definition.
2. The '__init__' method of a class works like a function. Its only specialty 
   is that it is automatically executed when an object of the class is created.
3. The first argument in a method (called 'self' by convention) always refers 
   to the object itself. 

For example: 
If we construct a TunnelPass object and request its 'fare' attribute as:
TunnelPass(10, 'IJtunnel').fare
then the result should be equal to the integer:
0
"""
# 3rd
class TunnelPass:
    def __init__(self, weight, tunnel):
        self.weight = weight
        self.tunnel = tunnel

        if weight < 13 and tunnel == 'Stationstunnel':
            self.fare = 10
        elif weight < 13 and tunnel == 'Noordtunnel':
            self.fare =  2
        elif weight >= 13 and tunnel in ('Noordtunnel','Stationstunnel'):
            self.fare = 12
        else:
            self.fare = 0





# 2nd trial
# class TunnelPass:
#     def __init__(self, weight, tunnel):
#         self.weight = weight
#         self.tunnel = tunnel
#         self.fare = self._fare(self.weight, self.tunnel)

#     def _fare(self, weight, tunnel):
#         if weight < 13 and tunnel == 'Stationstunnel':
#             return 10
#         elif weight < 13 and tunnel == 'Noordtunnel':
#             return  2
#         elif weight >= 13 and tunnel in ('Noordtunnel','Stationstunnel'):
#             return 12
#         else:
#             return 0
 
# 1st
# class Calculator:
#     def __init__(self, base_number):
#         self.base_number = base_number
#     def add(self):
#         return self.base_number + 10
#     def sub(self):
#         return abs(self.base_number - 20)
#     def mul(self):
#         return self.base_number*30
#     def intdiv(self):
#         return self.base_number//40
