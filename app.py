import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

mlflow.set_tracking_uri("http://localhost:5000")

MODEL_NAME = "FraudDetectionModel"
MODEL_STAGE = "Production"

model = mlflow.pyfunc.load_model(
    f"models:/{MODEL_NAME}/{MODEL_STAGE}"
)

class Transaction(BaseModel):
    user_id: int
    amount: float
    merchant_risk: float
    transaction_hour: int

@app.post("/predict")
def predict(tx: Transaction):
    df = pd.DataFrame([tx.dict()])
    risk_score = model.predict(df)[0]

    return {
        "fraud_risk_score": float(risk_score),
        "decision": "BLOCK" if risk_score > 0.8 else "ALLOW"
    }
