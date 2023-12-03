import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def align_audio_with_transcript(audio_directory, transcript_directory, output_directory):
    """
    Align each audio file with its corresponding transcript file using aeneas.

    :param audio_directory: Directory containing the audio files
    :param transcript_directory: Directory containing the transcript files
    :param output_directory: Directory to save the alignment output JSON files
    """
    for audio_file in os.listdir(audio_directory):
        if audio_file.endswith(".wav"):
            # Construct the corresponding transcript file name
            transcript_file = audio_file.replace('.wav', '.txt')

            audio_file_path = os.path.join(audio_directory, audio_file)
            transcript_file_path = os.path.join(transcript_directory, transcript_file)
            output_json_path = os.path.join(output_directory, audio_file.replace('.wav', '.json'))

            if os.path.exists(transcript_file_path):
                # Construct the aeneas command
                command = [
                    "python", "-m", "aeneas.tools.execute_task",
                    audio_file_path,
                    transcript_file_path,
                    "task_language=eng|is_text_type=plain|os_task_file_format=json",
                    output_json_path
                ]

                try:
                    # Execute the command
                    logging.info(f"Starting alignment for {audio_file}")
                    subprocess.run(command, check=True)
                    logging.info(f"Alignment completed for {audio_file}")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Error during alignment for {audio_file}: {e}")
            else:
                logging.warning(f"Transcript file not found for {audio_file}")

def main():
    # Directories for audio files, transcripts, and output JSON files
    audio_directory = '../processed_data/audio'
    transcript_directory = '../data/transcripts/text_files'
    output_directory = '../processed_data/aligned_data'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Perform the alignment
    align_audio_with_transcript(audio_directory, transcript_directory, output_directory)

if __name__ == "__main__":
    main()
