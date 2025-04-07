## Omnistrate Job Controller Framework w/ Ray Clusters

This repository contains a job controller framework for managing Ray clusters using the Omnistrate platform and standardizing job management on the Ray cluster. The framework is designed to simplify the process of deploying, scaling, monitoring Ray clusters in a cloud environment and also providing an easy to use interface to package and run jobs on the Ray cluster.

## Features
- `spec-cluster.yaml`: A specification file to define the Ray cluster configuration including support for GPU-based workers.
- `spec-jobs-mt.yaml`: A specification file to define the job configuration including a hello-world job that uses the CUDA library to run a simple CUDA kernel.

## Prerequisites
- Omnistrate CLI installed and configured. See [Omnistrate CLI Installation](https://docs.omnistrate.com/getting-started/compose/getting-started-with-ctl/?h=ctl#getting-started-with-omnistrate-ctl) for instructions.

## Setup

1. Create the Ray cluster service template using the `spec-cluster.yaml` file. This file contains the configuration for the Ray cluster including the number of nodes, instance types, and other parameters.

```bash
omctl build-from-repo -f spec-cluster.yaml --service-name Ray
```

This command also packages the Ray cluster image for the head node and worker nodes and uploads it to your Github Container Registry as part of the service build process.

https://github.com/user-attachments/assets/27f73f01-c8e7-4c53-8fb2-6ae6b0f5847e

2. Create a deployment of the Ray cluster in a specific cloud environment. We will use AWS and the BYOA (Bring Your Own Account) mode to demonstrate the ease of deploying and managing the Ray cluster in your customer's account.

https://github.com/user-attachments/assets/f85f444e-6ae5-4e90-8108-92b6799eebd1

3. Create the Ray job service template using the `spec-jobs-mt.yaml` file. This file contains the configuration for the job including the job name, job type, and other parameters.

```bash
omctl build-from-repo -f spec-jobs-mt.yaml --service-name Ray
```

4. We will create an instance of the hello-world job and re-use the previously created Ray cluster to run the job.


https://github.com/user-attachments/assets/aa4e683f-95bb-44dc-9075-f00017bd7472


