# 3. Staircase
# 1. n: size of stair
def staircase(n):
    # Write your code here
    result = ""
    for i in range(n):
        result += " " * (n - (i + 1)) + "#" * (i + 1) + "\n"

    print(result)
    return result


staircase(6)
staircase(49)
