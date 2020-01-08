#! use python3
# tableprinter.py
# printTable(): takes a list of lists of strings and displays it in a well-organized
# table with each column right-justified.Assume that all the inner list will contain
# the same number of strings.For example, the value could look like this:
"""tableData = [['apples','oranges','cherries','banana'],
           ['Alice', 'Bob' 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]
printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
"""
tableData = [['apples', 'oranges', 'cherries','banana'],['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(tableData):
    # colWidths store the maximum width of each column to fit all the strings
    colWidths = []
    for data in tableData:
        widths = []
        for word in data:
            widths.append(len(word))
        colWidths.append(max(widths))

    # print stuff
    for i in range(len(tableData[0])): # row
        for j in range(len(tableData)): # col
            print(tableData[j][i].rjust(colWidths[j]), end=' ') # rightalign,space sep

        print()
        
    

printTable(tableData)


            
        
