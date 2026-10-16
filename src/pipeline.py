import pandas as pd
import numpy as np
from pathlib import Path

def load_data(input_path):
    df = pd.read_csv(input_path)
    return df

def inspect_data(df):
    print("Dataset shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

def parse_transaction_date(value):
    if pd.isna(value):
        return pd.NaT
    value = str(value).strip()

    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%d-%b-%Y",
    ]

    for date_format in formats:
        try:
            return pd.to_datetime(value, format=date_format)
        except ValueError:
            continue

    return pd.NaT

def clean_data(df):
    df = df.copy()

    df["transaction_date"] = df["transaction_date"].apply(
    parse_transaction_date
    )

    categorical_cols = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    for col in categorical_cols:
        df[col] = df[col].str.strip().str.lower()

    df = df.drop_duplicates()

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    for col in categorical_cols:
        if df[col].isnull().any():
            mode_values = df[col].mode()
            if not mode_values.empty:
                df[col] = df[col].fillna(mode_values[0])

    if df["transaction_date"].isnull().any():
        median_date = df["transaction_date"].median()

        if pd.notna(median_date):
            df["transaction_date"] = df["transaction_date"].fillna(median_date)

    return df

def transform_data(df):
    df = df.copy()

    numeric_cols = df.select_dtypes(include="number").columns

    col_min = df[numeric_cols].min()
    col_max = df[numeric_cols].max()

    denominator = (col_max - col_min).replace(0, 1)

    df[numeric_cols] = (
        df[numeric_cols] - col_min
    ) / denominator

    categorical_cols = df.select_dtypes(include=["object", "string", "category"]).columns

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        dtype=int
    )

    return df

def run_pipeline(input_path, output_path):
    df = load_data(input_path)
    df_clean = clean_data(df)
    df_processed = transform_data(df_clean)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df_processed.to_csv(output_path, index=False)
    print("Pipeline completed successfully!")
    print("Raw shape:", df.shape)
    print("Cleaned shape:", df_clean.shape)
    print("Processed shape:", df_processed.shape)
    print("Output saved to:", output_path)

