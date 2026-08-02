from utils.data_loader import DataLoader

loader = DataLoader()
tables = loader.load()

print("Keys with repr():")
for key in tables.keys():
    print(repr(key))