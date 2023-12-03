import os
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def rename_audio_files(csv_file_path, audio_directory):
    """
    Rename audio files based on the dates in the CSV file to match the transcript text file naming convention.

    :param csv_file_path: Path to the CSV file containing dates and transcripts
    :param audio_directory: Directory where the audio files are stored
    """
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Original file name based on the date
        original_file_name = f"Voicemail - {row['Date'].replace(':', ' ')} - Mom.wav"
        original_file_path = os.path.join(audio_directory, original_file_name)

        # New file name using underscores
        new_file_name = f"Voicemail_{row['Date'].replace('-', '_').replace(' ', '_').replace(':', '_')}_Mom.wav"
        new_file_path = os.path.join(audio_directory, new_file_name)

        # Check if the original file exists and then rename it
        if os.path.exists(original_file_path):
            os.rename(original_file_path, new_file_path)
            logging.info(f"Renamed '{original_file_name}' to '{new_file_name}'")
        else:
            logging.warning(f"File not found: {original_file_path}")

def main():
    # Path to the CSV file
    csv_file_path = '../data/transcripts/transcripts.csv'

    # Directory containing the audio files
    audio_directory = '../processed_data/audio'

    # Rename the audio files
    rename_audio_files(csv_file_path, audio_directory)

if __name__ == "__main__":
    main()
