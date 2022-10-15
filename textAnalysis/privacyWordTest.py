from ruthieAnalysis import *

privacyPolicy = analysisProj("instaPrivacy.txt")

print("number of lines:", privacyPolicy.filelen())

print("number of stanzas:", privacyPolicy.stanzact())

print("number of words per line", privacyPolicy.wordct())

print("number of words", privacyPolicy.total())

impWords = ["personal", "private", "privacy", "protection", "rights", "safe", "guard", "legal", "settings", " lock ", " locks ", "password", "username", "block"]
numWords = 0
for w in impWords:
    print(f'number of {w} in insta:', privacyPolicy.privacyWords(w))
    numWords += privacyPolicy.privacyWords(w)
print('score = ', numWords)
