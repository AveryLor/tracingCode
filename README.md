# ModellingEssayCode

This repository contains the code for tracing the glacier outline in an image and fitting a polynomial to the traced points. The model is intended for analyzing the glacier's shape and estimating its volume based on its cross-sectional area.

## Features

- **Image Tracing**: Allows users to trace the glacier's outline directly on an image.
- **Polynomial Fit**: Fits a polynomial to the traced points to model the glacier's outline.
- **Visualization**: Displays the original image with the fitted polynomial overlayed for easy visual inspection.
- **Data Output**: The traced points are saved for future analysis, and the polynomial equation is displayed.

## Requirements

Before running the code, make sure you have the following libraries installed:

- `numpy` - for numerical computations
- `matplotlib` - for plotting and visualization
- `scipy` (optional, for integration and area estimation)

You can install these dependencies using `pip`:

```bash
pip install numpy matplotlib scipy
```
