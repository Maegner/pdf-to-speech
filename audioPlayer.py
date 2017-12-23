import pyglet
import os
import pickle
import threading
from time import sleep

class AudioPlayer(threading.Thread):
    def __init__(self,startingPage,filename):
        threading.Thread.__init__(self)
        self.currentPage = startingPage
        self.filename = filename
    
    def playAudio(self,filename):
        audio = pyglet.media.load(filename, streaming=False)
        audio.play()
        sleep(audio.duration)
        os.remove(filename)

    def registerLastReadPage(self):
        logger = 'logs/'+self.filename[:-3]+'pk'
        with open(logger, 'wb') as fi:
            pickle.dump(self.currentPage, fi)

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
                self.registerLastReadPage()
