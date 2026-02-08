import math
import numpy as np
from PIL import Image
def main():
    st = input("Enter your string to convert :")
    BIT_PER_CHAR = 8
    length = (len(st)+1)*BIT_PER_CHAR  # size for 8 bits per letter + length specifier
    bitstream = [int(x) for x in f"{len(st):08b}"]
    matrixsize = math.ceil(math.sqrt(length)) # length/breadth of the square 
    for char in st:
        for x in f"{ord(char):08b}":
            bitstream.append(int(x))
    bitstream.extend([0]*((matrixsize**2)-len(bitstream))) # fill the remaining gap with spaces to make a square
    arr = np.array(bitstream, dtype=np.uint8).reshape(matrixsize, matrixsize)*255
    img = Image.fromarray(255-arr, 'L') # invert black and white 0 and 1
    imgshow = img.resize((250,250), resample=Image.NEAREST) # upscale
    imgshow.show()
    imgname = input("Type image name to save as or 0 to not save :")
    if imgname != '0':
        img.save(f"{imgname}.png")
main()