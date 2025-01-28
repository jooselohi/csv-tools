import pandas as pd
import sys


def search_column(file_path, column_name, query):
    """
    This function reads a CSV file and searches for rows where the specified column
    contains the given query string.

    Parameters:
    - file_path: str, path to the CSV file
    - column_name: str, name of the column to search in
    - query: str, the substring to search for in the column values

    Returns:
    - Prints the rows where the column values contain the query string.
    """
    try:
        data = pd.read_csv(file_path)

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        # Filtering data to find rows where the column contains the query
        matching_rows = data[data[column_name].str.contains(query, na=False)]

        if matching_rows.empty:
            print(f"No rows found containing '{query}' in column '{column_name}'.")
        else:
            print(f"Rows containing '{query}' in column '{column_name}':")
            print(matching_rows)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <CSV_FILE_PATH> <COLUMN_NAME> <QUERY>")
    else:
        file_path = sys.argv[1]
        column_name = sys.argv[2]
        query = sys.argv[3]
        search_column(file_path, column_name, query)
