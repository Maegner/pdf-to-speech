import os
import pickle
import pyglet
import threading
import pdfReader
from time import sleep
from gtts import gTTS

class AudioMaker(threading.Thread):
    def __init__(self,filename,lang,startingPage,qeue,all=False):
        threading.Thread.__init__(self)
        self.qeue = qeue
        self.currentPage = startingPage
        self.filename = filename
        self.pdfReaderObject = pdfReader.openFile(filename)
        self.lang = lang
        self.all = all

    
    def entireBookToPdf(self):
        entireText = ""
        while self.currentPage < self.pdfReaderObject.numPages:
            self.currentPage += 1
            entireText += '\n' + pdfReader.extractTextFromPage(self.pdfReaderObject,self.currentPage)
        print("All read, Converting to audio!")
        tts = gTTS(text=entireText, lang=self.lang)
        audioFile =  "audioFiles/" + self.filename[:-3] + 'mp3'
        tts.save(audioFile)
        print("MP3 audio file saved in " + audioFile)

    def flagForFileCreated(self,pageNumber):
        print("Qeued page " +str(pageNumber))
        self.qeue.append(pageNumber)


    def makeAudioFile(self,pageNumber):
        pageText = pdfReader.extractTextFromPage(self.pdfReaderObject,pageNumber)
        if pageText == "":
            self.flagForFileCreated(pageNumber)
            return
        tts = gTTS(text=pageText, lang=self.lang)
        audioFilename = str(pageNumber) + ".mp3"
        tts.save(audioFilename)
        print("Created audio file for page " + str(pageNumber))
        self.flagForFileCreated(pageNumber)
        music = pyglet.media.load(audioFilename, streaming=False)
        sleep(music.duration*0.50)

    def run(self):
        if(not self.all):
            while self.currentPage < self.pdfReaderObject.numPages:
                self.makeAudioFile(self.currentPage)
                self.currentPage += 1
        else:
            self.entireBookToPdf()     