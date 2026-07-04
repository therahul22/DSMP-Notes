# Matplotlib & Pandas Plotting Reference Guide

## 1. Core Basics & Figure Setup

Types of Data:
* Numerical Data: Quantitative values (e.g., age, price).
* Categorical Data: Qualitative groups (e.g., gender, country).

The Foundation:

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot(x, y, color='#FF5733', linestyle='dashed', marker='o', markersize=5, label='Data 1')
    plt.show()  # Required outside of Jupyter Notebooks to render the graph

Axis & Figure Customization:

    plt.title("Graph Title")
    plt.xlabel("X-Axis Label")
    plt.ylabel("Y-Axis Label")
    plt.grid(True)           # Adds a background grid
    plt.legend()             # Displays the label defined in plt.plot()

Handling Outliers (Zooming via Limits):

    plt.xlim(start_value, end_value)
    plt.ylim(start_value, end_value)


## 2. Relational Plots (Bivariate Analysis)

### Scatter Plots:
Use Case: Finding correlation between two numerical variables.

    # Fast Scatter Shortcut (Slightly faster, but loses advanced color/size mapping)
    plt.plot(x, y, 'o')

    # Standard Scatter (Allows deep customization)
    plt.scatter(x, y, s=df['weight'], c=df['category'], cmap='viridis', alpha=0.7)
    plt.colorbar()  # Displays a vertical legend for the color map

* s (Size): Change dot size dynamically based on a column.
* c (Color): Map colors to data. (Note: Convert text categories to numbers first).
* cmap: Set color map themes (e.g., 'viridis', 'coolwarm').
* alpha: Opacity from 0.0 (transparent) to 1.0 (solid).

### Annotations & Reference Lines:
    # Label specific points (Use a loop for multiple points)
    plt.text(x_coord, y_coord, "Label Text")

    # Draw reference lines across the entire axes
    plt.axhline(y_value)  # Horizontal line
    plt.axvline(x_value)  # Vertical line


## 3. Distribution & Categorical Plots

### Histogram: Univariate analysis to find frequency counts of a single numerical column.

    plt.hist(data, bins=[0, 10, 20, 30, 40, 50])
    plt.hist(data, log=True)  # Use logarithmic scale for highly skewed data

### Bar Chart: Bivariate analysis (Numerical vs. Categorical) for aggregate analysis of groups.

    plt.bar(x, y)          # Vertical Bar Chart
    plt.barh(x, y)         # Horizontal Bar Chart
    plt.xticks(rotation='vertical')  # Fix overlapping x-axis labels

### Pie Chart: Univariate/Bivariate analysis to show proportional contribution to a whole.

    plt.pie(data, labels=['A', 'B', 'C'], autopct='%0.1f%%', explode=[0.1, 0, 0], shadow=True)


## 4. Subplots (Multiple Graphs in One Figure)

### Method 1: The Modern Object-Oriented Approach (Recommended)

Creates a Figure object and an array of Axes objects at once.

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

    # Access specific graphs via matrix indexing
    ax[0, 0].scatter(x, y)
    ax[0, 1].plot(x, y)

    # Note: Axis labeling methods change slightly in OOP mode:
    ax[0, 0].set_title("Title")
    ax[0, 0].set_xlabel("X Label")

### Method 2: The Iterative Approach

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)  # (rows, cols, index_position)
    ax1.scatter(x, y)


## 5. 3D Plotting & Advanced Grids

### 3D Scatter & Line Plots:

    fig = plt.figure()
    ax = plt.subplot(projection='3d')
    ax.scatter3D(x, y, z)

### 3D Surface Plots & Meshgrids:

    # 1. Create 1D arrays
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)

    # 2. Create a 2D meshgrid
    xx, yy = np.meshgrid(x, y)

    # 3. Define the Z function
    z = xx**2 + yy**2

    # 4. Plot
    fig = plt.figure()
    ax = plt.subplot(projection='3d')
    ax.plot_surface(xx, yy, z)

### Contour Plots: Representing 3D topology on a 2D plane.

    fig = plt.figure()
    ax = plt.subplot()  # Note: projection='3d' is NOT required for a 2D contour
    ax.contour(xx, yy, z)


## 6. Pandas Plotting Wrapper

Quick, easy visualization directly from Pandas DataFrames or Series. Less customizable than raw Matplotlib, but much faster for basic EDA.

### Series Plotting:

    # Options: 'line', 'hist', 'pie', 'bar', etc.
    s.plot(kind='line') 

### DataFrame Plotting:

    df.plot(kind='scatter', x='col1', y='col2', title="My Title", figsize=(10, 5))

    # Automatically generate a grid of subplots for all numerical columns
    df.plot(subplots=True)