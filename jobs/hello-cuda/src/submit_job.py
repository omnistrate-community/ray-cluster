from ray.job_submission import JobSubmissionClient
import time
from ray.job_submission import JobStatus
import os

# Connect to your Ray cluster
ray_address = os.environ.get("RAY_ADDRESS", "auto")
print(f"Connecting to Ray cluster at: {ray_address}")
client = JobSubmissionClient(address=ray_address)

# Submit the job
job_id = client.submit_job(
    # Specify the command to run your script
    entrypoint="python cuda_workload.py",
    
    # Specify the runtime environment with required packages
    runtime_env={
        "working_dir": "./",
        "pip": ["torch", "numpy"]
    },
    
    # Request GPU resources
    entrypoint_num_cpus=1,
    entrypoint_num_gpus=1
)

print(f"Submitted CUDA job with ID: {job_id}")

# Poll for job status
def wait_until_status(job_id, status_to_wait_for, timeout_seconds=300):
    start = time.time()
    while time.time() - start <= timeout_seconds:
        status = client.get_job_status(job_id)
        print(f"Status: {status}")
        if status in status_to_wait_for:
            break
        time.sleep(5)

# Wait for job to complete
wait_until_status(job_id, {JobStatus.SUCCEEDED, JobStatus.STOPPED, JobStatus.FAILED})

# Get and print job logs
logs = client.get_job_logs(job_id)
print("\nJob logs:")
print(logs)
