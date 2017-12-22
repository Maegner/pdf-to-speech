import PyPDF2
import pickle

def openFile(filename):
    pdfFileObj = open(filename, 'rb')
    return PyPDF2.PdfFileReader(pdfFileObj)

def extractTextFromPage(readerObject,pageNumber):
    pageObj = readerObject.getPage(pageNumber)
    return pageObj.extractText()
