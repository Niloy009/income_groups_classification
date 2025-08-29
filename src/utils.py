"""Utility functions for data processing and analysis."""

import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def calculate_missing_percentage(df: pd.DataFrame) -> None:
    """Calculates the percentage of missing values for each column in the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        None: Prints the percentage of missing values for each column.
    """
    # Calculate and print missing value percentages
    total_rows = len(df)
    for column in df.columns:
        missing_count = df[column].isnull().sum()
        missing_percentage = (missing_count / total_rows) * 100
        print(f"Column '{column}': Total missing Values: {missing_count} - Percentage: {missing_percentage:.2f}%")

def plot_feature_distributions(df, cols=None, bins=30, top_n=None, ncols=3, figsize=(15, 12)):
    """
    Plots distributions for both numerical and categorical columns in a grid layout.

    Args:
        df (pd.DataFrame): Input dataframe
        cols (list, optional): Subset of columns to plot. If None, all columns are used.
        bins (int): Number of bins for numeric histograms.
        top_n (int, optional): Show only top_n categories for categorical columns.
        ncols (int): Number of subplot columns in the grid.
        figsize (tuple): Overall figure size (width, height).
    """
    if cols is None:
        cols = df.columns

    # Determine grid size
    n_features = len(cols)
    nrows = math.ceil(n_features / ncols)

    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = axes.flatten()  # make iterable

    i = -1  # Initialize i in case cols is empty
    for i, col in enumerate(cols):
        ax = axes[i]
        if pd.api.types.is_numeric_dtype(df[col]):
            # Numeric distribution
            sns.histplot(df[col].dropna(), kde=True, bins=bins, ax=ax)
            ax.set_xlabel(col)
            ax.set_ylabel("Frequency")
        else:
            # Categorical distribution
            order = df[col].value_counts().index
            if top_n:
                order = order[:top_n]
            sns.countplot(y=col, data=df, order=order, ax=ax)
            ax.set_xlabel("Count")
            ax.set_ylabel(col)

        ax.set_title(f"{col}")

    # Remove empty subplots if any
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
