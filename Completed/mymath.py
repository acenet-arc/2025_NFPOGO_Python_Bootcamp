def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#Your code goes here
def average(values):
    """Calculate the average"""
    sum_of_vals = 0
    for val in values:
        sum_of_vals += val
    average = sum_of_vals/len(values)
    return average

def convert_temperature(celcius):
    return (celcius * 9/5) + 32