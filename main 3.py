import sounddevice
from scipy.io.wavfile import write
from pydub import AudioSegment

def rcor(ti):
    i = 0
    while True:
        rece = sounddevice.rec((i*44100), samplerate=44100, channels=2)
        i += 1

        if i >= ti:
            sounddevice.wait(1)
            write("demo.wav", 44100, rece)
            return "end"

while True:
    try:
        a = int(input("enter number only: "))
        c = rcor(a)
        break
    
    except Exception as e:
        print("please enter valid value.")
        continue