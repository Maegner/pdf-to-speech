from audioMaker import AudioMaker
from audioPlayer import AudioPlayer
import pickle
import os
import sys
from time import sleep

def hasReadingStarted(filename):
    picklename = 'logs/' + filename[:-3]
    picklename += 'pk'
    return os.path.isfile(picklename)

def retrieveLastReadPage(filename):
    picklename = 'logs/' + filename[:-3]
    picklename += 'pk'
    with open(picklename, 'rb') as fi:
        return pickle.load(fi)

def main():
    
    qeue = []
    
    os.system("rm *.mp3")

    arguments = sys.argv
    narguments = len(arguments)

    os.system

    if narguments < 2:
       sys.stderr.write('[ERROR] please provide filename\n[HELP] $python3 pdfToSpeak.py foo.pdf\n')
       return

    if not os.path.isfile(arguments[1]):
        sys.stderr.write('[ERROR] there is no file named ' + arguments[1] + ' in the pdf-to-spech folder\n')
        return

    if narguments >= 3:
        audioMakerThread = AudioMaker(arguments[1],"en",int(arguments[2]),qeue,all=False)
        audioPlayerThread = AudioPlayer(int(arguments[2]),arguments[1],qeue)

    if narguments == 2:
        if hasReadingStarted(arguments[1]):
            startingPage = retrieveLastReadPage(arguments[1])
        else:
            startingPage = 0
        audioMakerThread = AudioMaker(arguments[1],"en",startingPage,qeue,all=False)
        audioPlayerThread = AudioPlayer(startingPage,arguments[1],qeue)

    audioMakerThread.daemon = True
    audioPlayerThread.daemon = True
    audioMakerThread.start()
    audioPlayerThread.start()

    while True:
        sleep(10000)

if __name__ == "__main__":
    main()