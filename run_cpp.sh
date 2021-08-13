#!/bin/bash

start_time="$(date -u +%s.%N)"  # seconds.nanoseconds

# && -> the next command only runs if previous succeeded
g++ $1 -o run_temp && ./run_temp
rm run_temp

end_time="$(date -u +%s.%N)"

elapsed="$(bc <<<"$end_time-$start_time")"

echo "Total of $elapsed seconds elapsed for process $1"
