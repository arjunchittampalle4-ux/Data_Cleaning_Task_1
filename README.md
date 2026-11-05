# Data Analyst Internship – Task 1

## Data Cleaning and Preprocessing

### Objective

The objective of this project is to clean and prepare a raw dataset
containing missing values, duplicate records and inconsistent formats.

### Tools Used

- Python
- Pandas
- VS Code

### Dataset

A random customer purchase dataset was created for this project.
The raw dataset intentionally contains common data-quality problems.

### Problems Identified

- Missing values
- Duplicate records
- Inconsistent gender values
- Inconsistent country names
- Inconsistent city names
- Different date formats
- Invalid numeric values
- Extra spaces in text
- Non-uniform column names

### Data Cleaning Steps

1. Loaded the raw CSV dataset using Pandas.
2. Standardized column names.
3. Removed duplicate records.
4. Removed unnecessary spaces.
5. Standardized gender values.
6. Standardized country names.
7. Standardized city names.
8. Converted numeric columns to appropriate data types.
9. Converted purchase dates into a consistent format.
10. Filled missing numerical values using the median.
11. Filled missing categorical values using the mode.
12. Saved the cleaned dataset.

### Project Files

- `raw_customer_dataset.csv` – Original dirty dataset
- `clean_data.py` – Python cleaning program
- `cleaned_customer_dataset.csv` – Final cleaned dataset
- `cleaning_summary.txt` – Summary of cleaning operations
- `README.md` – Project documentation

### Result

The raw dataset was successfully cleaned and transformed into a
structured dataset suitable for further analysis and visualization.