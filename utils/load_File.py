import os
import pandas as pd

def find_files(directory):
    """
    Finds all files in a directory and its subdirectories.

    Args:
        directory (str): The directory to search.

    Returns:
        list: A list of all files in the directory and its subdirectories.
    """

    files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            if "listingLinks" in filename:
                if filename.endswith(".csv"):
                    files.append(os.path.join(root, filename))
                    print(f"Found file: {os.path.join(root, filename)}")

    return files
def create_dataframe(files):
    """
    Creates a dataframe from a list of files.

    Args:
        files (list): A list of files.

    Returns:
        pandas.DataFrame: A dataframe containing the data from the files.
    """
    data = []
    print(files)

    for file in files:
        df = pd.read_csv(file, index_col=None, header=0)
        data.append(df)
        # with open(file, "r") as f:
        #     data.append(f.read())

    df = pd.concat(data, axis=0, ignore_index=True,)
    return df



def search_excel_file(file_path, search_term):
  """
  Searches an Excel file for a given search term.

  Args:
    file_path (str): The path to the Excel file.
    search_term (str): The search term.

  Returns:
    pandas.DataFrame: A dataframe containing the rows that contain the search term.
  """

  # Read the Excel file into a dataframe
  df = pd.read_excel(file_path)

  # Search the dataframe for the search term
  results = df[df.isin([search_term]).any(axis=1)]

  # Return the results
  return results





def find_row_with_least_null_values(df):
    """
    Finds the row with the least number of null values in a dataframe.

    Args:
        df (pandas.DataFrame): The dataframe to search.

    Returns:
        pandas.Series: The row with the least number of null values.
    """
    
    try:
        df.replace("null","")

        # Count the number of null values in each row
        # Find the row with the least number of null values
        
        # Get the row with the least number of null values
        
        
        row_with_least_null_values = df[df.isnull().sum(axis=1) == min(df.isnull().sum(axis=1))]

    # Return the row
        return row_with_least_null_values.iloc[0]
    except:
        return None







if __name__ == "__main__":
    import pandas as pd

    # Load the Excel file into a pandas DataFrame
