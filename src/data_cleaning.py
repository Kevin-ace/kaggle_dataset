def clean_data(df):
    """Basic data cleaning steps like handling missing values"""
    df = df.dropna()  # Drop missing values for simplicity
    return df
