import pandas as pd
import sys
import os
import argparse


def find_duplicates(file_path, column_name, output_dir=None):
    """
    This function reads a CSV file and checks for duplicate values in a specified column,
    filtering out NaN values in the process. If an output directory is provided,
    it writes duplicate entries to a new CSV file in the specified output directory.

    Parameters:
    - file_path: str, path to the CSV file
    - column_name: str, name of the column to check for duplicates
    - output_dir: str, optional directory to save the duplicates CSV (default is None)

    Returns:
    - Prints the rows with duplicate values in the specified column, grouped by the duplicate values.
    """
    try:
        data = pd.read_csv(file_path)

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        data = data.dropna(
            subset=[column_name]
        )  # Remove rows with NaN in the specified column

        duplicate_rows = data[data.duplicated(subset=column_name, keep=False)]

        if duplicate_rows.empty:
            print(f"No duplicates found in the column '{column_name}'.")
        else:
            print(f"Duplicate rows found:")
            grouped_duplicates = duplicate_rows.sort_values(by=column_name)
            print(grouped_duplicates)

            if output_dir:  # Only save to file if output_dir is provided
                os.makedirs(output_dir, exist_ok=True)
                output_file_path = os.path.join(output_dir, "duplicates.csv")
                grouped_duplicates.to_csv(output_file_path, index=False)
                print(f"Duplicate rows written to '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find and save duplicates in a specified column of a CSV file."
    )
    parser.add_argument("file_path", type=str, help="Path to the CSV file")
    parser.add_argument(
        "column_name", type=str, help="Name of the column to check for duplicates"
    )
    parser.add_argument(
        "-d",
        "--output_dir",
        type=str,
        help="Directory to output the results",
        default=None,  # Set default to None
    )

    args = parser.parse_args()

    find_duplicates(args.file_path, args.column_name, args.output_dir)
