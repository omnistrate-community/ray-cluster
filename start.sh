#!/bin/bash
ray start --num-gpus=$NUM_GPUS --address='rayhead:6379' --block --metrics-export-port=8080
