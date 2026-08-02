from utils.data_loader import DataLoader

loader = DataLoader()

tables = loader.load()

print("Loaded tables:")

for name in tables:
    print(name)