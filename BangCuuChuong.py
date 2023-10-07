for i in range(1, 10):
    for j in range(2, 10):
        line = "{0} * {1} = {2:>3}".format(j, i, i*j)
        print(line, end='\t\t')
    print()