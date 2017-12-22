import pyglet
import os
import threading
from time import sleep

class AudioPlayer(threading.Thread):
    def __init__(self,startingPage):
        threading.Thread.__init__(self)
        self.currentPage = startingPage
    
    def playAudio(self,filename):
        audio = pyglet.media.load(filename, streaming=False)
        audio.play()
        sleep(audio.duration)
        os.remove(filename)
    
    def run(self):
        while True:
            audioFileName = str(self.currentPage) + ".mp3"
            flagFile = str(self.currentPage) + ".pk"
            
            if not os.path.isfile(flagFile):
                print("Waiting for audio file for page " + str(self.currentPage))
                sleep(2)
            else:
                if os.path.isfile(audioFileName):
                    print("Reading page " + str(self.currentPage))
                    self.playAudio(audioFileName)
                os.remove(flagFile)
                self.currentPage += 1
