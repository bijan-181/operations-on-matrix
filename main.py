class operation:
    def __init__(self):
        a=0#todo
    def check_row(self,mR):
        while mR.isdigit() == False :
            print("you input is not an integer number.pleas try again:)")
            mR=input(f"insert row of your matrix:")
        else:
            return int(mR)
    def check_column(self,mC):
        while mC.isdigit() == False :
            print("you input is not an integer number.pleas try again:)")
            mC=input(f"insert column of your matrix:")
        else:
            return int(mC)
    def check_input(self,draye,mR,mC):
        while draye.isdigit() == False :
            print("oh your input is unaccepetable.pleas try again:)")
            draye=input(f"draye{mR+1 ,mC+1} ra vared konid:")
        else:
            return int(draye)
    def get_matrix(self):
        matrixRow=input("insert row of your matrix:")
        matrixRow=self.check_row(matrixRow)
        matrixColumn=input("insert row of your column:")
        matrixColumn=self.check_row(matrixColumn)
        matrix=[]
        for mR in range (matrixRow):
            matrix.append([])
            for mC in range(matrixColumn):
                draye=input(f"enter ({mR+1} , {mC+1}) matrix element:")
                draye=self.check_input(draye , mR , mC)
                matrix[mR].insert( mC , draye)
        return matrix , matrixColumn , matrixRow
    def show_matrix(self,matrix):
        for mR in matrix:
            if mR == matrix[0] :
                print('┌ ',end="")
            elif mR == matrix[-1]:
                print("└ ",end="")
            else:
                print("| ",end="")
            for mC in mR:
                print(mC,end=" ")
            if mR == matrix[0]:
                print('┐')
            elif mR == matrix[-1]:
                print("┘")
            else:
                print("|")
    def plus(self):
        matrix1 ,matrix1Column ,matrix1Row = self.get_matrix()
        matrix2 ,matrix2Column ,matrix2Row = self.get_matrix()
        matrixResult = []
        if matrix1Column == matrix2Column and matrix1Row == matrix2Row:
            for mR in range (matrix1Row):
                matrixResult.append([])
                for mC in range(matrix1Column):
                    elementResualt = matrix1[mR][mC] + matrix2[mR][mC]
                    matrixResult[mR].insert(mC,elementResualt)
    def minus(self):
        matrix1 ,matrix1Column ,matrix1Row = self.get_matrix()
        matrix2 ,matrix2Column ,matrix2Row = self.get_matrix()
        matrixResult = []
        if matrix1Column == matrix2Column and matrix1Row == matrix2Row:
            for mR in range (matrix1Row):
                matrixResult.append([])
                for mC in range(matrix1Column):
                    elementResualt = matrix1[mR][mC] - matrix2[mR][mC]
                    matrixResult[mR].insert(mC,elementResualt)
    def multipied_by_integer(self):
        f=0#todo
    def multipied_matrices(self):
        g=0#todo
    def determinant(self):
        h=0#todo
    def invert(self):
        i=0#todo

operation = operation()