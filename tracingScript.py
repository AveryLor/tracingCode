import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import quad

# Step 1: Load the glacier image
image_path = "1918-GlacierImage.png"  
img = plt.imread(image_path)

# Display the image
plt.imshow(img)
plt.title("Trace the Glacier Outline")
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.show()

print("Click along the glacier outline to trace its shape. Double-click to finish.")

# Step 2: User traces the glacier's outline
glacier_outline = plt.ginput(n=-1, timeout=0, show_clicks=True)
glacier_outline = np.array(glacier_outline)

# Separate the points into x (horizontal) and y (vertical)
x_points = glacier_outline[:, 0]
y_points = glacier_outline[:, 1]

# Step 3: Plot the traced outline
plt.imshow(img)
plt.plot(x_points, img.shape[0] - glacier_outline[:, 1], 'r-', label="Glacier Outline")
plt.legend()
plt.title("Traced Glacier Outline")
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.gca().invert_yaxis()  # Invert the y-axis to make it go from 0 to 400 upwards
plt.show()


# Step 4: Calculate the cross-sectional area using numerical integration
# Scaling factor (pixels to real-world units)
# Replace these with actual measurements or estimates
pixel_to_meter = 1  # Conversion factor from pixels to meters
depth_of_glacier = 1000  # Approximate depth of the glacier in meters

# Convert pixel coordinates to meters
x_points_meters = x_points * pixel_to_meter
y_points_meters = y_points * pixel_to_meter

# Use `quad` for numerical integration
'''
area, _ = quad(lambda x: np.interp(x, x_points_meters, y_points_meters), 
               min(x_points_meters), 
               max(x_points_meters))
'''

# Step 5: Estimate the volume
volume = area * depth_of_glacier

# Display results
print(f"Cross-sectional Area: {area:.2f} square meters")
print(f"Estimated Glacier Volume: {volume:.2f} cubic meters")

# Optional: Save traced data for later use
np.savetxt("glacier_outline.csv", glacier_outline, delimiter=",", header="x,y", comments="")