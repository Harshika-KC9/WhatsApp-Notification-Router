import pandas as pd


class MemoryEngine:

    def __init__(self, tables):

        self.history = tables["message_history"]
        self.events = tables["message_events"]

    def get_user_history(self, user_id):

        history = self.history[
            self.history["user_id"] == user_id
        ]

        return history

    def get_message_events(self, message_id):

        event = self.events[
            self.events["message_id"] == message_id
        ]

        if event.empty:
            return None

        return event.iloc[0]

    def retrieve_similar(self, user_id, text):

        history = self.get_user_history(user_id)

        if history.empty:
            return []

        text = str(text).lower()

        similar = []

        words = set(text.split())

        for _, row in history.iterrows():

            old_text = str(row["message_text"]).lower()

            overlap = words.intersection(
                set(old_text.split())
            )

            if len(overlap) >= 2:

                similar.append(row)

        return similar