import re
import os
from datetime import datetime

# Initialize variables
fastest_time = float('inf')
fastest_id = None

# Open the log file and process it line by line
# os.chdir(r"c:\Users\AntonKheyfets\Downloads")
# myfile="exam.log"
with open(r"c:\Users\AntonKheyfets\Downloads\exam.log", 'r') as log_file:
    start_time = None
    transaction_id = None

    for line in log_file:
        # Check for transaction begun
        begun_match = re.search(r"(\d{2}:\d{2}:\d{2}\.\d{3}).*transaction (\d+) begun", line)
        if begun_match:
            transaction_id = begun_match.group(1)
            start_time = datetime.strptime(begun_match.group(2).strip(), "%Y-%m-%d %H:%M:%S.%f")

        # Check for transaction done
        done_match = re.search(r"(\d{2}:\d{2}:\d{2}\.\d{3}).*(transaction done)", line)
        if done_match and start_time:
            end_time = datetime.strptime(done_match.group(1).strip(), "%Y-%m-%d %H:%M:%S.%f")
            duration = (end_time - start_time).total_seconds()

            # Check if this is the fastest transaction
            if duration < fastest_time:
                fastest_time = duration
                fastest_id = transaction_id

# Output the fastest transaction ID and duration
fastest_id, fastest_time
print(fastest_id)