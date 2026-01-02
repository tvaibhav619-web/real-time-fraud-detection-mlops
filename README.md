🛡️ Real-Time Fraud Detection System (MLOps)

A production-grade real-time fraud detection system built using modern MLOps best practices, featuring online inference, drift detection, auto-retraining, monitoring, alerting, and model governance.

🚀 Key Features

Real-time fraud risk scoring (continuous probability, not binary)

FastAPI inference service

LightGBM / XGBoost model

Online feature ingestion

Data drift detection (Evidently)

Automatic model retraining

MLflow model registry

Prometheus metrics

Grafana dashboards

Alerting-ready architecture (Slack / PagerDuty compatible)

Dockerized monitoring stack

⚙️ Tech Stack
Component	Tool
API	FastAPI
ML Model	LightGBM / XGBoost
Experiment Tracking	MLflow
Drift Detection	Evidently
Metrics	Prometheus
Visualization	Grafana
Containerization	Docker
Language	Python 3.10
▶️ How to Run the Project
1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train & register model
python training/train.py

4️⃣ Start FastAPI service
uvicorn src.app:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

📡 Monitoring Stack
Start Prometheus
docker run -d --name prometheus \
  -p 9090:9090 \
  -v ${PWD}/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus

Start Grafana
docker run -d --name grafana -p 3000:3000 grafana/grafana


Prometheus: http://localhost:9090

Grafana: http://localhost:3000

(default login: admin / admin)

🔔 Alerting (Production-Ready)

Prometheus alert rules can trigger:

API downtime alerts

High fraud-risk spikes

Drift detection alerts

Latency threshold breaches

Alertmanager can forward alerts to:

Slack

PagerDuty

Email

📊 Example Metrics Exposed

fraud_requests_total

fraud_risk_score

model_inference_latency_seconds

api_errors_total

🧠 Why This Project Is Impressive

✔ End-to-end MLOps
✔ Real-time inference
✔ Monitoring + retraining loop
✔ Model governance via MLflow
✔ Recruiter-ready architecture

🧪 Interview Talking Points

Why risk scoring over binary classification

How drift detection triggers retraining

Why MLflow registry is critical

Difference between offline vs online monitoring

How Prometheus & Grafana fit into MLOps

📌 Future Improvements

Kafka streaming ingestion

Redis online feature store

Canary model deployment

CI/CD with GitHub Actions

Kubernetes deployment

👤 Author

Vaibhav Tiwari
AI / ML Engineer — MLOps focused
GitHub: https://github.com/tvaibhav619-web

