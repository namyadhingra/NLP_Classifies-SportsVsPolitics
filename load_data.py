# load_data.py

import pandas as pd

def load_data(file_path):
    # Loads CSV file and performs structural cleaning.
    # Keeps only required columns and removes missing values.

    df = pd.read_csv(file_path)

    # Keep only necessary columns
    df = df[["category", "text"]]

    # Remove rows with missing values
    df = df.dropna()

    return df


if __name__ == "__main__":
    FILE_PATH = "indian_news_with_text.csv"

    df = load_data(FILE_PATH)

    print("Rows retained:", len(df))

    # Optional: save cleaned version separately
    df.to_csv("india_news_cleaned.csv", index=False)
