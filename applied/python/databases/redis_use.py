import time
import redis

r = redis.Redis(
    host="localhost",
    port = 6379,
    decode_responses=True
)

r.set("foo", "bar")
r.expire("foo", 5)
output = r.get("foo")
print(output)

r.hset("user_session:123", mapping={
    "name": "John",
    "last_name": "Baptist",
    "age": 12
})

output = r.hgetall("user_session:123")
print(output)

output = r.hget("user_session:123", "age")
print(output)

r.close()