# src/app.py
import os
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# ===============================
# CI FLAG (CRITICAL)
# ===============================
IS_CI = os.getenv("CI", "false").lower() == "true"

# ===============================
# OPTIONAL EXTERNAL SERVICES
# ===============================
redis_client = None
if not IS_CI:
    try:
        import redis
        redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    except Exception as e:
        print("Redis not available:", e)

# ===============================
# LOAD MODEL (LOCAL ONLY)
# ===============================
MODEL_PATH = "models/fraud_model.pkl"
model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

# ===============================
# FASTAPI APP
# ===============================
app = FastAPI(title="Real-Time Fraud Detection API")

# ===============================
# REQUEST SCHEMA
# ===============================
class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    merchant_risk: float
    transaction_hour: int

# ===============================
# HEALTH CHECK (CI NEEDS THIS)
# ===============================
@app.get("/")
def health():
    return {"status": "ok", "ci": IS_CI}

# ===============================
# PREDICTION ENDPOINT
# ===============================
@app.post("/predict")
def predict(txn: Transaction):
    if model is None:
        return {"error": "Model not loaded"}

    features = np.array([[txn.amount, txn.merchant_risk, txn.transaction_hour]])
    risk_score = float(model.predict_proba(features)[0][1])

    return {
        "transaction_id": txn.transaction_id,
        "fraud_risk_score": round(risk_score, 4)
    }

