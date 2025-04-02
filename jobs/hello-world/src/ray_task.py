import ray
import socket
import time
import os

# Initialize Ray - connect to your existing cluster
# The RAY_ADDRESS environment variable can be passed when running the container
ray_address = os.environ.get("RAY_ADDRESS", "auto")
print(f"Connecting to Ray cluster at: {ray_address}")
ray.init(address=ray_address)

# Define a remote function (Ray task)
@ray.remote
def hello_world(i):
    # This will run on a worker in your Ray cluster
    hostname = socket.gethostbyname(socket.gethostname())
    time.sleep(1)  # Simulate some work
    return f"Hello from task {i} running on {hostname}"

# Submit 1 task to the cluster using the replica index
print("Submitting task to the cluster...")
results = []
results.append(hello_world.remote({{ $sys.compute.node.index }}))

# Wait for and retrieve all results
print("Waiting for results...")
outputs = ray.get(results)

# Print the results
for output in outputs:
    print(output)

# Get cluster info
print(f"\nThis cluster consists of {len(ray.nodes())} nodes in total")
print(f"CPU resources in total: {ray.cluster_resources()['CPU']}")
