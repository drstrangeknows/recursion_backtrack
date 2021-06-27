'''
Rather than the naive recursive approach where we reduce n by 1 at every recursion,
we try the binary search approach. e.g. if we have 2^6, then rather than going by 2*2^5, 
then 2*2*2^4 ... 2*2*2*2*2*2*2^0, we try to do it in a way 2^3*2^3. This way no. of steps 
is reduced by half at every step. Earlier we had O(n) complexity. By reducing into half,
the complexity becomes O(nlogn). Focus on the base case - for +ve n we will get 0 on dividing 
by 2, so the base comes is n==0, however for negative 'n', we can never get 0 on dividing by 2
(mathemarical reasons), so the base case is for n==-1. Afterwards, when recursion completes from 
base case, then we if n is odd or even and simplify the return value accordingly e.g. n==3, so
2^3 can be put as 2 * 2^2 OR 2^5 can be put as 2*2^2*2^2 - thus we have x*result*result
'''

def main():
    x = 21
    n = -6

    if n>0:
        result = findPositive(x, n)
    else:
        result = findNegative(x, n)

    print("The result", result)

def findNegative(x, n):
    if n==-1:
        return 1/x
    res = findNegative(x, n//2)
    if n%2 == 0:
        return 1/res * 1/res
    else:
        return 1/x * 1/res * 1/res

def findPositive(x, n):
    if n==0:
        return 1
    res = findPositive(x, n//2)
    if n%2 == 0:
        return res * res
    else:
        return x * res * res

if __name__=='__main__':
    main()
