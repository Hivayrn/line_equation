import numpy as np

# Getting values of x and y from user
x = np.array(input("Please enter x values: ").split(), dtype=float)
y = np.array(input("Please enter y values: ").split(), dtype=float)

# calculate theta
def calculate_theta(x, y):
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    numerator = np.sum((x - x_bar) * (y - y_bar))
    denominator = np.sum((x - x_bar) ** 2)   
    theta = numerator / denominator
    return theta

theta_value = calculate_theta(x, y)

# calculate c
def calculate_c(x, y, theta):
    c = np.mean(y) - theta * np.mean(x)
    return c
c_value = calculate_c(x, y, theta_value)
print ("theta:",theta_value)
print ("c:",c_value)
