#!/bin/bash

cores=2

for seed in $(seq 1 10); do
	for flag in "true" "false"; do 
		# **Caution:**
		# Running python code simultaenously as a background processes (&).
		# Variable `cores` will control how many processed will be created at a time.
		python3 example.py -seed $seed -flag $flag &

		background=( $(jobs -p) )
		if (( ${#background[@]} >= cores )); then
			wait -n
		fi
	done
done
