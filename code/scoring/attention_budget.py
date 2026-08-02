class AttentionBudgetScorer:
    """
    Computes how much attention the user has left
    based on recent notification load.
    """

    @staticmethod
    def compute(notifications_sent, notifications_dismissed):

        if notifications_sent <= 0:
            return 100.0

        dismissal_rate = notifications_dismissed / notifications_sent

        score = (
            100
            - (notifications_sent * 5)
            - (dismissal_rate * 30)
        )

        score = max(0, min(100, score))

        return round(score, 2)