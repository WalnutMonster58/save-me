import random
import time
import json



while True:
    randomLetter = random.choice(bigGuyLetters)
    jsonObject = json.dumps(randomLetter, indent = 4)

    with open('bigData.json', 'a') as outfile:
        outfile.write(jsonObject)
    print(jsonObject)
    time.sleep(.1)