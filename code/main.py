import os
import pandas as pd

from utils.data_loader import DataLoader
from engines.perception_engine import PerceptionEngine


class NotificationRouter:

    def __init__(self):

        self.loader = DataLoader()
        self.tables = self.loader.load()

        self.messages = self.tables["messages"]

        self.perception = PerceptionEngine()

    def classify(self, row):

        # Handle missing text safely
        text = row.get("message_text", "")

        if pd.isna(text):
            text = ""

        result = self.perception.analyze(text)

        # -------------------------
        # Determine message type
        # -------------------------

        if result["scam"]:
            message_type = "scam"

        elif result["payment"]:
            message_type = "payment"

        elif result["promotion"]:
            message_type = "promotion"

        elif result["greeting"]:
            message_type = "greeting"

        elif result["urgent"]:
            message_type = "urgent"

        else:
            message_type = "unknown"

        # -------------------------
        # Determine action
        # -------------------------

        if result["scam"]:
            action = "mute"

        elif result["payment"] or result["urgent"]:
            action = "notify"

        elif result["promotion"]:
            action = "digest"

        else:
            action = "digest"

        # -------------------------
        # Reason
        # -------------------------

        if action == "notify":
            reason = "Potentially important message"

        elif action == "digest":
            reason = "Useful but not immediately important"

        else:
            reason = "Likely spam or risky"

        confidence = 0.75

        evidence = "none"

        return {
            "message_id": row["message_id"],
            "action": action,
            "message_type": message_type,
            "reason": reason,
            "confidence": confidence,
            "evidence_message_ids": evidence
        }

    def run(self):

        predictions = []

        print(f"Processing {len(self.messages)} messages...\n")

        for _, row in self.messages.iterrows():

            prediction = self.classify(row)

            predictions.append(prediction)

        output_df = pd.DataFrame(predictions)

        os.makedirs("output", exist_ok=True)

        output_path = os.path.join("output", "output.csv")

        output_df.to_csv(output_path, index=False)

        print("=" * 60)
        print("Prediction completed successfully.")
        print(f"Output saved to: {output_path}")
        print("=" * 60)


if __name__ == "__main__":

    router = NotificationRouter()

    router.run()