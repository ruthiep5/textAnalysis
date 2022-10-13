import re


class analysisProj:

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()
        
    def filelen(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            if len(line) != 0:
                n = n +1
        return n

    def stanzact(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            if line == '':
                n = n + 1
            c = n + 1
        return c

    def wordct(self):
        for i in range(len(self.lines)):
            line = self.lines[i].strip().split(" ")
        return len(line)

    def total(self):
        total = 0
        for i in range(len(self.lines)):
            line = self.lines[i].strip().split(" ")
            n = len(line)
            total = total + n
        return total

    def privacyWords(self, word):
        n = 0
        r = []
        self.getSentences()
        for s in self.sentences:
            if word.lower() in s.lower():
                n += 1
                r.append(s)
        return n, r
    
    def getSentences (self):
        with open (self.filename) as f:
            fullText = f.read()
        fullText = f.read()
        self.sentences = fullText.split(".")


