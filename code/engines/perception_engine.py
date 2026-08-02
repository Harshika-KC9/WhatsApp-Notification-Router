class PerceptionEngine:
    """
    Understands the semantic meaning of an incoming message.
    This version starts with text analysis only.
    OCR and Voice will plug in later.
    """

    PAYMENT_WORDS = {
        "payment", "bill", "invoice", "upi", "due", "recharge",
        "emi", "transaction", "credited", "debited"
    }

    URGENT_WORDS = {
        "urgent", "immediately", "asap", "emergency",
        "today", "now", "important"
    }

    PROMOTION_WORDS = {
        "sale", "offer", "discount", "free", "cashback",
        "coupon", "deal"
    }

    GREETING_WORDS = {
        "happy birthday",
        "congratulations",
        "good morning",
        "good night",
        "hello",
        "hi"
    }

    SCAM_WORDS = {
        "otp",
        "lottery",
        "click here",
        "claim",
        "prize",
        "win money"
    }

    def analyze(self, text):

        # Handle missing values
        if text is None:
            text = ""
        elif not isinstance(text, str):
            text = str(text)

        # Pandas NaN becomes "nan"
        if text.lower() == "nan":
            text = ""

        text = text.lower()

        result = {
            "payment": False,
            "urgent": False,
            "promotion": False,
            "greeting": False,
            "scam": False
        }

        for word in self.PAYMENT_WORDS:
            if word in text:
                result["payment"] = True

        for word in self.URGENT_WORDS:
            if word in text:
                result["urgent"] = True

        for word in self.PROMOTION_WORDS:
            if word in text:
                result["promotion"] = True

        for word in self.GREETING_WORDS:
            if word in text:
                result["greeting"] = True

        for word in self.SCAM_WORDS:
            if word in text:
                result["scam"] = True

        return result