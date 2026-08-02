from dataclasses import dataclass


@dataclass
class DigitalTwin:
    """
    Represents a personalized profile of a user.
    This object is created once per user and reused
    while routing all incoming messages.
    """

    user_id: str

    # Notification Preferences
    quiet_hours_start: str
    quiet_hours_end: str

    # User Behaviour
    opens_last_30d: int
    replies_last_30d: int
    dismissals_last_30d: int
    reports_last_30d: int

    # Derived scores (computed later)
    attention_budget: float = 0.0
    responsiveness_score: float = 0.0
    trust_bias: float = 0.0
    notification_fatigue: float = 0.0

    def summary(self):
        return {
            "User": self.user_id,
            "Attention Budget": self.attention_budget,
            "Responsiveness": self.responsiveness_score,
            "Trust Bias": self.trust_bias,
            "Fatigue": self.notification_fatigue,
        }