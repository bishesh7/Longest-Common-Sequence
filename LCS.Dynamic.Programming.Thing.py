## Program by Hugo Sanchez '17, Pierre-Alexander Low '17, and Bishesh '18
##
## Solves both homework problems, 15.4-5 by find_longest_monotonically_increasing()
## and 15-2 by find_palindrome()

## NICE WORK: 3/3

def LCS(list2, list1):  # Returns the longest common subsequence between two lists
    global matrix
    global result
    result = []
    matrix = []
    for row in range(len(list2)+1):
        matrix.append([])
        for column in range(len(list1)+1):
            matrix[row].append([-9,0,list1[column-1], list2[row-1]])
            if(row == 0 or column == 0):
                matrix[row][column] = [0,0,0,0]

    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            if matrix[row][column][2] == matrix[row][column][3]:
                matrix[row][column][0] = matrix[row-1][column-1][0] + 1
                matrix[row][column][1] = 1 #northwest arrow
            elif matrix[row-1][column][0] >= matrix[row][column-1][0]:
                matrix[row][column][0] = matrix[row-1][column][0]
                matrix[row][column][1] = 2 # up arrow
            else:
                matrix[row][column][0] = matrix[row][column-1][0]
                matrix[row][column][1] = 0 # blank

## Debug code that prints the entire matrix 
##    for i in range(len(b)+1):
##        for j in range(len(a)+1):
##            print("[" + str(matrix[i][j][0]) + str(matrix[i][j][1]) + str(matrix[i][j][2]) + str(matrix[i][j][3]) + "]", end="\t")
##        print("", end="\n")
    return read_answer_from_matrix(len(matrix)-1, len(matrix[0])-1)
        

def read_answer_from_matrix(row,column): # Takes the completed array with arrows etc and returns the sequence as a string
    global matrix
    global result
    if( row == 0 or column == 0 ):
        return
    elif matrix[row][column][1] == 1:
        read_answer_from_matrix(row-1,column-1)
        result.append(matrix[row][column][2])
    elif matrix[row][column][1] == 2:
        read_answer_from_matrix(row-1,column)
    else:
        read_answer_from_matrix(row,column-1)
    return result
    
    

def find_palindrome(stringToCheck): # Returns longest palindrome in string using LCS
    listForm = []
    for char in stringToCheck:
        listForm.append(char)
    reverseForm = []
    for char in reversed(listForm):
        reverseForm.append(char)
    return LCS(listForm, reverseForm)

def find_longest_monotonically_increasing(inputList): # Pretty badly titled
    sortedVersion = sorted(inputList) # Uses python's built in implementation of Timsort - O(n log n)
    return LCS(inputList, sortedVersion)
    
def main():
    a = [ 3, 1, 5, 10, 0, 6, 7]
    print(find_palindrome("character"))
    print(find_longest_monotonically_increasing(a))
    




main()
