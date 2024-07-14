
#!/usr/bin/python3
"""Module containing a function for minimum operations"""


def copy_all(count, file):
    """Function to copy the entire string content and increase
    count value by 1"""

    return count + 1, file


def paste(count, file, copy):
    """Function to concatenate the last copied content and
    increment the count value by 1"""

    return count + 1, file + copy

def len_of_remainder(curr, maxLen):
    return maxLen - len(curr)

def check_factor(n, srcLen):
    """Function to check if the current file length is a factor
    of the desired value

    ie., if src is a multiple of n"""

    if n % srcLen:
        return 0
    return 1

def minOperations(n):
    """Function to determine the minimum number of operations required
    to rewrite a single letter"""

    if not isinstance(n, int) or n < 1:
        return 0

    file = 'H'
    count = 0
    copy = ''
    rem = len_of_remainder(file, n)

    if (rem > 0):
        count, copy = copy_all(count, file)
        count, file = paste(count, file, copy)
    else:
        return count

    while (len(file) < n):
        rem = len_of_remainder(file, n)
        print({'lenFile': len(file), 'rem': rem, 'copyLen': len(copy)})
        if (check_factor(rem, len(file))):
            count, copy = copy_all(count, file)
            count, file = paste(count, file, copy)
        else:
            count, file = paste(count, file, copy)

    return count

"""
Min # of operations to reach 6 char: 5
Min # of operations to reach 18 char: 8
Min # of operations to reach 620 char: 40
Min # of operations to reach 1917030 char: 63911
"""

#def minOperations(n):
#    """Function to determine the minimum number of operations required
#    to rewrite a single letter"""

#    if not isinstance(n, int) or n < 1:
#        return 0

#    file = 'H'
#    count = 0
#    copy = ''

#    while (len(file) < n):
#        rem = len_of_remainder(file, n)
#        #factor = check_factor(n, len(file)

#        #if (factor) and (len(file + copy) <= n / 2):
#        #    count, copy = copy_all(count, file)
#        #else:
#        #    pass

#        #count, file = paste(count, file, copy)

#    return count
