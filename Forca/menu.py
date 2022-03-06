import os

matriz_forca=[["#", "-", "-", "-", " "],
                ["|", " "," ", ".", " "],
                ["|", " ",".", ".", "."],
                ["|", " ",".", " ", "."]]

def tela_principal():
#    print(" ________")
#    print("|        |")
#    print("|")
#    print("|")
#    print("|")
#    print("|\n")
#                      0    1    2    3    4
#   0  matriz_forca=[["#", "-", "-", "-", " "],  posiççoes do corpo: [1][3], [2][2], [2][3], [2][4], [3][2], [3][4]
#   1                 ["|", " "," ", "O", " "],
#   2                 ["|", " ","/", "|", "\\"],
#   3                 ["|", " ","/", " ", "\\"]]
    
    
    os.system("cls")

    i=j=0
    while i<4:
        j=0
        while j<5:
            print(matriz_forca[i][j], end='')
            j+=1
        print()
        i+=1
    print()

def redefinir_matriz(mat):

    mat=[["#", "-", "-", "-", " "],
        ["|", " "," ", ".", " "],
        ["|", " ",".", ".", "."],
        ["|", " ",".", " ", "."]]

    return mat