#!/bin/bash

# && -> the next command only runs if previous succeeded
g++ $1 -o run_temp && ./run_temp && rm run_temp