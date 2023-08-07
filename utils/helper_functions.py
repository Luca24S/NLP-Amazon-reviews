import os
import json
import matplotlib.pyplot as plt
from pathlib import Path

def ensure_directory_exists(directory_path):
    """
    Ensures that the specified directory exists. If not, creates it.
    
    Args:
        directory_path (str or Path): Path to the directory.
    """
    directory_path = Path(directory_path)
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)

def save_plot(fig, file_path, dpi=300):
    """
    Saves a matplotlib figure to a file.
    
    Args:
        fig (matplotlib.figure.Figure): The figure to save.
        file_path (str or Path): Path to save the figure.
        dpi (int): Resolution in dots per inch. Default is 300.
    """
    fig.savefig(file_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)

def save_json(data, file_path):
    """
    Saves a dictionary or list to a JSON file.
    
    Args:
        data (dict or list): Data to save.
        file_path (str or Path): Path to the JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_json(file_path):
    """
    Loads a JSON file into a Python object.
    
    Args:
        file_path (str or Path): Path to the JSON file.
        
    Returns:
        dict or list: Loaded JSON data.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def format_large_numbers(num):
    """
    Formats large numbers into a human-readable string (e.g., 1,000 -> 1K).
    
    Args:
        num (int or float): Number to format.
        
    Returns:
        str: Formatted string.
    """
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)

def clean_column_names(df):
    """
    Cleans DataFrame column names by removing whitespace and standardizing to lowercase.
    
    Args:
        df (pd.DataFrame): DataFrame with columns to clean.
        
    Returns:
        pd.DataFrame: DataFrame with cleaned column names.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def chunk_dataframe(df, chunk_size):
    """
    Splits a DataFrame into chunks of specified size.
    
    Args:
        df (pd.DataFrame): DataFrame to chunk.
        chunk_size (int): Number of rows per chunk.
        
    Returns:
        list of pd.DataFrame: List of DataFrame chunks.
    """
    return [df.iloc[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

def display_progress(current, total, prefix='', suffix='', length=50):
    """
    Displays a progress bar in the terminal.
    
    Args:
        current (int): Current progress.
        total (int): Total steps for the progress bar.
        prefix (str): Prefix string for the progress bar.
        suffix (str): Suffix string for the progress bar.
        length (int): Length of the progress bar. Default is 50.
    """
    progress = int(length * current // total)
    bar = '█' * progress + '-' * (length - progress)
    print(f'\r{prefix} |{bar}| {current}/{total} {suffix}', end='\r')
    if current == total:
        print()