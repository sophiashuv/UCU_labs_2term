import random
from arrays import GreyscaleImage


def randomizing(width, height):
    """
    The function generates a random image
    """
    uncompressed = GreyscaleImage(width, height)
    for i in range(width):
        for j in range(height):
                uncompressed[i, j] = random.randint(0, 255)
    return uncompressed


def compress(uncompressed, width, height):
    """
    The function compress a string of numbers to a list of output numbers
    """

    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    for i in range(width):
        for j in range(height):
            uncompressed.arrey_2[i, j] = chr(uncompressed.arrey_2[i, j])

    w = ""
    result = []
    for c in range(uncompressed.nrows):
        for j in range(uncompressed.ncols):
            wc = w + str(uncompressed[c, j])
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = str(uncompressed[c, j])

    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed, width, height):
    """
    The function decompress a list of output numbers to a string of numbers
    """

    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = ""
    w = chr(compressed.pop(0))
    result += w
    im = GreyscaleImage(width, height)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    m = 0
    for i in range(width):
        for j in range(height):
            im[i, j] = ord(result[m])
            m += 1
    return im


if __name__ == '__main__':
    width = int(input("Enter width of image: "))
    height = int(input("Enter height of image: "))
    image = randomizing(width, height)
    print("-" * 50)
    print("The original image: ")
    print(str(image))
    print("Compressed image: ")
    compressed = compress(image, width, height)
    print(str(compressed) + "\n")
    print("Decompressed image: ")
    decompressed = decompress(compressed, width, height)
    print(str(decompressed) + "\n")
