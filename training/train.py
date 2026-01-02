import mlflow
import mlflow.sklearn
import pandas as pd

from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from mlflow.tracking import MlflowClient

# -----------------------------
# MLflow configuration
# -----------------------------
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("fraud_detection")

MODEL_NAME = "FraudDetectionModel"
TARGET_COL = "fraud_probability"

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("data/historical_transactions.csv")

X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

# -----------------------------
# Train / test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train + log model
# -----------------------------
with mlflow.start_run():

    model = LGBMRegressor(
        n_estimators=300,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # Metrics (compatible with older sklearn)
    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, preds)

    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2_score", r2)

    # Register model
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name=MODEL_NAME
    )

    print("✅ Model trained & registered")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    # -----------------------------
    # AUTO-PROMOTION LOGIC
    # -----------------------------
    client = MlflowClient()

    try:
        prod_versions = client.get_latest_versions(
            MODEL_NAME, stages=["Production"]
        )
        prod_version = prod_versions[0]
        prod_run = client.get_run(prod_version.run_id)
        prod_rmse = float(prod_run.data.metrics["rmse"])
    except Exception:
        prod_rmse = float("inf")  # No production model yet

    print(f"Current Production RMSE: {prod_rmse}")
    print(f"New Model RMSE: {rmse}")

    if rmse < prod_rmse:
        print("🚀 New model is better → Promoting to Production")

        latest_version = client.get_latest_versions(MODEL_NAME)[-1].version

        client.transition_model_version_stage(
            name=MODEL_NAME,
            version=latest_version,
            stage="Production",
            archive_existing_versions=True
        )
    else:
        print("ℹ New model is NOT better → Keeping existing Production model")
