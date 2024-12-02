import numpy as np
import matplotlib.pyplot as plt

# Step 1: Example of x and y values (replace these with your traced data)
# Traced data points (x, y) for the glacier outline
x = np.array([0, 17, 26, 42, 115.4, 154, 180,200,240,320,345,400,410,470])  # 1918 x-values
y = np.array([128, 110, 61, 108, 90, 89, 105,100,120,122,114,120,122,150])  # 11918 y-values

#x = np.array([0, 17, 26, 42, 115.4, 154, 180,200,240,320,345,400,410,470])  # 2018 x-values
#y = np.array([49.1, 50, 45, 48, 42.2, 39.3, 35.1,35,32,25,23,20,17,10])  # 2018 y-values


# Step 2: Fit a polynomial to the data
degree = 5  # Degree of the polynomial (adjust this as needed), this checked manually to see which polynomial best fit the graph
coeffs = np.polyfit(x, y, degree)

# Step 3: Print the polynomial coefficients
print(f"Polynomial coefficients (degree {degree}): {coeffs}") # Prints the degree of the polynomial and its related coefficients

# Step 4: Create a polynomial function from the coefficients
polynomial = np.poly1d(coeffs) # Using numpy to create a funtion with the coefficients

# Step 5: Generate x values for the polynomial curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = polynomial(x_fit)

# Step 6: Plotting the data points and the polynomial fit
plt.scatter(x, y, color='blue', label='Traced Points')  # Data points
plt.plot(x_fit, y_fit, color='red', label=f'Polynomial Fit (degree {degree})')  # Polynomial fit
year = "1918"
#year = "2018" Change which line is commented out based on the year
plt.title(f"Polynomial Fit to {year} Glacier Outline")
plt.xlabel("Width (meters)")
plt.ylabel("Height (meters)")
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Printing the polynomial in a more readable format
print("Polynomial equation:")
print(polynomial)
