class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        #i = row1
        #print(row1,row2)
        for i in range(row1,row2+1):
            for s in range(col1,col2+1):
                self.rectangle[i][s] = newValue
            #print(self.rectangle[i])

    def getValue(self, row, col):
        print(self.rectangle[row][col])
        return self.rectangle[row][col]


subrectangleQuery = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
subrectangleQuery.getValue(0, 2); # return 1
subrectangleQuery.updateSubrectangle(0, 0, 3, 2, 5);
subrectangleQuery.getValue(0, 2); # return 5
subrectangleQuery.getValue(3, 1); # return 5
subrectangleQuery.updateSubrectangle(3, 0, 3, 2, 10);
subrectangleQuery.getValue(3, 1); # return 10
subrectangleQuery.getValue(0, 2); # return 5
