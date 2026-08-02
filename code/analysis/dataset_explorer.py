import os
import pandas as pd

# ---------------------------------------------------------
# DATASET EXPLORER
# ---------------------------------------------------------

# Project Structure:
# WhatsApp-Notification-Router/
# ├── dataset/
# └── code/
#     └── analysis/
#         └── dataset_explorer.py

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "..", "dataset")

print("=" * 80)
print("DATASET EXPLORER")
print("=" * 80)

# Check whether dataset exists
if not os.path.exists(DATASET_PATH):
    print(f"Dataset folder not found: {DATASET_PATH}")
    exit()

csv_files = sorted(
    [file for file in os.listdir(DATASET_PATH) if file.endswith(".csv")]
)

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    print("=" * 80)
    print(f"FILE : {file}")
    print("=" * 80)

    file_path = os.path.join(DATASET_PATH, file)

    try:
        df = pd.read_csv(file_path)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        for column in df.columns:
            print(f" - {column}")

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 3 Records:")
        print(df.head(3))

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

    print("\n")

print("=" * 80)
print("Dataset exploration completed successfully.")
print("=" * 80)