from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import PyPDF2



#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

   
def convertMultiple(pdfDir, txtDir, tagDir):
    txtFile = open(txtDir, "r")        
    tags_ex = ""
    tags = list()            
    for gives in txtFile :
        tags_ex = gives.strip()
        if tags == [] :
            tags += gives.split()
        txts = ""
        for examine in range(len(tags)) :
            txts = tags_ex.find(tags[examine])
            if txts != -1 :
                break
        if txts == -1 :
            tags += gives.split()
                    
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            print (pdf.strip(".pdf"))
            try :
                text = convert(pdfFilename) #get string of text content of pdf
            except :
                text = "Can't convert?!"      
                                                     
            #pdfname = ""
            #for i in range(len(tags)) :
             #   txts = ""
              #  txts = text.find(tags[i])
               # if txts != -1 : 
                #    tagFilename = tagDir + tags[i] + ".txt"
                 #   textFile = open(tagFilename, "w") #make text file                    
                  #  pdfname += str(pdf)
                   # pdfname += "\n"
                    #textFile.write(pdfname) #write text to text file
			#textFile.close
                   
            pdfname = ""
            #no_of_tags = 0
            txts_extar = list()
            #print("Searching Tags...")
            for examine2 in range(len(tags)) :
                txt_tag = ""
                txt_tag = text.find(tags[examine2])
                tagFilename = tagDir + tags[examine2] + ".txt"
                textFile = open(tagFilename, "a+") #make text file
                if txt_tag != -1 :
                    if txts_extar == [] :
                        txts_extar += tags[examine2].split()
                        pdfname += str(pdf.split())
                        pdfname += " | "
                        no_of_tags = 1
                    ex_tags = ""
                    for examine3 in range(len(txts_extar)) :
                        ex_tags = tags[examine2].find(txts_extar[examine3])
                        if ex_tags != -1 :
                            break
                    if ex_tags == -1 :                        
                        txts_extar += tags[examine2].split()
                        pdfname += str(pdf.strip(".pdf"))
                        pdfname += "\n"
                        #pdfname += " | "
                        #no_of_tags = 1
            textFile.write(pdfname)
            

testpdfDir = raw_input("Location of PDF file : ")
pdfDir = ""
for test1 in testpdfDir :
    if test1 == "\\" :
        pdfDir += "\\\\"  
    else :
        pdfDir += test1
pdfDir += "\\\\"

testtagDir = raw_input("Location Create of Tagfile : ")
tagDir = ""
for test3 in testtagDir :
    if test3 == "\\" :
        tagDir += "\\\\"  
    else :
        tagDir += test3
tagDir += "\\\\"

testtxtDir = raw_input("Location of Tags & '\+(Name of File)' : ")
txtDir = ""
for test2 in testtxtDir :
    if test2 == "\\" :
        txtDir += "\\\\"  
    else :
        txtDir += test2
txtDir +=".txt"

convertMultiple(pdfDir, txtDir, tagDir)
