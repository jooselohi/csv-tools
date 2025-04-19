import pandas as pd
import sys


def remove_rows_with_missing_values(input_file, missing_column_header, output_file):
    """
    This function reads a CSV file, removes rows that contain missing values in a specified column,
    and saves the modified data to an output CSV file.

    Returns:
    - Saves the data without rows containing missing values in the specified column to an output CSV file.
    """
    try:
        data = pd.read_csv(
            input_file, dtype={"business_id": str, "id": str, "phone_number": str}
        )

        if missing_column_header not in data.columns:
            print(f"Column '{missing_column_header}' does not exist in the CSV file.")
            return

        data.dropna(subset=[missing_column_header], inplace=True)
        data.to_csv(output_file, index=False)
        print(
            f"Data with rows containing missing values in column '{missing_column_header}' removed saved to {output_file}"
        )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[3] != "-d":
        print(
            "Usage: python3 main.py <INPUT_FILE> <MISSING_COLUMN_HEADER> -d <OUTPUT_FILE>"
        )
    else:
        input_file = sys.argv[1]
        missing_column_header = sys.argv[2]
        output_file = sys.argv[4]
        remove_rows_with_missing_values(input_file, missing_column_header, output_file)
