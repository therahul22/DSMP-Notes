# Pandas — Data Analysis, Multi-Indexing & Transformations
---

## 1. Core Structures & Membership Mechanics 💡 *(Interview Topic)*

Pandas is built on two primary data structures:
* **`pd.Series`:** 1D labeled array capable of holding any data type.
* **`pd.DataFrame`:** 2D labeled tabular data structure with aligned axes (rows and columns).

```python
import pandas as pd

# Series Creation
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame Creation
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
```

### In-Place Modifications
Many Pandas methods accept `inplace=True` to mutate the existing DataFrame in memory directly, avoiding a copy (e.g., `df.dropna(inplace=True)`).

### Membership Operators vs. Loops
> ❓ **Interview Question: How do membership operators (`in`) behave on a Pandas Series?**
>
> **Answer:**
> * The `in` operator checks **Index labels**, NOT values.
> * Standard `for` loops iterate over the **Values** of the Series.

```python
s = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

# Membership check
'x' in s     # Output: True  (Checks Index)
100 in s     # Output: False (100 is a value, not an index!)

# Iteration
for val in s:
    print(val) # Prints 100, 200, 300 (Iterates over values)
```

---

## 2. Essential API Reference

### Data Loading & Inspection
```python
df = pd.read_csv('data.csv')

df.head(5)            # Inspect first 5 rows
df.tail(5)            # Inspect last 5 rows
df.shape              # Returns tuple: (num_rows, num_cols)
df.info()             # Overview of column dtypes, non-null counts, memory usage
df.describe()         # Summary statistics for numerical columns
df['col'].value_counts() # Frequency distribution of categorical values
df['col'].unique()    # Array of unique values
df['col'].nunique()   # Count of unique non-null values
```

### Data Cleaning & Filtering
```python
df.isnull()                          # Boolean mask of missing values
df.notnull()                         # Boolean mask of valid values
df.dropna(subset=['col1'])           # Drops rows where 'col1' has NaN
df.fillna(value=0)                   # Replaces NaNs with 0
df.drop_duplicates(subset=['col'], keep='last') # Keeps last duplicate occurrence
df.drop(columns=['col1', 'col2'])    # Drops specified columns
df.drop(index=['idx1', 'idx2'])      # Drops specified index rows

# Range & Set Filtering
df['col'].between(10, 50)            # Boolean mask for range [10, 50]
df['col'].isin(['Val1', 'Val2'])     # Boolean mask for matching values in list
df['col'].clip(lower=0, upper=100)   # Caps values outside range [0, 100]
```

### Structural Manipulations
```python
df.set_index('col')                  # Promotes column to DataFrame Index
df.reset_index()                     # Resets Index back to default integer range
df.rename(columns={'old': 'new'})    # Renames specified columns
df['col'].astype('float64')          # Casts column data type
df['col'].apply(lambda x: x * 2)     # Applies custom function element-wise
```

### Sorting & Ranking
```python
df.sort_values('col', ascending=False)               # Sorts by column values
df.sort_index(ascending=False)                        # Sorts by index labels
df.rank(ascending=False)                             # Computes numerical ranks
df.nlargest(n=5, columns='col')                      # Top N largest entries
df.nsmallest(n=5, columns='col')                     # Top N smallest entries
```

### Aggregations & Math
```python
df.sum(), df.mean(), df.median(), df.mode()
df.std(), df.var(), df.max(), df.min(), df.count()
df.corr()                            # Pairwise column correlation matrix
```

---

## 3. Combining, Merging & Grouping

### GroupBy Mechanics
> The `groupby()` operation follows the **Split-Apply-Combine** strategy and is typically applied to **categorical data**.

```python
# Grouping single column and aggregating
df.groupby('category_col')['numeric_col'].mean()

# Grouping multiple columns
df.groupby(['Dept', 'Gender'])['Salary'].agg(['mean', 'std'])
```

### Concatenation vs. Merging

```python
# Concat: Stacking DataFrames vertically or horizontally
pd.concat([df1, df2], keys=['df1_key', 'df2_key'])

# Deprecation Warning:
# df.append(df2) is deprecated in modern Pandas versions. Use pd.concat([df1, df2]) instead.
```

