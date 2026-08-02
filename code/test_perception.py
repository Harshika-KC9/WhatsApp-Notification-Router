from engines.perception_engine import PerceptionEngine

engine = PerceptionEngine()

samples = [
    "Your electricity bill is due tomorrow.",
    "Huge SALE! 70% OFF today only.",
    "Happy Birthday Harshika!",
    "Claim your lottery prize now!",
    "Meeting postponed to tomorrow."
]

for msg in samples:
    print("=" * 50)
    print(msg)
    print(engine.analyze(msg))