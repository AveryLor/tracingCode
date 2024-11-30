import numpy as np
import matplotlib.pyplot as plt

# Step 1: Example of x and y values (replace these with your traced data)
# Traced data points (x, y) for the glacier outline
#x = np.array([0, 17, 26, 42, 115.4, 154, 180,200,240,320,345,400,410,470])  # 1918 x-values
#y = np.array([128, 110, 61, 108, 90, 89, 105,100,120,122,114,120,122,150])  # 1918 y-values
x = np.array([0, 17, 26, 42, 115.4, 154, 180,200,240,320,345,400,410,470])  # 1918 x-values
y = np.array([128, 110, 61, 108, 90, 89, 105,100,120,122,114,120,122,150])  # 1918 y-values


# Step 2: Fit a polynomial to the data
degree = 11  # Degree of the polynomial (adjust this as needed)
coeffs = np.polyfit(x, y, degree)

# Step 3: Print the polynomial coefficients
print(f"Polynomial coefficients (degree {degree}): {coeffs}")

# Step 4: Create a polynomial function from the coefficients
polynomial = np.poly1d(coeffs)

# Step 5: Generate x values for the polynomial curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = polynomial(x_fit)

# Step 6: Plot the data points and the polynomial fit
plt.title("Polynomial Fit to 1918 Glacier Outline")
plt.scatter(x, y, color='blue', label='Traced Points')  # Data points
plt.plot(x_fit, y_fit, color='red', label=f'Polynomial Fit (degree {degree})')  # Polynomial fit
plt.title("Polynomial Fit to Glacier Outline")
plt.xlabel("Width (meters)")
plt.ylabel("Height (meters)")
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Optionally, print the polynomial equation in a human-readable format
print("Polynomial equation:")
print(polynomial)
