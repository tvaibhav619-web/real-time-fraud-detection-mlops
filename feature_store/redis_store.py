import redis, json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def write_features(user_id, features):
    redis_client.set(user_id, json.dumps(features))

def read_features(user_id):
    data = redis_client.get(user_id)
    return json.loads(data) if data else None
