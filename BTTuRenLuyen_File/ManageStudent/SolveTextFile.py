def readFile(path):
    """read file path"""
    fi = open(path, 'r', encoding='utf-8')
    lst = []
    for line in fi:
        lst.append(line.strip().split(","))
    fi.close()
    return lst


def writeFile(path, data):
    """write data to the file path"""
    fo = open(path, 'a', encoding='utf-8')
    fo.writelines(data + '\n')
    fo.close()
    