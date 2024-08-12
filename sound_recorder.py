"""
This script records audio, saves it as a WAV file, and plays it back.
"""

#import sounddevice module
import sounddevice as sd
from scipy.io.wavfile import write

# Record audio
FREQ = 44100  # Sample rate
DURATION = 5  # Recording duration in seconds
print("Recording...")
recording = sd.rec(int(DURATION * FREQ), samplerate=FREQ, channels=2)
sd.wait()  # Wait until recording is finished
print("Recording finished.")

# Save the recording as a WAV file
write("recording.wav", FREQ, recording)

# Play the recorded audio
print("Playing audio...")
sd.play(recording, FREQ)
sd.wait()  # Wait until playback is finished
print("Playback finished.")
