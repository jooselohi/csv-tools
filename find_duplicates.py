import pandas as pd
import sys


def find_duplicates(file_path, column_name):
    """
    This function reads a CSV file and checks for duplicate values in a specified column,
    filtering out NaN values in the process.

    Parameters:
    - file_path: str, path to the CSV file
    - column_name: str, name of the column to check for duplicates

    Returns:
    - Prints the rows with duplicate values in the specified column, grouped by the duplicate values.
    """
    try:
        data = pd.read_csv(file_path)

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        data = data.dropna(subset=[column_name])  # Remove rows with NaN in column

        duplicate_rows = data[data.duplicated(subset=column_name, keep=False)]

        if duplicate_rows.empty:
            print(f"No duplicates found in the column '{column_name}'.")
        else:
            print("Duplicate rows found:")
            grouped_duplicates = duplicate_rows.sort_values(by=column_name)
            print(grouped_duplicates[[column_name, "name"]])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <CSV_FILE_PATH> <COLUMN_NAME>")
    else:
        file_path = sys.argv[1]
        column_name = sys.argv[2]
        find_duplicates(file_path, column_name)
