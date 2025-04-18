#!/bin/bash
ray start --address='rayhead:6379' --block --metrics-export-port=8080
