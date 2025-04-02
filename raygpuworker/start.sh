#!/bin/bash
ray start --num-gpus='{{ $sys.compute.node.gpus }}' --address='0.0.0.0:6379' --block
