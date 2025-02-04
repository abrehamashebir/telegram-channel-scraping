import json
import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from .logger_utils import Logger
class DataProcessor:
    """
    A class for loading, cleaning, and preprocessing JSON data into a Pandas DataFrame.
    """
    import logging

    logging.basicConfig(level=logging.INFO)

    def __init__(self, file_path):
        """
        Initialize the processor with a file path.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path
        self.df = None  # DataFrame will be stored here after loading
        # self.logger = Logger(name="DataProcessor").get_logger() 

    def load_json(self):
        """
        Loads a JSON file and converts it into a Pandas DataFrame.

        Returns:
            pd.DataFrame: Loaded DataFrame.
        """
        try:
            # self.logger.info(" Reading .json files")
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)  # Load JSON properly
            
            self.df = pd.DataFrame(data)
            print("JSON data loaded successfully.")
            return self.df
        except FileNotFoundError:
            print(f" Error: The file '{self.file_path}' was not found.")
            return None
        except json.JSONDecodeError:
            print(f" Error: Failed to decode JSON from '{self.file_path}'.")
            return None
        except Exception as e:
            print(f" Unexpected error: {e}")
            return None

    def clean_data(self):
        """
        Cleans the DataFrame by handling missing values and duplicates.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
        if self.df is None:
            print(" No data loaded. Run `load_json()` first.")
            return None

        # Remove duplicates
        duplicates = self.df.duplicated().sum()
        self.df = self.df.drop_duplicates()
        print(f" Removed {duplicates} duplicate records.")

        # Handle missing values
        missing_values = self.df.isnull().sum().sum()
        self.df = self.df.dropna()
        print(f" Removed {missing_values} rows with missing values.")

        print(" Data cleaning completed.")
        return self.df

    def preprocess_data(self):
        """
        Performs preprocessing like data type conversion and feature engineering.

        Returns:
            pd.DataFrame: Preprocessed DataFrame.
        """
        if self.df is None:
            self.logger.info(" No data loaded. Run `load_json()` first.")
            return None

        # Convert text columns to lowercase (example preprocessing)
        for col in self.df.select_dtypes(include=["object"]).columns:
            self.df[col] = self.df[col].str.lower()

        # Add feature engineering steps if needed
        print("Data preprocessing completed.")
        return self.df

    def get_data(self):
        """
        Returns the processed DataFrame.

        Returns:
            pd.DataFrame: Processed DataFrame.
        """
        if self.df is None:
            print(" No data available. Load and process the data first.")
            return None
        return self.df
