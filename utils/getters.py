"""
Script with getter function for generating random data showing ID, gender and income.
"""

import pandas as pd
import numpy as np

def generate_random_data(n_id:int=1000, years:np.array= np.arange(2015, 2025), gender_list:list =["M", "F", "N/A"], base_income:float=30000) -> pd.DataFrame:
    """
    Generates a random dataset showing ID, gender, year and income.

    Args:
        n_id (int, optional): number of individuals to generate. Defaults to 1000.
        years (np.array, optional): range of years. Defaults to np.arange(2015, 2025).
        gender_list (list, optional): Gender. Defaults to ["M", "F", "N/A"].
        base_income (float, optional): Base income. Defaults to 30000.

    Returns:
        pd.DataFrame: generated dataset
    """
    # Assign gender and base income + growth rate per ID
    id_df = pd.DataFrame({
        'id': np.arange(1, n_id + 1),
        'gender': np.random.choice(gender_list, size=n_id),
        'base_income': np.round(np.random.normal(base_income, 10000, size=n_id), -2),
        'growth_rate': np.random.uniform(0.01, 0.05, size=n_id)  # annual income growth: 1–5%
    })

    # Create (id, year) pairs
    df = pd.merge(id_df, pd.DataFrame({'year': years}), how='cross')

    # Calculate year offset per person
    df['year_offset'] = df['year'] - years.min()

    # Adjust income
    df['yearly_income'] = (
        df['base_income'] * (1 + df['growth_rate']) ** df['year_offset']
    )

    # Gender adjustment
    gender_adjustment = {'M': 1.1, 'F': 1.0, 'N/A': 0.9}
    df['yearly_income'] *= df['gender'].map(gender_adjustment)

    # Round to nearest 100
    df['yearly_income'] = df['yearly_income'].round(-2)

    df = df[['id', 'gender', 'year', 'yearly_income']]

    return df