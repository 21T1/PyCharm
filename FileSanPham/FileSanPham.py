def writeFile(path, data):
    """Write to an existing file path"""
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data + '\n')
    file.close()


def readFile(path):
    """Read the data from an existing file path"""
    arrProduct = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct