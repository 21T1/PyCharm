def writeFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data + '\n')
    file.close()


def readFile(path):
    arrNum = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(',')
        arrNum.append(arr)
    file.close()
    return arrNum
