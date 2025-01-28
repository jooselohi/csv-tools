import pandas as pd
import sys


def csv_to_json(file_path, json_path):
    """
    This function reads a CSV file and converts it to a JSON file.

    Parameters:
    - file_path: str, path to the CSV file
    - json_path: str, path where the JSON file will be saved

    Returns:
    - Saves the CSV file as a JSON file with each row as a JSON object.
    """
    try:
        # Reading the CSV file
        data = pd.read_csv(file_path)

        # Converting to JSON format
        json_data = data.to_json(orient="records")

        # Writing the JSON data to a file
        with open(json_path, "w") as json_file:
            json_file.write(json_data)

        print(f"CSV has been successfully converted to JSON and saved to {json_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <CSV_FILE_PATH> <JSON_FILE_PATH>")
    else:
        file_path = sys.argv[1]
        json_path = sys.argv[2]
        csv_to_json(file_path, json_path)
