import pandas as pd
import argparse


def find_and_delete(file_path, column_name, value_to_delete, output_path):
    try:
        # Read the CSV file
        data = pd.read_csv(
            file_path,
            dtype={
                "business_id": str,
                "id": str,
                "phone_number": str,
                "phone_number": str,
            },
        )

        if column_name not in data.columns:
            print(f"Column '{column_name}' does not exist in the CSV file.")
            return

        # Count initial rows
        initial_row_count = len(data)

        # Remove rows where the column contains the specified value (case-insensitive)
        data = data[
            ~data[column_name].str.contains(value_to_delete, case=False, na=False)
        ]

        # Count removed rows
        removed_row_count = initial_row_count - len(data)

        if removed_row_count == 0:
            print(
                f"No rows found containing '{value_to_delete}' in column '{column_name}'."
            )
            # Save the modified DataFrame to the output file
            data.to_csv(output_path, index=False)
            print(f"Modified data saved to {output_path} \033[92m✓\033[39m")
        else:
            print(
                f"Removed {removed_row_count} row(s) containing '{value_to_delete}' in column '{column_name}'."
            )

            # Save the modified DataFrame to the output file
            data.to_csv(output_path, index=False)
            print(f"Modified data saved to {output_path} \033[92m✓\033[39m")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Remove rows from a CSV file where a specific column contains a given value."
    )
    parser.add_argument("file_path", type=str, help="Path to the input CSV file")
    parser.add_argument("column_name", type=str, help="Name of the column to search in")
    parser.add_argument(
        "value_to_delete", type=str, help="Value to find and delete in the column"
    )
    parser.add_argument(
        "-d",
        "--output",
        type=str,
        required=True,
        help="Path to save the output CSV file",
    )

    args = parser.parse_args()

    find_and_delete(args.file_path, args.column_name, args.value_to_delete, args.output)
