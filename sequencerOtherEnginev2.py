'''
    THIS FOLLOWING PROGRAM IS A MULTITRACK SEQUENCER THAT USES STRINGS
'''


import pyglet
#from time import sleep
import sys
from exitstatus import ExitStatus
import pause as INTERVAL
from threading import Thread


# sample.PlaySound("kick.wav" , sample.SND_FILENAME)

def main():
        
    global pyglet
    
    pyglet.lib.load_library('avbin64')
    pyglet.have_avbin=True
   
    loadSamples() # load the samples
    
    track1 = '1k 1k 0s 1k 0k 1k 0s 0s 1k 1k 0s 1k 0k 1k 0s 0k' #notes in the sequence: first char an int [0,1] -> [False, True] second char [k, s, h, t] -> [kick, snare, hat, tom]     
    track2 = '1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h 1h'
    track3 = '0s 0s 1s 0s 0s 0s 1s 0s 0s 0s 1s 0s 1s 1s 1s 1s'
    
    
    t1 = Thread(target=ch1, args=(track1, 300)) # first track
    t2 = Thread(target=ch1, args=(track2, 300)) # second track
    t3 = Thread(target=ch1, args=(track3, 300)) # third track
    

    # start all the processes first 
    t1.start()
    t2.start()
    t3.start()
    
    INTERVAL.seconds(5) # wait to sync
    
    # join them in order to run them at the same time (supposedly)
    t1.join()
    t2.join()
    t3.join()
    

        
def exitProgram(): #unused exit program function
    a = input("type 'q' then ENTER to exit")   
    if (a == 'q'):
        sys.exit(ExitStatus.success)
        
        


def loadSamples():
    
    # global sample variales, expandability will be added soon!
    global hat1 , kick1, snare1 

#        kick1 = pygame.mixer.Sound("kick.ogg")
#        hat1 = pygame.mixer.Sound("hat.ogg")
#        snare1 = pygame.mixer.Sound("snare.ogg")


    # load the files (expandability soon, but 3 samples to start with)
    kick1 = pyglet.media.StaticSource(pyglet.media.load('kick.ogg'))
    snare1 = pyglet.media.StaticSource(pyglet.media.load('snare.ogg'))
    hat1 = pyglet.media.StaticSource(pyglet.media.load('hat.ogg'))
        
           
#  this function detects the string chunk SIZE 2.
def beat(bang, instrument):
   
    if (bang == '1'):
        if(instrument == 'k'):
            kick1.play()
              
        elif(instrument == 's'):
            snare1.play()
            
        elif(instrument == 'h'):
            hat1.play()
        else:
            pass
    elif(bang == '0'):
        pass
        
def ch1(track, BPM):
    
    # string partitions for chunk
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
      
    # for now it is an infinitie loop, later limitation will be added as iteration no.
    while True:
        
        INTERVAL.milliseconds(BPM) # wait time
        beat(n1[0],n1[1])          # [0] -> if play true [1] -> sample :: more parameters will be added soon
        INTERVAL.milliseconds(BPM)
        beat(n2[0],n2[1])
        INTERVAL.milliseconds(BPM)
        beat(n3[0],n3[1])
        INTERVAL.milliseconds(BPM)
        beat(n4[0],n4[1])
        INTERVAL.milliseconds(BPM)
        beat(n5[0],n5[1])
        INTERVAL.milliseconds(BPM)
        beat(n6[0],n6[1])
        INTERVAL.milliseconds(BPM)
        beat(n7[0],n7[1])
        INTERVAL.milliseconds(BPM)
        beat(n8[0],n8[1])
        INTERVAL.milliseconds(BPM)
        beat(n9[0],n9[1])
        INTERVAL.milliseconds(BPM)
        beat(n10[0],n10[1])
        INTERVAL.milliseconds(BPM)
        beat(n11[0],n11[1])
        INTERVAL.milliseconds(BPM)
        beat(n12[0],n12[1])
        INTERVAL.milliseconds(BPM)
        beat(n13[0],n13[1])
        INTERVAL.milliseconds(BPM)
        beat(n14[0],n14[1])
        INTERVAL.milliseconds(BPM)
        beat(n15[0],n15[1])
        INTERVAL.milliseconds(BPM)
        beat(n16[0],n16[1])
        

        
main()   #run main function    

