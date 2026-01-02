import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

ref = pd.read_csv("data/historical_transactions.csv")
cur = pd.read_csv("data/current_transactions.csv")

report = Report(metrics=[
    DataDriftPreset()
])

report.run(reference_data=ref, current_data=cur)
report.save_html("monitoring/drift_report.html")

# create flag for auto-retraining
open("monitoring/drift_detected.flag", "w").close()
