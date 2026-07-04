# Seaborn Personal Documentation & Reference Guide

Official API Reference: https://seaborn.pydata.org/api.html

---

## 1. Architectural Foundations

### Why Seaborn?
* Abstraction Layer: Built on top of Matplotlib; achieves complex plots with much less code.
* Aesthetics: Elegant default themes, color palettes, and grid layouts.
* Statistical Native: Built-in calculation engines for aggregation, regression lines, and confidence intervals.

### Figure-Level vs. Axis-Level Functions
Seaborn splits its API into two core architectural approaches:

| Feature | Axis-Level Functions (scatterplot, histplot) | Figure-Level Functions (relplot, displot, catplot) |
| :--- | :--- | :--- |
| Returns | Matplotlib AxesSubplot object. | Seaborn FacetGrid object. |
| Grid Target | Fits easily into pre-defined Matplotlib subplots. | Sets up and manages its own global figure layout wrapper. |
| Faceting | Does not natively support structural row/column matrix splitting. | Seamless multi-plot splitting via col= and row= parameters. |
| Sizing | Managed via standard Matplotlib figure size tools. | Managed explicitly via functional arguments (height, aspect). |

---

## 2. Seaborn API Roadmap

                    ┌─────────────────────────┐
                    │      seaborn.plot       │
                    └────────────┬────────────┘
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
   Relational Plots      Distribution Plots      Categorical Plots
    (relplot)              (displot)               (catplot)
   ├── scatterplot        ├── histplot            ├── stripplot / swarmplot
   └── lineplot           ├── kdeplot             ├── boxplot / violinplot
                          └── rugplot             └── barplot / countplot

---

## 3. Core Plot Types Reference

### 3.1 Relational Plots (Visualizing Relationships)
Primary Function: sns.relplot(data, x, y, kind)

**Scatter Plot**:

    # Axis-Level
    sns.scatterplot(data=df, x='col_x', y='col_y', hue='cat_col', style='cat_col', size='num_col')

    # Figure-Level (Supports Faceting matrix arrays)
    sns.relplot(data=df, x='col_x', y='col_y', kind='scatter', col='col_cat', row='row_cat')

**Line Plot**:

    # Axis-Level
    sns.lineplot(data=df, x='time_col', y='metric_col', hue='group_col')

    # Figure-Level
    sns.relplot(data=df, x='time_col', y='metric_col', kind='line', errorbar=None)

---

### 3.2 Distribution Plots (Univariate & Bivariate Data Shapes)

#### Primary Function: 

sns.displot(data, x, y, kind)

#### Histogram (histplot):

 **1D Univariate Histogram**

    sns.histplot(data=df, x='total_bill', bins=30, kde=True)

 **2D Bivariate Heatmap Histogram** 

    sns.histplot(data=df, x='total_bill', y='tip', cbar=True)

#### Kernel Density Estimate (kdeplot):

Calculates and plots a smooth, continuous mathematical distribution using Gaussian kernels.

    sns.kdeplot(data=df, x='total_bill', fill=True, bw_adjust=0.5)

#### Rug Plot (rugplot):

Draws tiny tick marks along the axes to mark individual observation locations.

    sns.kdeplot(data=df, x='total_bill')
    sns.rugplot(data=df, x='total_bill')

---

### 3.3 Categorical Plots (Grouped Column Comparisons)

#### Primary Function: sns.catplot(data, x, y, kind)

    # Figure-Level Syntax Template
    sns.catplot(data=df, x='category', y='numeric', kind='box|violin|bar|count|strip|swarm')

Categorical Scatter Plots
* stripplot: Jitters points slightly along the categorical axis to resolve overplotting.
* swarmplot: Adjusts points automatically along the axis so they do not overlap.

Categorical Distribution Plots
* boxplot: Highlights the five-number summary (Min, Q1, Median, Q3, Max) alongside outliers.
* violinplot: Combines a classic box plot container with a mirrored KDE distribution.

Categorical Estimate Plots (Central Tendency)
* barplot: Computes the statistical mean per group category and overlays a confidence interval error bar.
* countplot: A specialized histogram for categorical data that tallies the frequency count.

---

### 3.4 Regression Plots (Linear Visualizations)
Both methods plot a linear regression model fit (y ~ x) with a shaded 95% statistical confidence interval wrapper.

    # Axis-Level (Fast, simple, lacks hue support matrix processing)
    sns.regplot(data=df, x='total_bill', y='tip')

    # Figure-Level (Supports row/col faceting and hue grouping parameters)
    sns.lmplot(data=df, x='total_bill', y='tip', hue='smoker', col='time')

---

### 3.5 Matrix Plots (Grid Heatmaps)
Requires rectangular matrix inputs where row headers and column fields serve as coordinates (e.g., pivot tables or .corr() output matrices).

**Heatmap**:

    sns.heatmap(df.corr(), annot=True, linewidths=0.5, cmap='coolwarm', fmt=".2f")

**Clustermap**:

Uses Scipy under the hood to perform hierarchical clustering.
    sns.clustermap(df.corr(), cmap='viridis')

---

## 4. Multi-Plot Grid Objects (Advanced Custom Layouts)

### 4.1 Structural Faceting (FacetGrid)

When you want total control over mapping customized subplots manually across data subsets.

    g = sns.FacetGrid(data=df, col='time', row='smoker')
    g.map(sns.scatterplot, 'total_bill', 'tip')
    g.add_legend()

### 4.2 Pairwise Data Testing (pairplot vs PairGrid)

Used to automatically map interactions across all numerical features inside a DataFrame.

#### pairplot: Fast out-of-the-box shortcut template. 

    sns.pairplot(df, hue='species')

#### PairGrid: Highly customizable engine wrapper. 

    g = sns.PairGrid(df, hue='species')
    g.map_upper(sns.scatterplot) # Upper right triangle
    g.map_diag(sns.histplot)     # Diagonal blocks
    g.map_lower(sns.kdeplot)     # Lower left triangle

### 4.3 Joint Relationship Projections (jointplot vs JointGrid)

Combines a bivariate relationship graph with univariate marginal distributions.

#### jointplot: Quick shortcut call.

    sns.jointplot(data=df, x='total_bill', y='tip', kind='reg')

#### JointGrid: Manual layout framework.

    g = sns.JointGrid(data=df, x='total_bill', y='tip')
    g.plot_joint(sns.scatterplot, color="m")
    g.plot_marginals(sns.histplot, kde=True)


subplot