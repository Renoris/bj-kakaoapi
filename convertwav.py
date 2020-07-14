from pydub import AudioSegment

# sound = AudioSegment.from_wav("audio.wav")
# sound = sound.set_channels(1)
# sound = sound.set_frame_rate(16000)
# sound = sound.set_sample_width(2)
#
# sound.export("output.wav",format="wav")

def convertkakaousevoice(file):
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound = sound.set_sample_width(2)
    return sound.raw_data

asd=open('audio.wav','rb')
result=convertkakaousevoice(asd)
print(type(result))
print("잉")