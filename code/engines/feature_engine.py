class FeatureEngine:
    """
    Converts raw dataset tables into meaningful
    user-level features used by all downstream engines.
    """

    def __init__(self, tables):
        self.tables = tables

    def build_user_features(self):
        """
        Returns:
            {
                user_id: {
                    feature_name: value,
                    ...
                }
            }
        """
        user_profiles = {}

        # Feature computation will be implemented step by step.

        return user_profiles