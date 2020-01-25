""" 1.1 Is Unique """
#Determine if a string contains only unique chars without using non-string data
#structures like sets
if __name__ == "__main__":
    lst = "aabbcd"
    uniqueItems = []
    answer = True

	#If item not in uniqueItems, append it to the array
	#Otherwise, there is a duplicate value, set a to false
    for i in lst:
        if i not in uniqueItems:
            uniqueItems.append(i)
        else:
            answer = False
    print(answer)


""" 1.2 Check Permutation """
#Given two inputs: String word and String otherword, check if one is a
#permutation of the other.
#Input: "Taco Cat", "Tact Coa"
#Output: True
from collections import Counter

def isPerm():
    word = input()
    otherword = input()

	#Check that length of word and otherword match
	#and that Counter objects of each match
    return (len(word) == len(otherword)
        and Counter(word.lower()) == Counter(otherword.lower()))

print(isPerm())


""" 1.3 URLify """
#Given two inputs: String name and int length, print name with %20 in place of
#spaces and truncate string to length.
#Input: "Mr John Smith sldfkjsldf"
#Output: "Mr%20John%20Smith"
if __name__ == "__main__":
    name = input()
    length = int(input())

	#Reduce length of name from 0-length. Split on space and rejoin on %20.
    urld = "%20".join(name[0:length].split(" "))
    print(urld)


""" 1.4 Palindrome Permutation """
#Determine if words is a palindrome, then print out all permuatations of words
#regardless.
from itertools import permutations

words = "poop"

def isPalindrome(words):

    def permut(words):
        perms = set(["".join(i) for i in permutations(words)])
        print(perms)

    def toChars(words):
        words = words.lower()
        ans = ''

        for chars in words:
            if chars in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + chars
        permut(words)
        return ans

    def isPal(words):
        if len(words) <= 1:
            return True
        else:
            return words[0] == words[-1] and isPal(words[1:-1])
    return isPal(toChars(words))

print(isPalindrome(words))


""" 1.5 One Away """
#Determine if two strings are one letter away from having all matching characters
#If the difference between the strings is greater than 1 character, print False.
#Otherwise, print True.
if __name__ == "__main__":
    set1 = set(map(str, input()))
    set2 = set(map(str, input()))

    diff = set1.difference(set2)

    if (len(diff) > 1):
       print(False)
    else:
        print(True)


""" 1.6 String Compression """
#Compress a string into a count of characters and the number of times each
#occurs in the string consecutively
from itertools import groupby

if __name__ == "__main__":
    s = input()
    groups = []

    for key, group in groupby(list(s)):
        g = ("{}{}".format(key, len(list(group))))
        groups.append(str(g))
    print(" ".join(groups))


""" 1.7 Rotate Matrix """
#Rotate an NxN matrix of len 4 90 degrees (swap values of 4x4 arrays).
if __name__ == "__main__":
    array1 = [1, 2, 3, 4]
    array2 = [4, 3, 2, 1]
    array3 = [5, 6, 7, 8]
    array4 = [8, 7, 6, 5]

    for i in range(len(array1)):
        array2[i], array1[i] = array1[i], array2[i]
        array3[i], array2[i] = array2[i], array3[i]
        array4[i], array3[i] = array3[i], array4[i]
        array1[i], array4[i] = array4[i], array1[i]
    print(array1, array2, array3, array4)


""" 1.7 Zero Matrix """
#Note: Only works in Anaconda (because numpy)
#In a matrix, if a value is equal to zero, set its whole row and column to zero.
#Do not allow mutations of the array to make all values zero.
import numpy as np

if __name__ == "__main__":
    array1 = np.array([[0, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 0, 1]])

    zeroIndex1 = np.where(array1 == 0)[1] #create condition for testing col
    zeroIndex2 = np.where(array1 == 0)[0] #create condition for testing row

    array1[:, zeroIndex1] = 0 #Change column to zeros if zeroIndex is True
    array1[zeroIndex2,:] = 0 #Change row to zeros if zeroIndex is True

    print(array1)
