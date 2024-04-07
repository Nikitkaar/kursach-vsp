import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd


"""def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, 3, name="Alice", age=30)
"""

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)

print(my_function())

