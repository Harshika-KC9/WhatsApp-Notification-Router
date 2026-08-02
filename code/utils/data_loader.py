import os
import pandas as pd


class DataLoader:
    """
    Loads all dataset CSV files once.
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        self.dataset_path = os.path.join(
            base_dir,
            "..",
            "..",
            "dataset"
        )

        self.tables = {}

    def load(self):

        csv_files = [
            file
            for file in os.listdir(self.dataset_path)
            if file.endswith(".csv")
        ]

        for file in csv_files:

            path = os.path.join(self.dataset_path, file)

            # Remove extension and trailing spaces
            table_name = os.path.splitext(file)[0].strip()

            df = pd.read_csv(path)

            # Clean column names
            df.columns = df.columns.str.strip()

            # Fill missing values ONLY for object/string columns
            object_cols = df.select_dtypes(include=["object"]).columns
            df[object_cols] = df[object_cols].fillna("")

            self.tables[table_name] = df

        return self.tables

    def get(self, table_name):
        return self.tables.get(table_name)