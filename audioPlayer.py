import pyglet
import os
import pickle
import threading
from time import sleep

class AudioPlayer(threading.Thread):
    def __init__(self,startingPage,filename,qeue):
        threading.Thread.__init__(self)
        self.qeue = qeue
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
            if not self.qeue:
                sleep(5)
            else:
                self.currentPage = self.qeue.pop(0)
                audioFileName = str(self.currentPage) + ".mp3" 
                if os.path.isfile(audioFileName):
                    print("Reading page " + str(self.currentPage))
                    self.playAudio(audioFileName)
                self.registerLastReadPage()
