import re
'''class for a text analysis project'''

class analysisProj:

    '''initializes class'''
    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()
        print(len(self.lines))
        
    '''finds the number of lines'''
    def filelen(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            if len(line) != 0:
                n = n +1
        return n

    '''finds the number of stanzas'''
    def stanzact(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            if line == '':
                n = n + 1
            c = n + 1
        return c

    '''finds number of words in a line'''
    def wordct(self):
        for i in range(len(self.lines)):
            line = self.lines[i].strip().split(" ")
        return len(line)

    '''finds total number of words in document'''
    def total(self):
        total = 0
        for i in range(len(self.lines)):
            line = self.lines[i].strip().split(" ")
            n = len(line)
            total = total + n
        return total

    '''finds specific words having to do with my project'''
    def privacyWords(self, word):
        n = 0
        r = []
        self.getSentences()
        for s in self.sentences:
            if word.lower() in s.lower():
                n += 1
                r.append(s)
        return n
    
    '''finds specific sentences'''
    def getSentences (self):
        with open (self.fname) as f:
            fullText = f.read()
        self.sentences = fullText.split(".")


