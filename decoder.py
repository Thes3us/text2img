import numpy as np
from PIL import Image

def decode_image(path):
    BIT_PER_CHAR = 8
    # Load image and convert to grayscale
    img = Image.open(path).convert("L")
    arr = np.array(img)

    # Convert pixels to bits
    bits = (arr < 128).astype(int).flatten()

    # Read length (first 8 bits)
    length_bits = bits[:8]
    msg_length = int("".join(map(str, length_bits)), 2)

    # Read message bits
    start = 8
    end = start + msg_length * BIT_PER_CHAR
    msg_bits = bits[start:end]

    # Convert bits to characters
    chars = []
    for i in range(0, len(msg_bits), BIT_PER_CHAR):
        byte = msg_bits[i:i+BIT_PER_CHAR]
        chars.append(chr(int("".join(map(str, byte)), 2)))

    message = "".join(chars)
    return message

if __name__ == "__main__":
    filename = input("Enter your filename :")
    print(decode_image(filename))
