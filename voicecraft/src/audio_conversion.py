from pydub import AudioSegment
import os

def convert_amr_to_wav(amr_path, wav_path):
    """
    Convert an AMR file to WAV format.

    :param amr_path: Path to the AMR file
    :param wav_path: Path to save the WAV file
    """
    try:
        # Load AMR file
        amr_audio = AudioSegment.from_file(amr_path, format="amr")

        # Export as WAV
        amr_audio.export(wav_path, format="wav")
        print(f"Converted {amr_path} to {wav_path}")

    except Exception as e:
        print(f"Error converting {amr_path}: {e}")

def main():
    input_directory = "../data/audio/original"
    output_directory = "../processed_data/audio"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Convert each AMR file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".amr"):
            amr_path = os.path.join(input_directory, filename)
            wav_filename = filename.replace(".amr", ".wav")
            wav_path = os.path.join(output_directory, wav_filename)
            convert_amr_to_wav(amr_path, wav_path)

if __name__ == "__main__":
    main()
