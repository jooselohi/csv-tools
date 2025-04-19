import pandas as pd
import sys


def print_header(file_path):
    """
    This function reads the header row from a CSV file and prints it.

    Parameters:
    - file_path: str, path to the CSV file

    Returns:
    - Prints the header row with the column titles if it exists.
    """
    try:
        # Using 'nrows=0' to only read the header without loading any data
        data = pd.read_csv(
            file_path,
            nrows=0,
            dtype={"business_id": str, "id": str, "phone_number": str},
        )

        if data.columns.empty:
            print("No header row found in the CSV file.")
        else:
            print("Header row with column titles:")
            print(list(data.columns))  # Printing as a list for better readability

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <CSV_FILE_PATH>")
    else:
        file_path = sys.argv[1]
        print_header(file_path)
