def readFile(path):
    f = open(path, 'r', encoding='utf-8')
    lst = []
    for line in f:
        lst.append(line.strip().split(","))
    f.close()
    return lst


def writeFile(path, data):
    f = open(path, 'a', encoding='utf-8')
    f.writelines(data + '\n')
    f.close()


