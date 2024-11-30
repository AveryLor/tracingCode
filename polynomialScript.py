import numpy as np
import matplotlib.pyplot as plt

# Example: x and y points (replace with your traced data)
x_points = np.array([0, 1, 2, 3, 4, 5])
y_points = np.array([0, 1, 4, 9, 16, 25])  # Quadratic data for demonstration

# Fit a polynomial of degree 2 (quadratic)
degree = 2
coefficients = np.polyfit(x_points, y_points, degree)

# Generate the polynomial function
polynomial = np.poly1d(coefficients)

# Generate a smooth curve for plotting
x_smooth = np.linspace(min(x_points), max(x_points), 500)
y_smooth = polynomial(x_smooth)

# Plot the original points and the fitted curve
plt.scatter(x_points, y_points, color='red', label='Traced Points')
plt.plot(x_smooth, y_smooth, color='blue', label=f'Polynomial (Degree {degree})')
plt.legend()
plt.title('Polynomial Fit to Glacier Outline')
plt.xlabel('Width (pixels)')
plt.ylabel('Height (pixels)')
plt.show()

# Print the polynomial equation
print(f"Fitted Polynomial: {polynomial}")
