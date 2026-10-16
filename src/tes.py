import pandas as pd

def load_data(input_path):
    df = pd.read_csv(input_path)
    return df

def clean_data(data):
    data = data.copy()
    print(data.head())
    return data

df_raw = load_data("data/raw/automobileEDA.csv")

df_clean = clean_data(df_raw)