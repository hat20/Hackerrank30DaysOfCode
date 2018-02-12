#!/bin/python3

import sys
import math

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    tip = meal_cost * (tip_percent/100.0)
    tax = meal_cost * (tax_percent/100.0)
    total_cost = int(math.floor(meal_cost + tip + tax +0.5))
    
    #Since the total_cost is always positive
    #added 0.5 so as to correctly round up the floating point to nearest integer.
    
    print("The total meal cost is",total_cost, "dollars.")