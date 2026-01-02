import requests, os

SLACK = os.getenv("SLACK_WEBHOOK_URL")
PD_KEY = os.getenv("PAGERDUTY_API_KEY")

def alert_slack(msg):
    requests.post(SLACK, json={"text": msg})

def alert_pagerduty(msg):
    requests.post(
        "https://events.pagerduty.com/v2/enqueue",
        json={
            "routing_key": PD_KEY,
            "event_action": "trigger",
            "payload": {
                "summary": msg,
                "severity": "critical",
                "source": "fraud-mlops"
            }
        }
    )

def send_alert(msg):
    alert_slack(msg)
    alert_pagerduty(msg)
