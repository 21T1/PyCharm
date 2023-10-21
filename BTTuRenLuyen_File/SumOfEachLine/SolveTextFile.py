def readFileTxt(path):
    """Read file path"""
    arrNum = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip().split(";")
        del data[10]
        arrNum.append(data)
    return arrNum


def writeFileTxt(path, data):
    """Write data to an existing file path"""
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data + '\n')
    file.close()


# writeFileTxt("Number.txt", "100; 9; 8; 7; 6; 5; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 99; 8; 7; 6; 5; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 88; 7; 6; 5; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 77; 6; 5; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 66; 5; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 6; 55; 4; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 6; 5; 44; 3; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 6; 5; 4; 33; 2; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 6; 5; 4; 3; 22; 1;")
# writeFileTxt("Number.txt", "10; 9; 8; 7; 6; 5; 4; 3; 2; 11;")