#### Merge / Join Types (`pd.merge`)
```python
# Inner Join: Keeps matching keys in both DataFrames
pd.merge(x, y, how='inner', on='key_col')

# Left / Right Outer Join
pd.merge(x, y, how='left', on='key_col')
pd.merge(x, y, how='right', on='key_col')

# Full Outer Join
pd.merge(x, y, how='outer', on='key_col')

# Self Join (Joining a DataFrame with itself on different keys)
x.merge(x, how='inner', left_on='manager_id', right_on='emp_id')
```

---

## 4. MultiIndex (Hierarchical Indexing) 💡 *(Interview Topic)*

Multi-indexing allows representation of **higher-dimensional data** within 1D Series or 2D DataFrames.

### Creating MultiIndex Objects
```python
# 1. From List of Tuples
tuples = [('CSE', 'Sem 1'), ('CSE', 'Sem 2'), ('ECE', 'Sem 1')]
multi_idx1 = pd.MultiIndex.from_tuples(tuples, names=['Branch', 'Semester'])

# 2. From Cartesian Product
branches = ['CSE', 'ECE']
semesters = ['Sem 1', 'Sem 2']
multi_idx2 = pd.MultiIndex.from_product([branches, semesters], names=['Branch', 'Semester'])
```

### Slicing & Indexing MultiIndex Objects
```python
# Fetching whole top-level section
s['CSE']

# Precise Tuple Lookup via .loc
s.loc[('CSE', 'Sem 1')]

# Slice ranges using .loc
s.loc[('CSE', 'Sem 1'):('ECE', 'Sem 1')]

# Positional Slicing via .iloc
s.iloc[0:4:2]
s.iloc[[1, 4, 8], [0, 1]]  # Row index positions & column index positions
```

### Sorting MultiIndex
```python
# Sort by descending order across all index levels
df.sort_index(ascending=False)

# Mixed sorting directions per level
df.sort_index(ascending=[False, True])

# Sorting a specific level
df.sort_index(level=0, ascending=False)
```

### Index Swapping & Transposition
```python
df.swaplevel(axis=0)  # Swaps row index levels
df.transpose()         # Transposes rows and columns (or df.T)
```

---

## 5. Reshaping Functions: Stack, Unstack, Pivot Table & Melt

### `stack()` and `unstack()`
* **`unstack()`:** Converts a MultiIndex Series into a DataFrame by pivoting an **inner row index level to columns**.
* **`stack()`:** The inverse operation; pivots **column levels into row index levels**.

```python
# Converting MultiIndex Series to DataFrame
df_unstacked = multi_series.unstack()

# Restoring back to MultiIndex Series
series_stacked = df_unstacked.stack()
```

### Wide vs. Long Data Transformations

#### `melt()` (Wide to Long)
Unpivots a DataFrame from wide format to long format.
```python
df_long = df.melt(id_vars=['Name'], value_vars=['Sem1_Marks', 'Sem2_Marks'],
                  var_name='Semester', value_name='Marks')
```

#### `pivot_table()` (Long to Wide Aggregation)
```python
# Basic Pivot Table
df.pivot_table(index='Category', columns='Region', values='Sales', 
               aggfunc='sum', margins=True)  # margins=True adds row/col Subtotals

# Multi-Dimensional & Mixed Aggregation Pivot
df.pivot_table(
    index=['Dept', 'Role'], 
    columns=['Year', 'Quarter'], 
    values=['Salary', 'Bonus'], 
    aggfunc={'Salary': 'mean', 'Bonus': 'sum'}
)
```

---

## 6. Pandas DateTime Utility

Pandas provides extensive time-series utilities via the `.dt` accessor.

### Converting & Extracting Components
```python
# Convert text or raw object column to DateTime64
df['date_col'] = pd.to_datetime(df['date_col'])

# DateTime Extractors via .dt
df['year'] = df['date_col'].dt.year
df['month'] = df['date_col'].dt.month
df['month_name'] = df['date_col'].dt.month_name()
df['day_name'] = df['date_col'].dt.day_name()
df['is_leap_year'] = df['date_col'].dt.is_leap_year
```
