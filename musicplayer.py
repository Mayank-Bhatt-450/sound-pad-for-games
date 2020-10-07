from pynput.keyboard import Key, Listener
from pygame import mixer
import wave
import pyaudio
import threading,time,os,random
import music
from pynput.keyboard import Controller
#print(ls,k)
k=['1']
mixer.init()
ACTION=''
pause=False
playlist=[]
vol=.5
s=os.listdir('.')
action_flag='stop'

        
for i in s:
    if '.wav'in i:
        #print ( i,'\n\n\n\n')
        playlist.append(i)
random.shuffle(playlist)
st=os.listdir('./SOUNdBOX')
playlist_soundbox=[]
for i in st:
    if '.wav'in i:
        #print ( i,'\n\n\n\n')
        playlist_soundbox.append(i)
print(playlist_soundbox)
keyboard = Controller()
mixer_s=music.mixer()
mixer_s.start()
mixer_o=music.mixer(8)
mixer_o.start()
action_mixer=music.mixer(8)
action_mixer.start()
def checker():
    s=''
    global ACTION ,playlist,pause,vol,action_flag
    k=0
    mixer_s.load(playlist[k])
    mixer_o.load(playlist[k])
    
    
    mixer_s.set_volume(vol)
    mixer_o.set_volume(vol)
    print(k,':::',playlist[k],'\n')
    play_next=0
    while True:

            
        if mixer_s.isbusy()==False:
            if play_next!=1:
                k+=1
            else:
                play_next=0
                
            
            if k==len(playlist):
                k=0
            mixer_s.load(playlist[k])
            mixer_o.load(playlist[k])
            mixer_s.set_volume(vol)
            mixer_o.set_volume(vol)
            s+=str(k)+':::'+playlist[k]+'\n'
            print(s)

            
            
        if 'song'in  ACTION :
            ACTION=int(ACTION.split('_')[1])
            if ACTION==9:
                mi='./SOUNdBOX/'+playlist_soundbox[1]
                mixer_s.load(mi)
                mixer_o.load(mi)
                mixer_s.set_volume(vol)
                mixer_o.set_volume(vol)
                
                play_next=1
                print(playlist_soundbox[1]+'\n')
            if ACTION==8:
                mi='./SOUNdBOX/'+playlist_soundbox[3]
                mixer_s.load(mi)
                mixer_o.load(mi)
                mixer_s.set_volume(vol)
                mixer_o.set_volume(vol)
                
                play_next=1
                print(playlist_soundbox[3]+'\n')
            if ACTION==6:
                mi='./SOUNdBOX/'+playlist_soundbox[2]
                mixer_s.load(mi)
                mixer_o.load(mi)
                mixer_s.set_volume(vol)
                mixer_o.set_volume(vol)
                
                play_next=1
                print(playlist_soundbox[2]+'\n')
            if ACTION==5:
                mi='./SOUNdBOX/'+playlist_soundbox[0]
                mixer_s.load(mi)
                mixer_o.load(mi)
                mixer_s.set_volume(vol)
                mixer_o.set_volume(vol)
                
                play_next=1
                print(playlist_soundbox[0]+'\n')
                
            
        if ACTION=='pause/paly':
            #print('checker_inn')
            pause=(not pause)
            if pause:
                print('paused')
                mixer_o.pause()
                mixer_s.pause()
            else:
                print('uNpaused')
                mixer_o.unpause()
                mixer_s.unpause()
        if ACTION=='volume_up':
            mixer_s.set_volume(mixer_s.get_volume()+.1)
            mixer_o.set_volume(mixer_o.get_volume()+.1)
            vol=mixer_o.get_volume()
        if ACTION=='Volume_down':
            if mixer_o.get_volume()==0.078125:
                mixer_o.set_volume(0)
                mixer_s.set_volume(0)
            else:
                mixer_s.set_volume(mixer_s.get_volume()-.1)
                mixer_o.set_volume(mixer_o.get_volume()-.1)
            vol=mixer_o.get_volume()
            #print(mixer_o.get_volume())
        if ACTION=='next':
            if play_next!=1:
                k+=1
            else:
                play_next=0
                
            if k==len(playlist):
                k=0
            mixer_s.load(playlist[k])
            mixer_o.load(playlist[k])
            
            mixer_s.set_volume(vol)
            mixer_o.set_volume(vol)
            #print(k,':::',playlist[k],'\n')
            os.system('cls')
            s+=str(k)+':::'+playlist[k]+'\n'
            print(s)
        if ACTION=='previous':
            if play_next!=1:
                k-=1
            else:
                play_next=0
            
            if k==-1:
                k=len(playlist)-1
            mixer_s.load(playlist[k])
            mixer_o.load(playlist[k])
            mixer_s.set_volume(vol)
            mixer_o.set_volume(vol)
            #print(k,':::',playlist[k],'\n')
            os.system('cls')
            s+=str(k)+':::'+playlist[k]+'\n'
            print(s)
        if ACTION=='ACTION':
            mixer_o.pause()
            mixer_s.pause()
            pause=True
            keyboard.press('t')

            action_mixer.load("[FREE] Japanese Type Beat - 'OROCHI'-nj33MArNjC8.wav")#"Pitbull ft. Enrique Iglesias - Messin' Around (Official Video)-6X3SAs-5GUE.wav")
        else:
            if ACTION!='':
                keyboard.release('t')
                action_mixer.pause()
        ACTION=''
        time.sleep(1)
        if ACTION=='clr':
            s=''
            os.system('cls')
    
def thd():
    thread=threading.Thread(target=checker)
    thread.daemon=True
    thread.start()




def on_press(key):
    global ACTION
    
    key_event=str(key).replace("'",'')
    #print(key_event)
    if key_event=='Key.pause':
        ACTION='pause/paly'
    if key_event=='Key.page_up':
        ACTION='volume_up'
    if key_event=='Key.page_down':
        ACTION='Volume_down'
    if key_event=='Key.end':
        ACTION='next'
    if key_event=='Key.home':
        ACTION='previous'
    if key_event=='Key.delete':
        ACTION='clr'
    
    if len(key_event)<2 and ord(key_event)>47 and ord(key_event)<58:
        ACTION='song_'+ key_event
    
    if key_event=='Key.scroll_lock':
        ACTION='ACTION'
    
    
        
        
            
if playlist!=[]:
    thd()
    with Listener(on_press=on_press) as listener:
        listener.join()
else:
    input('no song in folder press any key to exit...')
    
