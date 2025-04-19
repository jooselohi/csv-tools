import pandas as pd
import sys


def filter_date_range(input_file, date_column, start_date, end_date, output_file):
    """
    This function reads a CSV file, filters rows based on a specified date range in a given date column,
    and then saves the filtered data to another CSV file.

    Parameters:
    - input_file: str, path to the input CSV file
    - date_column: str, the name of the date column to apply the filter on
    - start_date: str, the start of the date range (inclusive), in YYYY-MM-DD format
    - end_date: str, the end of the date range (inclusive), in YYYY-MM-DD format
    - output_file: str, path to the output CSV file where filtered data will be saved

    Returns:
    - Saves filtered rows to a new CSV file.
    """
    try:
        data = pd.read_csv(
            input_file, dtype={"business_id": str, "id": str, "phone_number": str}
        )

        # Convert the date column to datetime with UTC
        data[date_column] = pd.to_datetime(data[date_column], errors="coerce", utc=True)
        data = data.dropna(subset=[date_column])

        # Ensure that start_date and end_date are also timezone-aware
        start_dt = pd.to_datetime(start_date).tz_localize("UTC")
        end_dt = pd.to_datetime(end_date).tz_localize("UTC")

        mask = (data[date_column] >= start_dt) & (data[date_column] <= end_dt)
        filtered_data = data.loc[mask]
        filtered_data.to_csv(output_file, index=False)
        print(f"Filtered data saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Usage: python3 main.py <INPUT_FILE> <DATE_COLUMN> <START_DATE> <END_DATE> <OUTPUT_FILE>"
        )
    else:
        input_file = sys.argv[1]
        date_column = sys.argv[2]
        start_date = sys.argv[3]
        end_date = sys.argv[4]
        output_file = sys.argv[5]
        filter_date_range(input_file, date_column, start_date, end_date, output_file)
