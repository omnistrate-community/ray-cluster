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
    entrypoint="python hello_world_script.py",
    
    # Specify the directory containing your script
    runtime_env={"working_dir": "./"},
    
    # Optional: Specify resource requirements
    entrypoint_num_cpus=1
)

print(f"Submitted job with ID: {job_id}")

# Poll for job status
def wait_until_status(job_id, status_to_wait_for, timeout_seconds=30):
    start = time.time()
    while time.time() - start <= timeout_seconds:
        status = client.get_job_status(job_id)
        print(f"Status: {status}")
        if status in status_to_wait_for:
            break
        time.sleep(1)

# Wait for job to complete
wait_until_status(job_id, {JobStatus.SUCCEEDED, JobStatus.STOPPED, JobStatus.FAILED})

# Get and print job logs
logs = client.get_job_logs(job_id)
print("\nJob logs:")
print(logs)
