import pandas as pd




def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file."""

    return pd.read_csv(file_path)

def get_columns(path:str) ->list[str]:
    '''
    Return every column name in the csv file
    
    '''

    return read_csv(path).columns.tolist()