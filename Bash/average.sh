#!/bin/bash

# Path to the log file
LOG_FILE="c:\Users\AntonKheyfets\Downloads\exam.log"

# Variables to store total time and transaction count
total_time=0
transaction_count=0

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

        # Accumulate total time and increment the transaction count
        total_time=$((total_time + time_diff))
        transaction_count=$((transaction_count + 1))
    fi
done < "$LOG_FILE"

# Calculate the average transaction time
if [ $transaction_count -gt 0 ]; then
    average_time=$((total_time / transaction_count))
    echo "Average Transaction Time: ${average_time}ms"
else
    echo "No transactions found."
fi
