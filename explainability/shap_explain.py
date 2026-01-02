import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("model.joblib")
data = pd.read_csv("data/historical_transactions.csv")

X = data[["amount", "merchant_risk", "transaction_hour"]]

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Global explanation
shap.summary_plot(shap_values, X, show=False)
plt.savefig("explainability/global_shap.png")
