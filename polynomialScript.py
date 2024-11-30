import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Load the glacier image
image_path = "1918-GlacierImage.png"  # Adjust the file path if needed
img = plt.imread(image_path)

# Display the image
plt.imshow(img)
plt.title("Trace the Glacier Outline")
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.gca().invert_yaxis()  # Invert y-axis scale for natural tracing
plt.show()

print("Click along the glacier outline to trace its shape. Double-click to finish.")

# Step 1: Trace the glacier outline
glacier_outline = plt.ginput(n=-1, timeout=0, show_clicks=True)
glacier_outline = np.array(glacier_outline)

# Separate x and y points
x_points = glacier_outline[:, 0]
y_points = glacier_outline[:, 1]

# Save the traced points to a CSV file
np.savetxt("glacier_outline.csv", glacier_outline, delimiter=",", header="x,y", comments="")
print("Traced points saved to glacier_outline.csv.")

# Step 2: Fit a polynomial to the traced points
# Choose the degree of the polynomial (adjust as needed)
degree = 5
poly_coeffs = np.polyfit(x_points, y_points, degree)
poly_func = np.poly1d(poly_coeffs)

# Print polynomial coefficients
print("Polynomial coefficients (highest degree first):")
print(poly_coeffs)

# Generate x values for the polynomial curve
x_poly = np.linspace(min(x_points), max(x_points), 500)
y_poly = poly_func(x_poly)

# Step 3: Plot the traced points and the fitted polynomial
plt.imshow(img)
plt.plot(x_points, y_points, 'ro', label="Traced Points")  # Traced points
plt.plot(x_poly, y_poly, 'b-', label=f"Polynomial Fit (degree {degree})")  # Polynomial fit
plt.gca().invert_yaxis()  # Ensure y-axis is inverted
plt.title("Traced Glacier Outline with Polynomial Fit")
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.legend()
plt.show()

# Step 4: Save polynomial coefficients to a file
np.savetxt("polynomial_coeffs.txt", poly_coeffs, header="Polynomial Coefficients (highest degree first)", comments="")
print("Polynomial coefficients saved to polynomial_coeffs.txt.")
