# APAE - Adaptive Personal Attention Engine

## Goal

Build an AI-powered notification routing system for WhatsApp that decides whether an incoming message should be:

- notify
- digest
- mute

using multimodal reasoning, personalization, historical behavior, trust, and explainability.

---

## System Pipeline

Incoming Message
        │
        ▼
Perception Engine
(Text / Image / Voice)
        │
        ▼
Digital Twin Engine
(User Profile Builder)
        │
        ▼
Memory Engine
(Historical Retrieval)
        │
        ▼
Trust Engine
(Sender & Business Credibility)
        │
        ▼
Attention Engine
(User Attention Budget)
        │
        ▼
Decision Orchestrator
(Final Decision)
        │
        ▼
Explanation Engine
(Reason + Confidence + Evidence)

---

## Engines

### 1. Perception Engine

Purpose:
Understand the content of the incoming message.

Inputs:
- messages.csv
- images.csv
- voice_notes.csv

Outputs:
- message category
- urgency
- entities
- extracted text

---

### 2. Digital Twin Engine

Purpose:
Build a profile representing the user's preferences and behavior.

Inputs:
- users.csv
- group_members.csv
- daily_notification_summary.csv

Outputs:
- attention budget
- quiet hours
- notification fatigue
- responsiveness

---

### 3. Memory Engine

Purpose:
Retrieve similar historical messages.

Inputs:
- message_history.csv
- message_events.csv

Outputs:
- evidence_message_ids
- engagement history
- similarity score

---

### 4. Trust Engine

Purpose:
Estimate trustworthiness of the sender.

Inputs:
- business_accounts.csv
- user_business_history.csv

Outputs:
- trust score
- business relationship
- risk indicators

---

### 5. Attention Engine

Purpose:
Estimate whether the user should be interrupted.

Inputs:
- Outputs from all previous engines

Outputs:
- attention score

---

### 6. Decision Orchestrator

Purpose:
Choose:
- notify
- digest
- mute

---

### 7. Explanation Engine

Purpose:
Generate:
- reason
- confidence
- evidence_message_ids