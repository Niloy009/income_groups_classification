"""
This scripts provides utilities for loading and preprocessing the income dataset
used for income group classification tasks. It includes functions to read raw data files,
assign column names, handle missing values, and optionally save the cleaned data as a CSV file.
"""

from pathlib import Path
import pandas as pd


def load_income_data(file_path: str, output_path: str = None) -> pd.DataFrame:
    """Loads the income dataset, assigns column names, replaces missing values, 
    and optionally saves it as a CSV file.
    
    Args:
        file_path (str): Path to the raw .train or .test file.
        output_path (str, optional): Path to save the cleaned CSV. If None, no file is saved.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """

    col_names = [
        "age", "workclass", "fnlwgt", "education", "education_num",
        "marital_status", "occupation", "relationship", "race", "sex",
        "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"
    ]


    # Load data
    df = pd.read_csv(file_path, header=None, names=col_names, na_values="?", skipinitialspace=True)

    # Save cleaned CSV if output path is provided
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned CSV at {output_path}")

    return df
