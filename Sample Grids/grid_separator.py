# Separate the file of grids into individual files

path = "sudoku.txt"

curLine = 0

with open(path, "r") as fp:
    while True:
        curLine = fp.readline()
        if curLine is None or curLine == "":
            break
        if curLine[0] == "G":
            gridNum = int(curLine[-3:])

        newFile = open("Grid{:02d}.txt".format(gridNum), "w")

        for i in range(9):
            newFile.writelines(fp.readline().replace("\n",""))
            if i != 8:
                newFile.write("\n")
        
        newFile.close()
    
