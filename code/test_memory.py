from utils.data_loader import DataLoader
from engines.memory_engine import MemoryEngine

loader = DataLoader()
tables = loader.load()

engine = MemoryEngine(tables)

user = tables["users"].iloc[0]["user_id"]

history = engine.get_user_history(user)

print("=" * 60)
print("History Count:", len(history))

similar = engine.retrieve_similar(
    user,
    "electricity bill due tomorrow"
)

print("Similar Messages:", len(similar))

for msg in similar[:5]:
    print(msg["message_id"], "-", msg["message_text"])