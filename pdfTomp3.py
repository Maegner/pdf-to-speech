import sys
from time import sleep
from audioMaker import AudioMaker

def main():
    
    arguments = sys.argv
    narguments = len(arguments)

    if narguments < 2:
        sys.stderr.write('[ERROR] please provide filename\n[HELP] $python3 pdfToSpeak.py foo.pdf\n')
        return
    if not os.path.isfile(arguments[1]):
        sys.stderr.write('[ERROR] there is no file named ' + arguments[1] + ' in the pdf-to-spech folder\n')
        return
    if narguments >= 3:
        audioMakerThread = AudioMaker(arguments[1],"en",int(arguments[2]),all=True)
    if narguments == 2:
        audioMakerThread = AudioMaker(arguments[1],"en",startingPage,all=True)
    audioMakerThread.daemon = True
    audioMakerThread.start()
    