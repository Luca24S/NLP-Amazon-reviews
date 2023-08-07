import json
import pandas as pd

def readJSON(file_path):
    """Reads a JSON file and loads it into a DataFrame."""
    data = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                data.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                print(f"Error decoding JSON: {line}")
    return pd.DataFrame(data)

def save_to_json(df, file_path):
    """Saves a DataFrame to a JSON file."""
    df.to_json(file_path, orient="records", lines=True)