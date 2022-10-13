from ruthieAnalysis import *

instaPrivacy = analysisProj("instaPrivacy.txt")

print("number of lines:", instaPrivacy.filelen())

print("number of stanzas:", instaPrivacy.stanzact())

print("number of words per line", instaPrivacy.wordct())

print("number of words", instaPrivacy.total())

impWords = ["personal", "private"]
for w in impWords:
    print(f"number of {w} in insta:", instaPrivacy.impWords(w))