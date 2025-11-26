def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#Solution
def average(values):
    """Calculate the average of a list of values."""
    return sum(values) / len(values)

def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def calculate_density(salinity, temperature):
    """Estimate water density based on salinity and temperature."""
    return 1000 + (0.8 * salinity) - (0.2 * temperature)