from os import path
from pydub import AudioSegment
import os
# files
'''
src = "Badfella Video _ PBX 1 _ Sidhu Moose Wala _ Harj Nagra _ Latest Punjabi Songs 2018.mp3"
dst = "test.wav"

from pydub import AudioSegment
sound = AudioSegment.from_mp3(src)
sound.export("file.wav", format="wav")'''
st=os.listdir('.')
playlist=[]
for i in st:
    if '.mp3'in i:
        #print ( i,'\n\n\n\n')
        playlist.append(i)
print(playlist)
for i in playlist:
    print(i)
    sound = AudioSegment.from_mp3(i)
    sound.export(i[:len(i)-4]+".wav", format="wav")
