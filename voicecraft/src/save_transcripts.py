import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def save_transcripts_as_text_files(transcripts_df, output_directory):
    """
    Save each transcript in the DataFrame as a separate text file.

    :param transcripts_df: DataFrame containing the transcripts
    :param output_directory: Directory to save the text files
    """
    for index, row in transcripts_df.iterrows():
        # Construct the file name from the date, replacing spaces and dashes with underscores
        file_name = f"Voicemail_{row['Date'].replace('-', '_').replace(' ', '_').replace(':', '_')}_Mom.txt"
        file_path = os.path.join(output_directory, file_name)

        # Write the transcript to a text file
        with open(file_path, 'w') as file:
            file.write(row['Transcript'])
        logging.info(f"Saved transcript to {file_path}")

def main():
    # Load the transcript CSV file
    transcript_file_path = '../data/transcripts/transcripts.csv'
    transcripts_df = pd.read_csv(transcript_file_path)

    # Directory to save the transcript text files
    transcript_text_directory = '../data/transcripts/text_files'

    # Create the directory if it doesn't exist
    if not os.path.exists(transcript_text_directory):
        os.makedirs(transcript_text_directory)

    # Save transcripts as text files
    save_transcripts_as_text_files(transcripts_df, transcript_text_directory)

    # Additional code for other processing can go here
    # ...

if __name__ == "__main__":
    main()
