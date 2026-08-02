import pandas as pd


class DigitalTwinEngine:

    def __init__(self, tables):

        self.users = tables["users"]
        self.notification_summary = tables["daily_notification_summary"]
        self.group_members = tables["group_members"]

    def build_user_profile(self, user_id):

        user = self.users[self.users["user_id"] == user_id]

        if user.empty:
            return None

        user = user.iloc[0]

        opened = int(user["messages_opened_30d"])
        replied = int(user["messages_replied_30d"])
        dismissed = int(user["notifications_dismissed_30d"])
        reported = int(user["messages_reported_30d"])

        responsiveness = replied / max(opened, 1)
        dismissal_rate = dismissed / max(opened + dismissed, 1)
        report_rate = reported / max(opened + dismissed + reported, 1)

        history = self.notification_summary[
            self.notification_summary["user_id"] == user_id
        ]

        avg_notifications = history["notifications_sent"].mean()

        if pd.isna(avg_notifications):
            avg_notifications = 0

        attention_budget = max(0, 100 - avg_notifications * 5)

        return {
            "user_id": user_id,
            "quiet_hours": user["do_not_disturb_window"],
            "opened_30d": opened,
            "replied_30d": replied,
            "dismissed_30d": dismissed,
            "reported_30d": reported,
            "responsiveness": round(responsiveness, 2),
            "dismissal_rate": round(dismissal_rate, 2),
            "report_rate": round(report_rate, 2),
            "attention_budget": round(attention_budget, 2),
        }