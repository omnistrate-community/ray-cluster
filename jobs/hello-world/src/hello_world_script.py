import ray
import socket

@ray.remote
def hello_world():
    hostname = socket.gethostbyname(socket.gethostname())
    return f"hello world from {hostname}"

ray.init()
print(ray.get(hello_world.remote()))
