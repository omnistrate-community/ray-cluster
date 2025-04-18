#!/bin/bash
ray start --head --dashboard-host 0.0.0.0 --block --metrics-export-port=8080
