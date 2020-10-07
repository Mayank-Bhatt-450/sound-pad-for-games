from pynput.keyboard import Key, Listener
import pyaudio,time
import threading,time,os,random
import numpy as np
def mic_stream():
    global FLAG
    print('in')
    p = pyaudio.PyAudio()
    RATE=44100
    CHUNK=1024
    CHANNELS=1
    SAMPWIDTH=2
    FORMAT= pyaudio.paInt16#p.get_format_from_width(SAMPWIDTH)
    stream_MIC = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    input_device_index = 2,
                    frames_per_buffer = CHUNK)

    pq = pyaudio.PyAudio()
    stream = pq.open(format =FORMAT ,
                    channels = CHANNELS,
                    rate = RATE,
                    output_device_index=8,#8,
                    output = True
                    )
    data = stream_MIC.read(CHUNK)
    g=0
    p_flag=0
    thrushhold=6
    while True:
        if FLAG=='ON':
            stream.write(data)
            data = stream_MIC.read(CHUNK)
        else:
            time.sleep(0.2)
    print('yolo')

tuggle_flag=0
FLAG='OFF'
def tuggle():
    global tuggle_flag,FLAG
    tuggle_flag=-(1*tuggle_flag)+1

def on_press(key):
    global tuggle_flag,FLAG
    key_event=str(key).replace("'",'')
    if tuggle_flag==0 and key_event in['t','y']:
        tuggle()
        FLAG='ON'
        print(key_event)
        
    
def on_release(key):
    global tuggle_flag,FLAG
    key_event=str(key).replace("'",'')
    if key_event in['t','y','T','Y']:
        tuggle()
        FLAG='OFF'
        print('Key {} released.'.format(key))
        
        
        
def thd():
    thread=threading.Thread(target=mic_stream)
    thread.daemon=True
    thread.start()            

thd()
with Listener(on_press=on_press,on_release = on_release) as listener:
    listener.join()












