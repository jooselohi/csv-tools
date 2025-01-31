import pandas as pd
import sys
import argparse


def search_column(file_path, column_name, query, output_path=None):
    """
    This function reads a CSV file and searches for rows where the specified column
    contains the given query string.

    Parameters:
    - file_path: str, path to the CSV file
    - column_name: str, name of the column to search in
    - query: str, the substring to search for in the column values
    - output_path: str, optional, path to output the results to a CSV file

    Returns:
    - Prints the rows where the column values contain the query string.
      Optionally, outputs the results to a CSV file.
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
            if output_path:
                matching_rows.to_csv(output_path, index=False)
                print(f"Results saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search a CSV file for rows containing a query in a specific column."
    )
    parser.add_argument("file_path", type=str, help="Path to the CSV file")
    parser.add_argument("column_name", type=str, help="Name of the column to search in")
    parser.add_argument("query", type=str, help="Substring to search for in the column")
    parser.add_argument(
        "-d",
        "--output",
        type=str,
        help="Path to output the results to a CSV file",
        default=None,
    )

    args = parser.parse_args()

    search_column(args.file_path, args.column_name, args.query, args.output)
