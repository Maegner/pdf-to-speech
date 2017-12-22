from audioMaker import AudioMaker
from audioPlayer import AudioPlayer
import pickle
import os
import sys
from time import sleep

def hasReadingStarted(filename):
    picklename = filename[:-3]
    picklename += 'pk'
    return os.path.isfile(filename)

def retrieveLastReadPage(filename):
    with open(filename, 'rb') as fi:
        return pickle.load(fi)

def main():
    
    arguments = sys.argv
    narguments = len(arguments)

    if narguments < 2:
       sys.stderr.write('[ERROR] please provide filename\n[HELP] $python2.7 pdfToSpeak.py foo.pdf\n')
       return

    if not os.path.isfile(arguments[1]):
        sys.stderr.write('[ERROR] file ' + arguments[1] + ' does not exist\n')
        return

    if narguments >= 3:
        audioMakerThread = AudioMaker(arguments[1],"en",int(arguments[2]),all=False)
        audioPlayerThread = AudioPlayer(int(arguments[2]))

    if narguments == 2:
        audioMakerThread = AudioMaker(arguments[1],"en",0,all=False)
        audioPlayerThread = AudioPlayer(0)

    audioMakerThread.daemon = True
    audioPlayerThread.daemon = True
    audioMakerThread.start()
    audioPlayerThread.start()

    while True:
        sleep(10000)

if __name__ == "__main__":
    main()