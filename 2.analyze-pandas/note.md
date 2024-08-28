## Basic ways to manipulate data

- Column addition: Use df["new_col"] = value to create new columns in a DataFrame.
- Aggregates: groupby and agg compute summary metrics that can be joined to the original DataFrame.
- Boolean indexing: Create new columns based on conditions using df["new_col"] = df["existing_col"] > threshold.
- pivot_table: Reshape data, providing a multidimensional analysis tool similar to pivot tables in Excel. Specify index, columns, values, and aggfunc parameters.
- groupby: Segment data based on column values. Create a GroupBy object and use methods like sum, mean, or apply for aggregation or transformation.
- join: Combine two DataFrames based on their indexes or specified columns. Use on, how (left, right, inner, or outer) parameters to control the join type.
