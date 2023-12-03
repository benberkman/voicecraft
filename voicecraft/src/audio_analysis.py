import librosa
import librosa.display
import matplotlib.pyplot as plt

def analyze_audio(file_path):
    # Load the audio file
    audio, sample_rate = librosa.load(file_path, sr=None)

    # Display the waveform
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(audio, sr=sample_rate)
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

    # Display the spectrogram
    X = librosa.stft(audio)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.title('Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

# Replace with the path to one of your .wav files
analyze_audio('../processed_data/audio/Voicemail - 2016-10-10 20 45 02 - Mom.wav')
