import sounddevice as sd

def record_audio(duration=5):
    """
    Record audio from the microphone for the specified duration (in seconds).
    Parameters:
    - duration (int): The duration of the recording in seconds (default is 5 seconds).

    Returns:
    - audio_data (numpy.ndarray): The recorded audio data as a NumPy array.
    - sample_rate (int): The sample rate of the recorded audio.
    """
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()
    return audio_data, 44100  

def play_audio(audio_data, sample_rate):
    """
    Play audio using sounddevice.
    Parameters:
    - audio_data (numpy.ndarray): The audio data to play.
    - sample_rate (int): The sample rate of the audio data.
    """
    print("Playing audio...")
    sd.play(audio_data, sample_rate)
    sd.wait()
    print("Finished playing audio.")

#Record audio for 10 seconds 
audio_data, sample_rate = record_audio(duration=10)
#play the recorded audio
play_audio(audio_data, sample_rate)