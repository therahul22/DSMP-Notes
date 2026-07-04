# Plotly Interactive Data Visualization Reference Guide

## 1. Overview & Advantages
Plotly is a powerful, interactive data visualization library supported across multiple languages (Python, JavaScript, R, Julia).

Key Advantages:
* Multi-language support (Write in Python, render in JS).
* Highly interactive out-of-the-box (Hover tooltips, zooming, panning).
* Beautiful, production-ready aesthetics.
* Seamless integration with Pandas DataFrames.

---

## 2. The Plotly Ecosystem (Roadmap)
Plotly is divided into three main tiers:

1. Plotly Graph Objects (go): The low-level, foundational engine. Highly customizable, but requires more code. Builds graphs using "Traces" and "Layouts".
2. Plotly Express (px): The high-level wrapper. Write less code, integrates perfectly with Pandas. Used for 90% of standard EDA and plotting.
3. Dash: A framework built on top of Plotly to create full-stack interactive web applications and dashboards.

Standard Imports:
    import plotly.graph_objects as go
    import plotly.express as px

---

## 3. Plotly Express (High-Level / Pandas Friendly)

Use Case: Quick, beautiful, interactive plots directly from DataFrames.

Scatter Plot (With Animations & Faceting):

    fig = px.scatter(df, x='col1', y='col2', 
                     color='category_col',     # Colors dots based on a category
                     size='numerical_col',     # Changes dot size
                     title="My Scatter Plot",
                     facet_col='region',       # Creates subplots for each region
                     animation_frame='year',   # Creates a play button to animate over time
                     animation_group='country')# Keeps track of individual entities during animation
    fig.show()

Common Express Graphs:

**Line Chart**

    fig = px.line(df, x='date', y='price', color='company')

**Bar Chart** (barmode can be 'group' or 'relative/stacked')

    fig = px.bar(df, x='category', y='sales', color='region', barmode='group')

**Histogram**

    fig = px.histogram(df, x='age', nbins=20, color='gender')

**Pie Chart**

    fig = px.pie(df, values='revenue', names='department', hole=0.3) # hole=0.3 makes a donut chart

---

## 4. Plotly Graph Objects (Low-Level / Custom Control)

Use Case: When Plotly Express doesn't support a specific customization, layering completely different types of graphs together, or making 3D Surface plots.

The Graph Objects Workflow:
1. Trace: The actual data and the type of graph (e.g., Scatter, Bar).
2. Data: A list containing one or more traces.
3. Layout: The visual styling of the overall figure (titles, axes, margins).
4. Figure: The final object combining Data and Layout.

Basic GO Example (Multiple Graphs on One Plot):

    # 1. Create Traces
    trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines+markers', name='Line Chart')
    trace2 = go.Bar(x=[1, 2, 3], y=[2, 3, 4], name='Bar Chart')

    # 2. Combine into a Data List
    data = [trace1, trace2]

    # 3. Define the Layout
    layout = go.Layout(
        title="Combined Line and Bar Chart",
        xaxis=dict(title="X-Axis Label"),
        yaxis=dict(title="Y-Axis Label")
    )

    # 4. Create Figure and Show
    fig = go.Figure(data=data, layout=layout)
    fig.show()

---

## 5. Advanced / 3D Plotting (Requires Graph Objects)

Plotly Express cannot create 3D Surface plots. You must use `graph_objects` with a meshgrid of data (similar to Matplotlib 3D surfaces).

3D Surface Plot:

    import numpy as np

    # Generate grid data
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    xGrid, yGrid = np.meshgrid(x, y)
    z = np.sin(np.sqrt(xGrid**2 + yGrid**2))

    # Create the surface trace
    trace = go.Surface(x=x, y=y, z=z, colorscale='Viridis')

    # Plot
    fig = go.Figure(data=[trace])
    fig.update_layout(title='3D Surface Plot', autosize=False, width=800, height=800)
    fig.show()