class RelationshipScorer:
    """
    Computes how important a sender is to a user.
    Returns a score between 0 and 100.
    """

    @staticmethod
    def score(
        reply_rate: float,
        read_rate: float,
        mutual_groups: int,
        is_group_admin: bool,
    ):

        score = 0

        # User usually replies
        score += reply_rate * 40

        # User usually reads
        score += read_rate * 30

        # Shared groups
        score += min(mutual_groups, 5) * 5

        # Group admins get extra importance
        if is_group_admin:
            score += 10

        score = max(0, min(100, score))

        return round(score, 2)