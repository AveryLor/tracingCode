import matplotlib.pyplot as plt
import numpy as np
# Step 1: Load the glacier image
#image_path = "images/1918-GlacierImage.png"  
image_path = "images/2018-GlacierImage.png" #Change which line is commented out based on which image you want to analyze
img = plt.imread(image_path)

# Display the image
plt.imshow(img)
plt.title("Trace the Glacier Outline")
plt.xlabel("Width (pixels)")
plt.ylabel("Height (pixels)")
plt.show()

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




