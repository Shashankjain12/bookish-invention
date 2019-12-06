#step1.importing the image
#step2.Extracting the words from image
#step3.after extraction of words creating the vector of very less ie only meanin#gful information is kept
#step4. data preprocessing using any of nlp library
#step5.after preprocessing of information creating a training set and basically #creating a sort of mapping using rnn
#step1. Importing of the libraries
"""
    Author:Shashank Jain
    github@username:Shashankjain12
"""
#!usr/bin/python
import cv2
import os
import sys
from PIL import Image
import pytesseract
import re
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import PyPDF2
from translate import Translator

#l=input("Enter the language you want to convert your notes:")

class NotesCreator:
    
    def __init__(self,file_name):

        self.translator=Translator(to_lang="Hindi")
        self.lemmatizer=WordNetLemmatizer()
        self.k=input("Do you want to translate your notes to Hindi? ")
        self.file_name=file_name
        #self.p=os.path.splitext(os.path.basename(os.path.join(os.getcwd(),file_name)))
        self.p=os.path.splitext(file_name)
        if self.p[1]==".png":
            self.pngnotes()
        else:
            self.pdfnotes()
    
    def pngnotes(self):
        
        if self.p[1]=='.png':
            
            img=cv2.imread(self.file_name)
            a=pytesseract.image_to_string(img)
            cv2.imshow('image',img)
            cv2.waitKey()
            #b=a.split()
            #print(b)
            sentences=nltk.sent_tokenize(a)
            word_tags=[]
            
            for i in range(len(sentences)):
                sentences[i]=re.sub(r"[@#$%^&|?!'\"]"," ",sentences[i])
                words=nltk.word_tokenize(sentences[i])
                newwords=[self.lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
                sentences[i]=' '.join(newwords)
                """
                    tagged_words=nltk.pos_tag(newwords)
                for tw in tagged_words:
                    word_tags.append(tw[0]+" "+tw[1])
                tagged_par=" ".join(word_tags)
            namedEnt=nltk.ne_chunk(tagged_words)
            print(namedEnt)
            namedEnt.draw()
            print(tagged_par)
                """
    
            print(sentences) 
            paragraph="\n".join(sentences)
            if self.k=='yes' or self.k=='y':
                translation=self.translator.translate(paragraph)
                print(translation)
            else:
                print(paragraph)
            words=nltk.word_tokenize(paragraph)
            tagged_words=nltk.pos_tag(words)
            namedEnt=nltk.ne_chunk(tagged_words)
            #for i in range(len(namedEnt)):
            #       print(namedEnt[i][1])
            #       print(namedEnt[i][1][i] 
            namedEnt.draw()
            #print(paragraph)
    
    def pdfnotes(self):
        if self.p[1]==".pdf":
            pdfFileObject = open('/home/shashank/Downloads/'+self.file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

            count = pdfReader.numPages
            sentence=[]
            word_tags=[]
            for i in range(count):
                page = pdfReader.getPage(i)
                sentence.append(page.extractText().split('\n'))
                sentences=nltk.sent_tokenize(page.extractText())
                for j in range(len(sentences)):
                    sentences[j]=re.sub(r"[Ò¥.@#$%^&|?!':\n\"//]"," ",sentences[j])
                    words=nltk.word_tokenize(sentences[j])
                    newwords=[self.lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
                    sentences[j]=' '.join(newwords)
                #print(sentences)

                paragraph="\n".join(sentences)
                #translation from english to any other language
                if self.k=='yes' or self.k=='y': 
                    translation=self.translator.translate(paragraph)
                    print(translation)
                else:
                    print(paragraph)
                words=nltk.word_tokenize(paragraph)
                tagged_words=nltk.pos_tag(words)
                namedEnt=nltk.ne_chunk(tagged_words)
                print("page "+str(i)+":")
                namedEnt.draw()


if __name__=="__main__":
    lang=input("Enter the language you want to convert in ?")
    filename=sys.argv[1]
    notes=NotesCreator(filename)
