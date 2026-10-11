from src.validator import *
from src.CONTENT import *



if __name__ == "__main__":

    file_path = FILE_PATH

    columns = get_columns(file_path)

    print(f"Columns in the CSV file: {columns}")

