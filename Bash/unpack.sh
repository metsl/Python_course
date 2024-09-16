#!/bin/bash

# Initialize counters
decompressed_count=0
not_decompressed_count=0

# Function to unpack a file based on its type
unpack_file() {
    local file="$1"
    local filetype=$(file -b --mime-type "$file")

    case "$filetype" in
        application/gzip)
            gunzip -f "$file"
            ;;
        application/x-bzip2)
            bunzip2 -f "$file"
            ;;
        application/zip)
            unzip -o "$file"
            ;;
        application/x-compress)
            uncompress -f "$file"
            ;;
        *)
            ((not_decompressed_count++))
            [ "$verbose" = true ] && echo "Warning: File '$file' was not decompressed. Unsupported type: $filetype"
            return 1
            ;;
    esac

    ((decompressed_count++))
    [ "$verbose" = true ] && echo "Decompressed: $file"
    return 0
}

# Function to process files or directories
process_file() {
    local path="$1"

    if [ -d "$path" ]; then
        # If it's a directory and -r is set, traverse it recursively
        if [ "$recursive" = true ]; then
            find "$path" -type f | while read -r file; do
                unpack_file "$file"
            done
        else
            [ "$verbose" = true ] && echo "Skipping directory '$path'. Use -r to recurse."
        fi
    else
        unpack_file "$path"
    fi
}

# Parse options
recursive=false
verbose=false

while getopts "rv" opt; do
    case "$opt" in
        r) recursive=true ;;
        v) verbose=true ;;
        *) echo "Usage: unpack.sh [-r] [-v] file [file...]"; exit 1 ;;
    esac
done
shift $((OPTIND-1))

# Process each file or directory passed as an argument
if [ $# -eq 0 ]; then
    echo "Usage: unpack.sh [-r] [-v] file [file...]"
    exit 1
fi

for target in "$@"; do
    process_file "$target"
done

# Output the number of decompressed and not decompressed files
echo "Number of archives decompressed: $decompressed_count"
echo "Number of files not decompressed: $not_decompressed_count"

# Return the number of files not decompressed as the script's exit status
exit $not_decompressed_count
