#!/bin/bash
ray start --num-gpus=$NUM_GPUS --address='rayhead:6379' --block
