import pygame as sound
from time import sleep

# sample.PlaySound("kick.wav" , sample.SND_FILENAME)



def loadSamples(loaded , strKey = ''):

    if (loaded == False): # if the file is not loaded, load the file
        
        s1 = sound.mixer.Sound("kick.wav") ## problem line
        
    elif (loaded == True):
        if (strKey == 'k'):
            s1.play()
            sound.time.wait(1000)
        elif (strKey == 's'):
            s2.play()
        elif (strKey == 'h'):
            s3.play()
            
        





def beat(bang, instrument):
    if (bang == 1):
        loadSamples(True, instrument)
    else:
        pass

def loadSequence(track):
    
    sound.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    sound.init() #turn all of pygame on.
    
    n1 = track[0:2]
    n2 = track[3:5]
    n3 = track[6:8]
    n4 = track[9:11]
    n5 = track[12:14]
    n6 = track[15:17]
    n7 = track[18:20]
    n8 = track[21:23]
    n9 = track[24:26]
    n10 = track[27:29]
    n11 = track[30:32]
    n12 = track[33:35]
    n13 = track[36:38]
    n14 = track[39:41]
    n15 = track[42:44]
    n16 = track[45:47]
    
    BPM = .250
    
    while(True):
    
        beat(n1[0],n1[1])
        sleep(BPM)
        beat(n2[0],n2[1])
        sleep(BPM)
        beat(n3[0],n3[1])
        sleep(BPM)
        beat(n4[0],n4[1])
        sleep(BPM)
        beat(n5[0],n5[1])
        sleep(BPM)
        beat(n6[0],n6[1])
        sleep(BPM)
        beat(n7[0],n7[1])
        sleep(BPM)
        beat(n8[0],n8[1])
        sleep(BPM)
        beat(n9[0],n9[1])
        sleep(BPM)
        beat(n10[0],n10[1])
        sleep(BPM)
        beat(n11[0],n11[1])
        sleep(BPM)
        beat(n12[0],n12[1])
        sleep(BPM)
        beat(n13[0],n13[1])
        sleep(BPM)
        beat(n14[0],n14[1])
        sleep(BPM)
        beat(n15[0],n15[1])
        sleep(BPM)
        beat(n16[0],n16[1])
        sleep(BPM)
        


        
track1 = '1k 0k 0k 1s 1k 0k 0k 0k 1k 0k 0k 0k 1k 1s 1s 0k ' #notes in the sequence: first char an int [0,1] -> [False, True] second char [k, s, h, t] -> [kick, snare, hat, tom]
         
track2 = '1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h '


loadSamples(False) # load the samples
loadSequence(track1) # load the sequence

''' 
 TESTING IF NOTES ARE CORRECTLY SPLITTED
    print(n1 , len(n1))
    print(n2 , len(n2))
    print(n3 , len(n3))
    print(n4 , len(n4))
    print(n5 , len(n5))
    print(n6 , len(n6))
    print(n7 , len(n7))
    print(n8 , len(n8))
    print(n9 , len(n9))
    print(n10 , len(n10))
    print(n11 , len(n11))
    print(n12 , len(n12))
    print(n13 , len(n13))
    print(n14 , len(n14))
    print(n15 , len(n15))
    print(n16 , len(n16))
    
  
                
                


sampleTrack = '#s #s #s #s #s #s #s #s #s #s #s #s #s #s #s #s' 

# in { 0 , 1}
s in {s, k, h, t}

'''


    



    
    
    



    
        

