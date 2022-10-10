class analysisProj:

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()
        
    def filelen(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            print(len(line))
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
        for i in range(len(lines)):
            lt = lines[i].strip().ssplit(" ")
            return len(lt)

    total = 0
    def total(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            n = len(lt)
            total = total + n
            return total
    
    def average(self):
        for i in range(len(lines)):
            lt = lines[i].strip().split(" ")
            average = total/len(self.lines)
            return average


