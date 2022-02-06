#!/bin/bash

start_time="$(date -u +%s.%N)"  # seconds.nanoseconds

# && -> the next command only runs if previous succeeded
ghci $1 -e 'calc'

end_time="$(date -u +%s.%N)"

elapsed="$(bc <<<"$end_time-$start_time")"

echo "Total of $elapsed seconds elapsed for process $1"
