import pandas as pd
import sys


def count_column_values(input_file, column_name, output_file):
    """
    This function reads a CSV file, counts how many times each unique value appears in a specified column,
    and saves the results to an output CSV file.

    Parameters:
    - input_file: str, path to the CSV file
    - column_name: str, the name of the column to analyze
    - output_file: str, path to the CSV file where the results will be saved

    Returns:
    - Saves the counts of each unique value in the specified column to an output CSV file.
    """
    try:
        data = pd.read_csv(input_file)
        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        value_counts = data[
            column_name
        ].value_counts()  # Count occurrences of each unique value in the column
        value_counts.to_csv(output_file, header=["Count"])

        print(
            f"Counts of each unique value in the column '{column_name}' have been saved to {output_file}"
        )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <INPUT_FILE> <COLUMN_NAME> <OUTPUT_FILE>")
    else:
        input_file = sys.argv[1]
        column_name = sys.argv[2]
        output_file = sys.argv[3]
        count_column_values(input_file, column_name, output_file)
