import ray
import torch
import socket
import time

@ray.remote(num_gpus=0.1)  # Request 1 GPU for this task
def cuda_task(matrix_size=5000):
    # Get device information
    hostname = socket.gethostbyname(socket.gethostname())
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    device_info = f"Device: {device}, CUDA available: {torch.cuda.is_available()}"
    
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        device_info += f", GPU: {device_name}"
    else:
        device_info += ", No GPU available, falling back to CPU"
    
    # Create random matrices on the appropriate device
    start_time = time.time()
    
    # Create two random matrices
    matrix_a = torch.rand(matrix_size, matrix_size, device=device)
    matrix_b = torch.rand(matrix_size, matrix_size, device=device)
    
    # Perform matrix multiplication
    torch.cuda.synchronize() if device.type == "cuda" else None
    mult_start = time.time()
    result = torch.matmul(matrix_a, matrix_b)
    torch.cuda.synchronize() if device.type == "cuda" else None
    
    # Calculate elapsed time
    mult_time = time.time() - mult_start
    total_time = time.time() - start_time
    
    # Get result statistics
    result_sum = result.sum().item()
    
    return {
        "hostname": hostname,
        "device_info": device_info,
        "matrix_size": matrix_size,
        "multiplication_time": mult_time,
        "total_time": total_time,
        "result_sum": result_sum
    }

# Initialize Ray
ray.init()

# Run the CUDA task
result = ray.get(cuda_task.remote())

# Print the results
print("\n=== CUDA Task Results ===")
print(f"Hostname: {result['hostname']}")
print(f"{result['device_info']}")
print(f"Matrix size: {result['matrix_size']}x{result['matrix_size']}")
print(f"Matrix multiplication time: {result['multiplication_time']:.4f} seconds")
print(f"Total execution time: {result['total_time']:.4f} seconds")
print(f"Result checksum: {result['result_sum']:.4f}")
print("=========================\n")
