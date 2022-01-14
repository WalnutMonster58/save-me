import random
import time
import json


bigGuyLetters = ["00100000", "01000001", "01000010", "00100000", "01000011", "01000100", "01000101", "00100000", "01000110", "01000111", "01001000", "01001001", "01001010", "01001011", "01001100", "01001101", "01001110", "01001111", "01010000", "01010001", "01010010", "01010011", "01010100", "01010101", "01010110", "01010111", "01011000", "01011001", "01011010"]

while True:
    randomLetter = random.choice(bigGuyLetters)
    jsonObject = json.dumps(randomLetter, indent = 4)

    with open('bigData.json', 'a') as outfile:
        outfile.write(jsonObject)
    print(jsonObject)
