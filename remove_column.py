import pandas as pd
import sys


def remove_column(input_file, column_to_remove, output_file):
    """
    This function reads a CSV file, removes a specified column, and saves the modified data to an output CSV file.

    Returns:
    - Saves the data without the specified column to an output CSV file.
    """
    try:
        data = pd.read_csv(input_file)

        if column_to_remove not in data.columns:
            print(f"Column '{column_to_remove}' does not exist in the CSV file.")
            return

        data.drop(columns=[column_to_remove], inplace=True)
        data.to_csv(output_file, index=False)
        print(f"Data with column '{column_to_remove}' removed saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[3] != "-d":
        print(
            "Usage: python3 main.py <INPUT_FILE> <REMOVE_COLUMN_HEADER> -d <OUTPUT_FILE>"
        )
    else:
        input_file = sys.argv[1]
        column_to_remove = sys.argv[2]
        output_file = sys.argv[4]
        remove_column(input_file, column_to_remove, output_file)
