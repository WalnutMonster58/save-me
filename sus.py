from typing import Counter
from PIL import Image

counter = 0

while counter <= 10:

    im = Image.open(r"apple.jpg") 
  
    im.show() 
    
    counter = counter + 1
    
    