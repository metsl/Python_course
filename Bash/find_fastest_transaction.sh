#!/bin/bash

# Path to the log file
LOG_FILE="c:\Users\AntonKheyfets\Downloads\exam.log"

# Variables to store the fastest time and transaction ID
fastest_time=999999999
fastest_transaction_id=""

# Read the log file line by line
while IFS= read -r line; do
    # Check for "transaction begun" and extract the time and transaction ID
    if [[ $line =~ transaction\ ([0-9]+)\ begun ]]; then
        transaction_id="${BASH_REMATCH[1]}"
        begin_time=$(echo $line | grep -oP '\d{2}:\d{2}:\d{2}\.\d{3}')
        begin_epoch=$(date -d "$begin_time" +%s%3N)
    fi

    # Check for "transaction done" and extract the time
    if [[ $line =~ transaction\ done ]]; then
        done_time=$(echo $line | grep -oP '\d{2}:\d{2}:\d{2}\.\d{3}')
        done_epoch=$(date -d "$done_time" +%s%3N)

        # Calculate the difference in milliseconds
        time_diff=$((done_epoch - begin_epoch))

        # Check if this is the fastest transaction
        if [ $time_diff -lt $fastest_time ]; then
            fastest_time=$time_diff
            fastest_transaction_id=$transaction_id
        fi
    fi
done < "$LOG_FILE"

# Print the fastest transaction time and ID
echo "Fastest Transaction ID: $fastest_transaction_id"
echo "Fastest Transaction Time: ${fastest_time}ms"
