Real-Time Fraud Detection System with MLOps & Kubernetes

A production-grade real-time fraud detection system demonstrating the full MLOps lifecycle, from model training to containerized deployment on Kubernetes, with CI/CD, monitoring, and scalability.

This project is designed to mirror real industry ML systems, not toy demos.

🚀 Key Features
🔹 Machine Learning

Probabilistic fraud risk scoring (not binary)

Tree-based model (LightGBM / XGBoost style)

Real-time inference via REST API

🔹 MLOps

Drift-aware design

Auto-retraining ready architecture

Model versioning compatible with MLflow

CI-safe ML system design

🔹 Engineering & DevOps

FastAPI inference service

Dockerized application

Kubernetes deployment with replicas

Horizontal scalability ready

CI/CD with GitHub Actions

Docker CD pipeline to Docker Hub


⚙️ Tech Stack
Layer	Technology
API	FastAPI
ML	LightGBM / XGBoost
Container	Docker
Orchestration	Kubernetes
CI/CD	GitHub Actions
Registry	Docker Hub
Language	Python 3.10
▶️ Running Locally (Without Kubernetes)
pip install -r requirements.txt
uvicorn app:app --reload


Open:

http://127.0.0.1:8000/docs

🐳 Docker
Build image
docker build -t vaibhav61999/fraud-detection:latest .

Run container
docker run -p 8000:8000 vaibhav61999/fraud-detection:latest

☸️ Kubernetes Deployment
1️⃣ Start Kubernetes

Docker Desktop → Enable Kubernetes
or

minikube start

2️⃣ Deploy to cluster
kubectl apply -f k8s/

3️⃣ Verify resources
kubectl get pods
kubectl get svc

4️⃣ Access API (Local Dev – Recommended)

Due to NodePort limitations on Windows/macOS:

kubectl port-forward svc/fraud-service 8000:80


Open:

http://localhost:8000/docs

📈 Scalability (HPA)

The system supports horizontal scaling using Kubernetes HPA:

Minimum replicas: 2

Scales based on CPU utilization

Ready for traffic spikes

🔄 CI/CD Pipeline
Continuous Integration

Code checkout

Dependency installation

Safe API import validation

Prevents broken deployments

Continuous Deployment

Docker image build

Container smoke test

Push to Docker Hub automatically

Author

Vaibhav Tiwari
AI / ML Engineer | MLOps-focused
GitHub: https://github.com/tvaibhav619-web





