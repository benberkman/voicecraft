#!/bin/bash

# Directories
audio_directory="/Users/benberkman/Desktop/voicecraft_project/processed_data/audio"
transcript_directory="/Users/benberkman/Desktop/voicecraft_project/data/transcripts/text_files"
output_directory="/Users/benberkman/Desktop/voicecraft_project/processed_data/aligned_data"

# Create output directory if it doesn't exist
mkdir -p "$output_directory"

# Iterate over each audio file
for audio_file in "$audio_directory"/*.wav; do
    # Extract the base name without the extension
    base_name=$(basename "$audio_file" .wav)

    # Corresponding transcript file
    transcript_file="$transcript_directory/$base_name.txt"

    # Output JSON file
    output_json="$output_directory/$base_name.json"

    # Check if the transcript file exists
    if [[ -f "$transcript_file" ]]; then
        echo "Processing: $base_name"
        python -m aeneas.tools.execute_task \
            "$audio_file" \
            "$transcript_file" \
            "task_language=eng|is_text_type=plain|os_task_file_format=json" \
            "$output_json"
        echo "Completed: $base_name"
    else
        echo "Transcript file not found for $base_name"
    fi
done

echo "All files processed."
