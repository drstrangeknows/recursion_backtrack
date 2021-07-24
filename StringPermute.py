'''
String Permutation
Fill in boxes kind of problem
A_ _ - All combinations here
B_ _ - All combinations here
C_ _ - All combinations here

Recursion and backtracking. Start with 0th index then call the function in recursion
with i+1. Base condition if i==length of array.
Send the string as list, because in python string is immutable, so in the swap step
it will cause issue as assignment cannot be done. On reaching base condition, use join
to convert the current list to string
'''

the_str = "ABC"
result = []

def find_permute(data, i):
    if i==len(data):
        result.append("".join(data))
    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            find_permute(data, i+1)
            data[i], data[j] = data[j], data[i]
    return result

find_permute(list(the_str), 0)
print(result)