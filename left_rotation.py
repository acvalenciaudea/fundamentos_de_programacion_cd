# 1 .Left Rotation
# https://www.hackerrank.com/challenges/array-left-rotation/problem
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

print(rotateLeft(2, [1, 2, 3, 4, 5]))
