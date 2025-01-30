import pandas as pd
import sys
import os


def column_to_array(file_path, column_name):
    """
    This function reads a CSV file and extracts unique values from a specified column,
    then saves these values to a new CSV file in a specified directory, separated by commas.

    Parameters:
    - file_path: str, path to the CSV file
    - column_name: str, name of the column to extract values from

    Returns:
    - Saves the unique values to 'output/column_values.csv'.
    """
    try:
        data = pd.read_csv(file_path)

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        unique_values = data[column_name].dropna().unique()

        # Create output directory if it doesn't exist
        output_directory = "output"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        output_path = os.path.join(output_directory, "column_values.csv")

        # Save the unique values to a new CSV file
        pd.DataFrame({column_name: unique_values}).to_csv(
            output_path, index=False, header=False
        )

        print(
            f"Unique values from column '{column_name}' have been written to '{output_path}'."
        )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <CSV_FILE_PATH> <COLUMN_NAME>")
    else:
        file_path = sys.argv[1]
        column_name = sys.argv[2]
        column_to_array(file_path, column_name)
