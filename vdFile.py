def writeFile(path):
    """Overwrite file path"""
    file = open(path, 'w', encoding='utf-8')    # use utf-8 to write vietnamese
    file.writelines("SV001;Hoàng A;1/1/2001\n")
    file.writelines("SV002;Nguyễn B;2/2/2001\n")
    file.writelines("SV003;Lê C;3/3/2001\n")
    file.close()


def readFile(path):
    """Open and read file path"""
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        print(data)
    file.close()


writeFile("vdFile.txt")
readFile("vdFile.txt")
