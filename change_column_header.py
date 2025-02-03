import pandas as pd
import sys


def change_column_header(input_file, old_header, new_header, output_file):
    """
    This function reads a CSV file, renames a specified column header from an old name to a new name,
    and saves the modified data to an output CSV file.

    Returns:
    - Saves the data with the modified column header to an output CSV file.
    """
    try:
        data = pd.read_csv(input_file)

        if old_header not in data.columns:
            print(f"Column '{old_header}' does not exist in the CSV file.")
            return

        data.rename(columns={old_header: new_header}, inplace=True)
        data.to_csv(output_file, index=False)
        print(f"Modified data with new column header saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 6 or sys.argv[4] != "-d":
        print(
            "Usage: python3 main.py <INPUT_FILE> <OLD_COLUMN_HEADER> <NEW_COLUMN_HEADER> -d <OUTPUT_FILE>"
        )
    else:
        input_file = sys.argv[1]
        old_header = sys.argv[2]
        new_header = sys.argv[3]
        output_file = sys.argv[5]
        change_column_header(input_file, old_header, new_header, output_file)
