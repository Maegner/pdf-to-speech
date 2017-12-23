# pdf-to-speech

PDF-to-speech is a Python script that reads your PDF's to you, 
and it can also create a mp3 file with your full PDF.

## Getting Started

Pdf-to-speech requires python to run, you can use Python3 or Python2.7.
There is not yet a version for Windows systems, this one might work but i have not had the change to test it properly yet.

To install the needed python libraries and AVbin needed for the pyglet library:

On linux
```sh
$ chmod +x setupLinux.sh
$ ./setupLinux.sh
```
On Mac OS X
```sh
$ ./setupMac.sh
```

If there is a problem with the AVbin version for your PC just go to https://avbin.github.io/AVbin/Download.html and download and install the right one.

#### Having pdf-to-speech reading the pdf to you live

Copy the pdf file you want to listen to the pdf-to-speech folder and run

```sh
$ python3 pdfTospeech.py filename.pdf 
```
or if you want to specify a certaint page for it to start reading
```sh
$ python3 pdfTospeech.py filename.pdf  pageNumber
```

It will take around 10-20 seconds before it actually starts reading, it could be faster or slower depending on the amount of text in the first page

You can stop it at any time by clicking ctrl-c and the next time you want to listen to your pdf just run
```sh
$ python3 pdfTospeech.py filename.pdf 
```
and it will start on the beginning of the page you were last listening to.

#### Saving the pdf in an mp3 file for later

Copy the pdf file you want to listen to the pdf-to-speech folder and run

```sh
$ python3 pdfTomp3.py filename.pdf 
```
or if you want to specify a certaint page for it to start reading
```sh
$ python3 pdfTomp3.py filename.pdf  pageNumber
```
Keep in mind that this might take a while if the pdf is very large

## Author
- Francisco Aguiar (franciscomaguiar@gmail.com)