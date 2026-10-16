# Automobile Data Preparation Pipeline

## 1. Project Overview

This project implements a reusable data preparation pipeline using Python and Pandas. The pipeline processes a dirty automobile dataset, handles missing values and duplicate records, standardizes categorical values, and transforms the data into a machine-learning-friendly format.

The pipeline reads a raw CSV file and generates a processed CSV file automatically.

## 2. Objectives

- Inspect and understand the raw dataset.
- Handle missing values in numerical, categorical, and date columns.
- Remove duplicate records.
- Standardize inconsistent categorical values.
- Apply Min-Max scaling to numerical columns.
- Apply one-hot encoding to categorical columns.
- Automate the workflow using reusable Python functions.

## 3. Technologies Used

- Python 3.11
- Pandas
- NumPy
- pathlib
- Jupyter Notebook

## 4. Project Structure

```text
data-pipeline-assignment/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── pipeline.py
├── documentation/
├── exploration.ipynb
└── README.md
```

- `data/raw/`: stores the original automobile dataset.
- `data/processed/`: stores the processed CSV output.
- `src/pipeline.py`: contains the reusable pipeline functions.
- `documentation/`: stores project documentation and diagrams.
- `exploration.ipynb`: contains exploratory analysis and development experiments.

## 5. Pipeline Stages

### 5.1 Data Loading

The `load_data()` function reads the raw CSV file into a Pandas DataFrame.

### 5.2 Data Inspection

The `inspect_data()` function reports the dataset dimensions, data types, missing values, and duplicate rows.

### 5.3 Data Cleaning

The `clean_data()` function:

- Converts `transaction_date` to datetime format.
- Standardizes categorical string values by trimming whitespace and converting text to lowercase.
- Removes duplicate rows.
- Fills missing numerical values using the median.
- Fills missing categorical values using the mode.
- Fills remaining missing dates using the median date.

### 5.4 Data Transformation

The `transform_data()` function:

- Applies Min-Max scaling to numerical columns.
- Applies one-hot encoding to categorical columns.

### 5.5 Data Export

The `run_pipeline()` function combines loading, cleaning, and transformation, then exports the resulting DataFrame to a CSV file.

## 6. How to Run

Ensure that the raw dataset is located at:

`data/raw/automobileEDA_dirty_training.csv`

Install the dependencies:

```bash
pip install pandas numpy
```

Run the pipeline from the project root using Python:

```python
from src.pipeline import run_pipeline

df_processed = run_pipeline(
    input_path="data/raw/automobileEDA_dirty_training.csv",
    output_path="data/processed/automobileEDA_processed.csv"
)
```

The processed dataset will be saved at:

`data/processed/automobileEDA_processed.csv`

## 7. Results

The pipeline produced the following results during testing:

| Stage | Rows | Columns |
|---|---:|---:|
| Raw dataset | 205 | 30 |
| Cleaned dataset | 201 | 30 |
| Processed dataset | 201 | 81 |

Four duplicate rows were removed. Categorical encoding expanded the dataset from 30 to 81 columns.

## 8. Output Validation

The generated CSV should be checked for:

- Expected dataset dimensions.
- Remaining missing values.
- Duplicate records.
- Correct numerical scaling and categorical encoding.

## 9. Limitations

- Median and mode imputation may not be appropriate for every dataset.
- Ambiguous date formats should be validated to ensure dates are interpreted correctly.
- Min-Max scaling is sensitive to extreme values.
- One-hot encoding increases the number of columns when categorical variables have many distinct values.
