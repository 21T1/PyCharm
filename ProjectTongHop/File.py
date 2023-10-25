path = "database.txt"


def writeFile(data):
    try:
        file = open(path, 'a', encoding='utf-8')
        file.writelines(data + '\n')
        file.close()
    except:
        pass


def readFile():
    lst = []
    try:
        file = open(path, 'r', encoding='utf-8')
        for line in file:
            lst.append(line.strip().split(';'))
        file.close()
    except:
        pass
    return lst